# English to Urhobo

Author: iroro orife

## Data

	- The JW300 English-Urhobo dataset.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with models (https://drive.google.com/drive/folders/1-0REUw5fg_Y13wrKgE9RFD_iljOsXykr)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. This will make the model more generally useful outside of religious text translations.

Example 1
```sh
	Source:     But freedom from what ?
	Reference:  Ẹkẹvuọvo , ẹdia vọ yen egbomọphẹ na che si ayen nu ?
	Hypothesis: ( 1 Pita 3 : 1 ) Ẹkẹvuọvo , die yen egbomọphẹ 
```

Example 2
```sh
	Source:     Today he is serving at Bethel .
	Reference:  Nonẹna , ọ ga vwẹ Bẹtẹl .
	Hypothesis: Nonẹna , ọ ga vwẹ Bẹtẹl asaọkiephana .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 15.91 | 28.82
Word-level | 11.80  | 22.39
