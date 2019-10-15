#-*- coding: utf-8 -*-

import argparse
import opustools_pkg
import subprocess
import pandas as pd
import csv
from subword_nmt import learn_bpe, apply_bpe
import codecs
import os
import os.path

def create_corpus(src, trg, en_test_sents, filedir, lc=False, seed=42, bpe_size=10000, dev_size=1000, test_dir="test"):
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
  skip_lines = []
  with open(source_file) as f:
    for i, line in enumerate(f):
      # skip sentences that are contained in the test set
      if line.strip() not in en_test_sents:
        source.append(line.strip())
      else:
        skip_lines.append(i)
  with open(target_file) as f:
    for j, line in enumerate(f):
      # only add to corpus if corresponding source was not skipped
      if j not in skip_lines:
        target.append(line.strip())
  print('Loaded data and skipped {} lines since contained in test set.'.format(len(skip_lines)))

  df = pd.DataFrame(zip(source, target), columns=['source_sentence', 'target_sentence'])

  # drop duplicate translations
  df_pp = df.drop_duplicates()

  # drop conflicting translations
  df_pp.drop_duplicates(subset='source_sentence', inplace=True)
  df_pp.drop_duplicates(subset='target_sentence', inplace=True)

  # shuffle
  df_pp = df_pp.sample(frac=1, random_state=seed).reset_index(drop=True)

  # do the split between dev/test/train and create parallel corpora
  num_dev_patterns = dev_size
  # test data is loaded from file
  # num_test_patterns = 1000 

  # Lower case the corpora
  if lc:
    df_pp["source_sentence"] = df_pp["source_sentence"].str.lower()
    df_pp["target_sentence"] = df_pp["target_sentence"].str.lower()

  dev = df_pp.tail(num_dev_patterns)
  stripped = df_pp.drop(df_pp.tail(num_dev_patterns).index)

  train_src_file = "{}/train.{}-{}.{}".format(filedir, src, trg, src)
  train_trg_file = "{}/train.{}-{}.{}".format(filedir, src, trg, trg)
  dev_src_file = "{}/dev.{}-{}.{}".format(filedir, src, trg, src)
  dev_trg_file = "{}/dev.{}-{}.{}".format(filedir, src, trg, trg)
  # tests are already created
  #test_src_file = "{}/test.{}-{}.{}".format(filedir, src, trg, src)
  #test_trg_file = "{}/test.{}-{}.{}".format(filedir, src, trg, trg)

  stripped[["source_sentence"]].to_csv(train_src_file, header=False, index=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  stripped[["target_sentence"]].to_csv(train_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  dev[["source_sentence"]].to_csv(dev_src_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  dev[["target_sentence"]].to_csv(dev_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  #test[["source_sentence"]].to_csv(test_src_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")
  #test[["target_sentence"]].to_csv(test_trg_file, index=False, header=False, quotechar="", quoting=csv.QUOTE_NONE, escapechar="\\", sep="§")

  
  # train bpe (separately for src and trg)
  src_bpe_file = "{}/{}-{}.{}.bpe".format(filedir, src, trg, src)
  trg_bpe_file = "{}/{}-{}.{}.bpe".format(filedir, src, trg, trg)
  learn_bpe.learn_bpe(codecs.open(train_src_file, encoding='utf-8'), codecs.open(src_bpe_file, "w", encoding='utf-8'), bpe_size)
  learn_bpe.learn_bpe(codecs.open(train_trg_file, encoding='utf-8'), codecs.open(trg_bpe_file, "w", encoding='utf-8'), bpe_size)

  # apply bpe
  def bpe_process(inp, outp, codes):
    codes = codecs.open(codes, encoding='utf-8')
    inp = codecs.open(inp, encoding='utf-8')
    outp = codecs.open(outp, "w", encoding='utf-8')
    bpe = apply_bpe.BPE(codes)
    for line in inp:
        outp.write(bpe.process_line(line))

  for split in ["train", "dev"]:
    for side in [src, trg]:
      bpe_process("{}/{}.{}-{}.{}".format(filedir, split, src, trg, side), "{}/{}.{}-{}.bpe.{}".format(filedir, split, src, trg, side), "{}/{}-{}.{}.bpe".format(filedir, src, trg, side))

  for side in [src, trg]:
    bpe_process("{}/{}.{}-{}.{}".format(test_dir, "test", src, trg, side), "{}/{}.{}-{}.bpe.{}".format(filedir, "test", src, trg, side), "{}/{}-{}.{}.bpe".format(filedir, src, trg, side))

if __name__ == "__main__":
  parser = argparse.ArgumentParser('JW300 corpus downloader and pre-processor for translations from english.')
  parser.add_argument('trgs', nargs='+', help='Target languages.')
  parser.add_argument('--output_dir', help='Output directory for corpus.', default='jw300')
  parser.add_argument('--lc', action='store_true', help='Lowercase the data.')  
  parser.add_argument('--seed', type=int, help='Random seed for corpus shuffling.', default=42)
  parser.add_argument('--bpe_size', type=int, help='Number of BPE subwords.', default=10000)
  parser.add_argument('--dev_size', type=int, help='Size of the development set.', default=1000)
  parser.add_argument('--test_dir', help='Path to test sets to filter from training and development data.', default="test")
  args = parser.parse_args()
  src="en"
  if not os.path.isdir(args.output_dir):
    os.makedirs(args.output_dir)
  langfile = open("{}/langs.txt".format(args.output_dir), "a")

  # first load global test sentences to filter
  # store english portion in set for quick filtering checks
  en_test_sents = set()
  filter_test_sents = "{}/test.en-any.en".format(args.test_dir)
  j = 0
  with open(filter_test_sents) as f:
    for line in f:
      en_test_sents.add(line.strip())
      j += 1
  print('Loaded {} global test sentences to filter from the training/dev data.'.format(j))

  for i, trg in enumerate(args.trgs):
    print('Creating corpus for {}-{} ({}/{}).'.format(src, trg, i+1, len(args.trgs)))
 #   try:
    create_corpus(src, trg, en_test_sents, args.output_dir, args.lc, args.seed, args.bpe_size, args.dev_size, args.test_dir)
    langfile.write("{}\n".format(trg))
#    except:
#      print('Could not process {}.'.format(trg))
#      continue



