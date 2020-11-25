# English to Kikuyu

Author: Kathleen Siminyu

## Data

	- The JW300 English-Kikuyu dataset, 106699 lines.

## Model
  
	- Link to google drive folder with model(https://drive.google.com/open?id=1kjb2hXaSaG-Esl_SHJIptTZ9-Gw-er6f)

## Analysis
	- Tried out different BPE settings and managed some improvements on the baseline. Highest BLEU score I recorded was at BPE 20000. It might be worth exploring different bpe settings for the source 		and target languages. Results from different settings included in the analysis below.

BPE 4000
```sh
	BLEU dev: 23.83
	BLEU test: 36.06
```

BPE 5000
```sh
	2020-05-02 16:15:52,007 -  dev bleu:  23.90 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:19:02,219 - test bleu:  36.53 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 10000
```sh
	2020-05-02 16:24:16,890 -  dev bleu:  25.08 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:27:32,801 - test bleu:  37.39 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 15000
```sh
	2020-05-02 16:29:11,281 -  dev bleu:  25.60 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:32:22,789 - test bleu:  37.75 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 25000
```sh
	2020-05-02 16:38:37,910 -  dev bleu:  25.13 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:41:35,004 - test bleu:  37.35 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 30000
```sh
	2020-05-02 16:43:32,174 -  dev bleu:  25.36 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:46:28,748 - test bleu:  37.35 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 35000
```sh
	2020-05-02 16:48:32,963 -  dev bleu:  25.95 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:51:30,421 - test bleu:  37.77 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

# Results
BPE 20000
```
	2020-05-02 16:33:57,175 -  dev bleu:  25.14 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-02 16:36:53,670 - test bleu:  37.85 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

