# English to Isoko

Author: iroro orife

## Data

	- The JW300 English-Isoko dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1r3A75C0Tzy67JdMF-_msaXwB3sNoQnmZ)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. This will make the model more generally useful outside of religious text translations. More precisely, we intend to clean up the following types of sentences:
```
	( Se 1 Pita 1 : 22 . )
	[ 1 ] ( edhe - ẹme avọ 1 ) 
	( Se Nehemaya 13 : 23 , 24 . )
	( b ) Ẹvẹ ma sai ro le utee mai tobọ ?
	( Se Ahwo Rom 15 : 1 , 2 . )
	( Se Eviavia 21 : 3 - 6 . )
	( Se 1 Jọn 5 : 14 , 15 . )
```

Example 1
```sh
	Source:     Still , words of apology are a strong force toward making peace .
	Reference:  Ghele na , eme unu - uwou u re fi obọ họ gaga evaọ eruo udhedhẹ .
	Hypothesis: Ghele na , eme unu - uwou yọ ẹgba ologbo nọ ma re ro ru udhedhẹ .
```

Example 2
```sh
	Source:     We can even ask God to ‘ create in us a pure heart . ’
	Reference:  Ma rẹ sae tubẹ yare Ọghẹnẹ re ọ ‘ kẹ omai eva efuafo . ’
	Hypothesis: Ma rẹ sae tubẹ yare Ọghẹnẹ re ọ ‘ ma omai eva efuafo . ’
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 32.58 | 38.05
Word-level | 32.38  | 38.91
