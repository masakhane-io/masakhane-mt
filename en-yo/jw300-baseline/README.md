# English to Yoruba

Author: Jamiil Toure Ali

## Data

	- The JW300 English-Urhobo dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/open?id=19hSc8eNY6iXy3rxHmicrFCRRlSaQIxIx)

## Analysis

Need to fine tune the model by playing with the parameter.

Example 1
```sh
	Source:     He is the Source of life , the One giving it as an undeserved gift through Christ .
	Reference:  Òun ni Orísun ìyè , Ẹni tí ń fi ìyè fúnni gẹ́gẹ́ bí ẹbùn tí a kò lẹ́tọ̀ọ́ sí nípasẹ̀ Kristi .
	Hypothesis: Òun ni Orísun ìyè , Ẹni tí ń fún un ní ẹ̀bùn àìlẹ́tọ̀ọ́sí nípasẹ̀ Kristi .
```

Example 2
```sh
	Source:     Now I had to find a legitimate line of work .
	Reference:  Torí náà , mo ní láti wá iṣẹ́ gidi .
	Hypothesis: Ní báyìí , mo ní láti rí iṣẹ́ tó dára gan - an .
```

Example 3
```sh
	Source:     Do I value material things more than my relationship with Jehovah and with people ?
	Reference:  Ṣé àwọn nǹkan tara ló jẹ mí lógún jù àbí àjọṣe mi pẹ̀lú Jèhófà àtàwọn èèyàn ?
	Hypothesis: Ṣé mo mọyì àwọn nǹkan tara ju àjọṣe mi pẹ̀lú Jèhófà àtàwọn èèyàn lọ ?
```

Example 4
```sh
	Source:     He has far more experience and stamina than you do , but he patiently walks near you .
	Reference:  Ẹni tẹ́ ẹ jọ ń lọ yìí mọ ọ̀nà yẹn dáadáa .
	Hypothesis: Ó ní ìrírí tó pọ̀ tó sì tún lágbára ju bó o ṣe ń ṣe lọ , àmọ́ ó ń fi sùúrù rìn nítòsí rẹ .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 29.15 | 36.74
