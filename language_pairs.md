# Current Language Pairs

- Total number of unique language pairs: 44
- Total number of benchmarks: 52

Training data for the models reported below comes from [JW300](http://opus.nlpl.eu/JW300.php) unless indicated otherwise (in brackets). For details about data source, preprocessing, training configurations etc. check the notebooks provided in the folders linked for each language pair.
The Test BLEU score is computed on the JW300 [test sets](https://github.com/masakhane-io/masakhane-mt/tree/master/jw300_utils/test) with [SacreBLEU](https://github.com/mjpost/sacrebleu) (`tokenize=None` to maintain the original JW300 tokenization). 

| Source | Target | Best Test BLEU | Link | [Avalailable on Masakhane-web](http://translate.masakhane.io/) |
---------|--------|-----------|------| ------|
| English | Afrikaans (Autshumato) | 19.56 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-af/autshumato-baseline) |  :x: |
| English | Afrikaans (JW300) | 45.48 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-af/jw300-baseline) | :x: |
| English | Amharic | 2.03 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-am/jw300-amharic-baseline) | :x: |
| English | Arabic (TED, custom) | 9.28 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ar/jw300-tedtalk-baseline) | :x: |
| English | Cinyanja | 30 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-nya/jw-300-baseline) | :x: |
| English | Dendi | 22.30 | [link](https://github.com/Jamiil92/masakhane/tree/master/en-ddn/live.bible.is-baseline) | :x: |
| English | Efik | 33.48 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-efi/jw300-baseline) | :x: |
| English | Ẹ̀dó | 12.49 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-bin/jw300-baseline) | :x: |
| English | Ẹ̀sán | 6.25 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ish/jw300-baseline) | :x: |
| English | Fon | 31.07 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-fon/jw300-baseline) | :x: |
| English | Hausa | 41.11 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ha/opus_en_ha_baseline) | :x: |
| English | Igbo | 34.85 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ig/jw300-baseline) | :heavy_check_mark: |
| English | Isoko | 38.91 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-iso/jw300-baseline) | :x: |
| English | Kamba | 27.90 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-kam/tuned-jw300-baseline) | :x: |
| English | Kimbundu | 32.76 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-kmb/jw300-baseline) | :x: |
| English | Kikuyu | 37.85  | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-ki/tuned-jw300-baseline) | :x: |  
| English | Lingala | 48.64 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ln/jw300-baseline) | :heavy_check_mark: |
| English | Luo | 34.33 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-luo/fine-tuned-jw300-baseline) | :x: |
| English | Nigerian Pidgin |  24.29   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-pcm/jw300-baseline) | :x: |
| English | Northern Sotho (Autshumato) | 19.56  | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-nso/autshumato-baseline) | :x: |
| English | Northorn Sotho (JW300) | 15.40 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-nso/jw300-baseline) | :x: |
| English | Sesotho  | 41.23 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-st) | :x: |
| English | Setswana |  19.66   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-tn/autshumato-baseline) | :heavy_check_mark: |
| English | Shona | 30.84  | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-sn/jw300-shona-baseline) | :heavy_check_mark: |
| English | Southern Ndebele |  4.01 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-nr/ari-jw300-baseline) | :x: |
| English | Southern Ndebele | 26.61  | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-nr/jw300-baseline) | :x: |
| English | kiSwahili (JW300) | 51.70  | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-sw/fine-tuned-jw300-baseline) | :heavy_check_mark: |
| English | kiSwahili (SAWA) | 3.60 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-sw/sawa-baseline) | :x: |
| English | kiSwahili (SAWA+JW300) | 17.61 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-sw/sawa%2Bjw300_baseline) | :x: |
| English | Tigrigna (JW300) | 4.02 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ti/jw300-tigrigna-baseline) | :x: |
| English | Tigrigna (JW300+Tatoeba+more) | 14.88  | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ti/tigmix-baseline) | :x: |
| English | Tiv | 44.70 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-tiv/jw300-baseline) | :x: |
| English | Tshiluba | 42.52 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-lua/jw300-baseline) | :heavy_check_mark: |
| English | Tshivenda | 49.57 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-ve/jw300-baseline) | :x: |
| English | Twi | 34.57 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-twi/jw300-baseline) | :x: |
| English | Urhobo |  28.82   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-urh/jw300-baseline) | :x: |
| English | isiXhosa (Autshumato) | 13.32 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-xh/autshumato-baseline) | :x: |
| English | isiXhosa (JW300) | 6.00 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-xh/jw300-baseline) | :x: |
| English | Xitsonga (JW300) |  4.44   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ts) | :x: |
| English | Xitsonga (Autshumato) | 13.54 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-ts/autshumato-baseline) | :x: |
| English | Yoruba |  38.62   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-yo/jw300-baseline-improve) | :x: |
| English | isiZulu (Autshumato) |  1.96   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/en-zu/autshumato-baseline) | :x: |
| English | isiZulu (JW300)|  4.87 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/en-zu/jw300-baseline) | :x: |
| Efik | English | 33.68 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/efi-en/jw300-baseline) | :x: |
| Hausa | English | 25.27 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/ha-en/opus_ha_en_baseline) | :x: |
| Shona | English | 38.42 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/sn-en/jw300-baseline) | :x: |
| Swahili | English | 48.79 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/sw-en) | :x: |
| Yoruba  | English |  39.44   | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/yo-en/jw300-baseline) | :heavy_check_mark: |
| French | Lingala | 39.81 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/fr-ln/french-lingala-baseline) | :x: |
| French | Swahili Congo | 33.73 | [link](https://github.com/masakhane-io/masakhane/tree/master/benchmarks/fr-swc/french-swahili_drc_baseline) | :x: |
| Nigerian Pidgin | English | 24.95 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/pcm-en/jw300-baseline) | :x: |
| Tshivenda | English | 46.82 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/ve-en/jw300-baseline) | :x: |
| Southern Ndebele | English | 40.56 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/nr-en/jw300-baseline) | :x: |
| Afrikaans (JW300) | English | 57.22 | [link](https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks/af-en/jw300-baseline) | :x: |

