# English to Swahili

Author: Kathleen Siminyu

## Data

	- The JW300 English-Luo dataset, 154941 lines.

## Model
  
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1_q4Gj4cIAbhNxTU3XOa1OH9Sxtg2cvEM?usp=sharing)

## Analysis
	- Tried out different BPE settings and managed some improvements on the baseline. Highest BLEU score I recorded was at BPE 30000. It might be worth exploring different bpe settings for the source 		and target languages. Results from different settings included in the analysis below.

BPE 4000
```sh
	BLEU dev: 23.22
	BLEU test: 32.64
```

BPE 5000
```sh
	2020-05-17 17:50:01,865 -  dev bleu:  23.32 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 17:51:18,137 - test bleu:  32.52 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 10000
```sh
	2020-05-17 17:52:12,396 -  dev bleu:  24.26 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 17:53:26,893 - test bleu:  32.97 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 15000
```sh
	2020-05-17 17:54:28,069 -  dev bleu:  24.55 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 17:55:46,813 - test bleu:  33.43 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 20000
```sh
	2020-05-17 18:01:41,447 -  dev bleu:  25.34 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:03:03,470 - test bleu:  33.38 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 25000
```sh
	2020-05-17 18:09:26,069 -  dev bleu:  24.81 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:10:45,675 - test bleu:  33.68 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 35000
```sh
	2020-05-17 20:35:45,530 -  dev bleu:  25.08 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 20:36:23,282 - test bleu:  33.70 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 40000
```sh
	2020-05-17 20:43:32,542 -  dev bleu:  24.75 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 20:44:11,245 - test bleu:  33.58 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

# Results
BPE 30000
```
	2020-05-17 20:28:46,395 -  dev bleu:  25.24 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 20:29:20,937 - test bleu:  34.33 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

