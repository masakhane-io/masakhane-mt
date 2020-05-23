# English to Swahili

Author: Kathleen Siminyu

## Data

	- The JW300 English-Swahili dataset, 979526 lines.

## Model
  
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1J8uciIPbgwjpPGgmnZ_-lP5yVCxQK3ru?usp=sharing)

## Analysis
	- Tried out different BPE settings and noted correlated improvement on the BLEU scores the higher the BPE setting. Highest BLEU score I recorded was at BPE 35000. I could not go any higher due to 		local memory constraints but the upward trend of the BLEU scores relative to higher BPEs implies it might be worth exploring higher settings, as well as different bpe settings for the source and 		target languages.

BPE 4000
```sh
	BLEU dev: 37.64
	BLEU test: 48.94
```

BPE 5000
```sh
	2020-05-17 17:50:50,695 -  dev bleu:  39.18 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 17:52:23,187 - test bleu:  50.40 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 10000
```sh
	2020-05-17 17:53:39,073 -  dev bleu:  39.86 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 17:55:27,476 - test bleu:  50.79 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

BPE 15000
```sh
	2020-05-17 18:01:32,359 -  dev bleu:  40.59 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:02:58,512 - test bleu:  51.14 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 20000
```sh
	2020-05-17 18:09:11,771 -  dev bleu:  40.82 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:10:38,749 - test bleu:  51.26 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 25000
```sh
	2020-05-17 18:16:44,195 -  dev bleu:  40.95 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:17:22,420 - test bleu:  51.31 [Beam search decoding with beam size = 5 and alpha = 1.0]
```
BPE 30000
```sh
	2020-05-17 18:23:20,438 -  dev bleu:  41.46 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 18:23:56,595 - test bleu:  51.68 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

# Results
BPE 35000
```
	2020-05-17 20:55:37,506 -  dev bleu:  41.38 [Beam search decoding with beam size = 5 and alpha = 1.0]
	2020-05-17 20:56:15,027 - test bleu:  51.70 [Beam search decoding with beam size = 5 and alpha = 1.0]
```

