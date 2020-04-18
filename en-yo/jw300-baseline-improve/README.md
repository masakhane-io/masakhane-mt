# English to Yoruba

Author: Kolawole Tajudeen

## Data

	- The JW300 English-Yoruba dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/open?id=11df3sipDiv7wXtdRnB01KH72krFsNU4r)

## Analysis

TO DO

Example 1
```sh
	Source:     He is the Source of life , the One giving it as an undeserved gift through Christ .
	Reference:  Òun ni Orísun ìyè , Ẹni tí ń fi ìyè fúnni gẹ́gẹ́ bí ẹbùn tí a kò lẹ́tọ̀ọ́ sí nípasẹ̀ Kristi .
	Hypothesis: Òun ni Orísun ìyè , Ẹni tí ń fi í fúnni gẹ́gẹ́ bí ẹ̀bùn àìlẹ́tọ̀ọ́sí nípasẹ̀ Kristi .
```

Example 2
```sh
	Source:     Do I value material things more than my relationship with Jehovah and with people ?
	Reference:  Ṣé àwọn nǹkan tara ló jẹ mí lógún jù àbí àjọṣe mi pẹ̀lú Jèhófà àtàwọn èèyàn ? 
	Hypothesis: Ǹjẹ́ mo mọyì àwọn nǹkan tara ju àjọṣe mi pẹ̀lú Jèhófà àti pẹ̀lú àwọn èèyàn lọ ?
```

Example 3
```sh
	Source:     He has far more experience and stamina than you do , but he patiently walks near you .
	Reference:  Ẹni tẹ́ ẹ jọ ń lọ yìí mọ ọ̀nà yẹn dáadáa . 
	Hypothesis: Ó ní ìrírí tó pọ̀ gan - an , ó sì tún ní ìrírí tó ju tìẹ lọ , àmọ́ ó fi sùúrù rìn nítòsí rẹ .
```

Example 4
```sh
	Source:     Now I had to find a legitimate line of work .
	Reference:  Torí náà , mo ní láti wá iṣẹ́ gidi .
	Hypothesis: Ní báyìí , mo ní láti wá iṣẹ́ tó dára .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 31.03 | 38.62

## BPE

- [Link to google drive folder with bpes](https://drive.google.com/open?id=1-63nP5CqUa8JRGLRxRY6vKZd9jgM-Y9_)
