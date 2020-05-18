# English to Kamba

Author: Kathleen Siminyu

## Data

	- The JW300 English-Kamba dataset, 58312 lines.

## Model
  
	- Link to google drive folder with model(https://drive.google.com/open?id=1kjb2hXaSaG-Esl_SHJIptTZ9-Gw-er6f)

## Analysis
	- Tried out different BPE settings and managed some improvements on the baseline. Highest BLEU score I recorded was at BPE 25000. It might be worth exploring different bpe settings for the source 		and target languages. Results from different settings included in the analysis below.

BPE 4000
```sh
	BLEU dev: 14.83
	BLEU test: 24.96
```

BPE 5000
```sh
	2020-05-10 17:08:17,436 -  dev bleu:  15.00 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:08:53,304 - test bleu:  26.06 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 10000
```sh
	2020-05-10 17:09:16,286 -  dev bleu:  16.63 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:09:51,410 - test bleu:  27.20 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 15000
```sh
	2020-05-10 17:10:16,787 -  dev bleu:  16.72 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:10:53,812 - test bleu:  27.34 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 20000
```sh
	2020-05-10 17:11:20,392 -  dev bleu:  16.00 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:11:57,920 - test bleu:  27.04 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 30000
```sh
	2020-05-10 17:13:45,951 -  dev bleu:  14.93 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:14:28,275 - test bleu:  25.84 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 35000
```sh
	2020-05-10 17:15:06,838 -  dev bleu:  14.83 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:15:51,339 - test bleu:  25.19 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 40000
```sh
	2020-05-10 17:16:32,342 -  dev bleu:  15.03 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:17:19,359 - test bleu:  25.87 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

# Results
BPE 25000
```
	2020-05-10 17:12:29,184 -  dev bleu:  16.70 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-10 17:13:12,772 - test bleu:  27.90 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

