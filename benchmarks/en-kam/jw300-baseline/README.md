# English to Kamba

Author: Kathleen Siminyu

## Data

	- The JW300 English-Kamba dataset.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1DL5JICbtNQ1hC285l3w7TiQ5LufryVw2?usp=sharing)

## Analysis

Example 1
```sh
	Source:     Gideon wondered how it would be possible for him to “ save Israel out of Midian’s hand . ”
 	Reference:  Mũlaĩka ũsu nĩwaneenie vandũ va Mũmbi na amũĩkĩĩthya Ngiteoni kana Yeova aĩ vamwe nake .
 	Hypothesis: Ngiteoni eekũlasya ũndũ ũtonya ‘ kũtia Isilaeli . ’
```

Example 2
```sh
	Source:     It includes links to lists of Witnesses currently imprisoned for their faith .
 	Reference:  7 : 12 ) Walika Kĩsesenĩ kya jw.org no wone masyĩtwa ma Ngũsĩ ila syovetwe .
 	Hypothesis: Amwe ma Ngũsĩ sya Yeova nĩmoovetwe nũndũ wa mũĩkĩĩo woo .
```

Example 3
```sh
	Source:     And then she would try to return to Hosea .
 	Reference:  Na ĩndĩ kyamina kũsembany’a na endwa makyo Yeova aĩtye kĩkatata kũmũsyokea Osea .
 	Hypothesis: Na ĩndĩ nĩwasyokie Avakuki ambĩĩa kũsyokea Hosua .
```

Example 4
```sh
	Source:     The Bible itself says : “ The green grass dries up , the blossom withers , but the word of our God endures forever . ” ​ — Isaiah 40 : 8 .
 	Reference:  Mbivilia yaĩtye atĩĩ : “ Nyeki nĩyũmaa , na ĩlaa nĩyĩvovaa ; ĩndĩ ndeto ya Ngai waitũ ĩkekala tene na tene . ” — Isaia 40 : 8 .
 	Hypothesis: Mbivilia yaĩtye atĩĩ : “ Na mũisyo ũla mũnene , na ndeto ya Ngai , ĩndĩ ndeto ya Ngai yĩkalĩte tene na tene . ” — Isaia 40 : 8 .

```
# Results
	- BLEU dev: 14.83
	- BLEU test: 24.96

