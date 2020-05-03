# English to Luo

Author: Kathleen Siminyu

## Data

	- The JW300 English-Luo dataset.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/drive/folders/19QcELteYcWnlFIhgbgOM5qSRSno5BcKY?usp=sharing)

## Analysis

Example 1
```sh
	Source:     He had written about the “ restoration of all things of which God spoke through the mouth of his holy prophets of old time . ”
 	Reference:  Noyudo Dunn osendiko wach “ loso gik moko duto odok makare , kaka Nyasaye nowacho gi dho jonabi duto maler nyaka a chakruok piny . ”
 	Hypothesis: Noyudo osendiko e wi “ weche duto ma Nyasaye ne wuoyo kuome kokalo kuom jonabi maler ma ne okoro chon . ”
```

Example 2
```sh
	Source:     Seeing ourselves in the light of what the Scriptures say can indeed be a powerful aid in identifying the intentions of the heart .
 	Reference:  Ka wanonore wawegi kaluwore gi gima Ndiko wacho , mano nyalo konyowa ng’eyo paro manie chunywa .
 	Hypothesis: Neno kaka Muma wacho nyalo bedo gima duong ’ ahinya e fwenyo chuny ng’ato .
```

Example 3
```sh
	Source:     It also gives me more reason to respect him as my father and spiritual head . ”
 	Reference:  Mano bende miyo amedo miye luor kaka wuonwa kendo kaka ng’at matayowa e weche mag lamo . ”
 	Hypothesis: Bende , omiyo amiyo luor kaka wuonwa kod wiye . ”
```

Example 4
```sh
	Source:     Their own willing obedience to what Jehovah requires should demonstrate that God’s rules are reasonable .
 	Reference:  Ka gin giwegi giikore luwo gima Jehova dwaro , mano biro nyiso ni chike Nyasaye gin chike mowinjore kendo inyalo makgi .
 	Hypothesis: Luwo chike Jehova e yo ma Jehova dwaro ni mondo onyis ni chike Nyasaye owinjore .
```
# Results
	- BLEU dev: 23.22
	- BLEU test: 32.64

