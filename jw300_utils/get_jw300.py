import argparse
import opustools_pkg
import subprocess
import pandas as pd
import csv
from subword_nmt import learn_bpe, apply_bpe
import codecs
import os
import os.path

def create_corpus(src, trg, filedir, lc=False, seed=42):
  """ Create a BPE-preprocessed corpus with random train/dev/test splits. """
  source_file = "{}/jw300.{}-{}.{}".format(filedir, src, trg, src)
  target_file = "{}/jw300.{}-{}.{}".format(filedir, src, trg, trg)

  # download
  opus_reader = opustools_pkg.OpusRead(directory="JW300", source=src, target=trg, write_mode="moses", write=[source_file, target_file], suppress_prompts=True)
  opus_reader.printPairs()

  # unzip
  subprocess.Popen('gunzip JW300_latest_xml_{}-{}.xml.gz'.format(src, trg).split())

  # TMX file to dataframe
  source = []
  target = []
  with open(source_file) as f:
    for _, line in enumerate(f):
      source.append(line.strip())
  with open(target_file) as f:
    for _, line in enumerate(f):
      target.append(line.strip())

  df = pd.DataFrame(zip(source, target), columns=['source_sentence', 'target_sentence'])

  # drop duplicate translations
  df_pp = df.drop_duplicates()

  # drop conflicting translations
  df_pp.drop_duplicates(subset='source_sentence', inplace=True)
  df_pp.drop_duplicates(subset='target_sentence', inplace=True)

  # shuffle
  df_pp = df_pp.sample(frac=1, random_state=seed).reset_index(drop=True)

  # do the split between dev/test/train and create parallel corpora
  num_dev_patterns = 1000
  num_test_patterns = 1000

  # Lower case the corpora
  if lc:
    df_pp["source_sentence"] = df_pp["source_sentence"].str.lower()
    df_pp["target_sentence"] = df_pp["target_sentence"].str.lower()

  devtest = df_pp.tail(num_dev_patterns + num_test_patterns)
  test = devtest.tail(num_test_patterns) 
  dev = devtest.head(num_dev_patterns)
  stripped = df_pp.drop(df_pp.tail(num_dev_patterns + num_test_patterns).index)

  train_src_file = "{}/train.{}-{}.{}".format(filedir, src, trg, src)
  train_trg_file = "{}/train.{}-{}.{}".format(filedir, src, trg, trg)
  dev_src_file = "{}/dev.{}-{}.{}".format(filedir, src, trg, src)
  dev_trg_file = "{}/dev.{}-{}.{}".format(filedir, src, trg, trg)
  test_src_file = "{}/test.{}-{}.{}".format(filedir, src, trg, src)
  test_trg_file = "{}/test.{}-{}.{}".format(filedir, src, trg, trg)

  stripped[["source_sentence"]].to_csv(train_src_file, header=False, index=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  stripped[["target_sentence"]].to_csv(train_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  dev[["source_sentence"]].to_csv(dev_src_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  dev[["target_sentence"]].to_csv(dev_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  test[["source_sentence"]].to_csv(test_src_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  test[["target_sentence"]].to_csv(test_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  
  # train bpe (separately for src and trg)
  src_bpe_file = "{}/{}-{}.{}.bpe".format(filedir, src, trg, src)
  trg_bpe_file = "{}/{}-{}.{}.bpe".format(filedir, src, trg, trg)
  learn_bpe.learn_bpe(codecs.open(train_src_file, encoding='utf-8'), codecs.open(src_bpe_file, "w", encoding='utf-8'), 10000)
  learn_bpe.learn_bpe(codecs.open(train_trg_file, encoding='utf-8'), codecs.open(trg_bpe_file, "w", encoding='utf-8'), 10000)

  # apply bpe
  def bpe_process(inp, outp, codes):
    codes = codecs.open(codes, encoding='utf-8')
    inp = codecs.open(inp, encoding='utf-8')
    outp = codecs.open(outp, "w", encoding='utf-8')
    bpe = apply_bpe.BPE(codes)
    for line in inp:
        outp.write(bpe.process_line(line))

  for split in ["train", "dev", "test"]:
    for side in [src, trg]:
      bpe_process("{}/{}.{}-{}.{}".format(filedir, split, src, trg, side), "{}/{}.{}-{}.bpe.{}".format(filedir, split, src, trg, side), "{}/{}-{}.{}.bpe".format(filedir, src, trg, side))
  
if __name__ == "__main__":
  parser = argparse.ArgumentParser('JW300 corpus downloader and pre-processor for translations from english.')
  parser.add_argument('trgs', nargs='+', help='Target languages.')
  parser.add_argument('--output_dir', help='Output directory for corpus.', default='jw300')
  parser.add_argument('--lc', action='store_true', help='Lowercase the data.')  
  parser.add_argument('--seed', type=int, help='Random seed for corpus shuffling.', default=42)
  args = parser.parse_args()
  src="en"
  if not os.path.isdir(args.output_dir):
    os.makedirs(args.output_dir)
  langfile = open("{}/langs.txt".format(args.output_dir), "a")

  for i, trg in enumerate(args.trgs):
    print('Creating corpus for {}-{} ({}/{}).'.format(src, trg, i+1, len(args.trgs)))
    try:
      create_corpus(src, trg, args.output_dir, args.lc, args.seed)
      langfile.write("{}\n".format(trg))
    except:
      print('Could not process {}.'.format(trg))
      continue



