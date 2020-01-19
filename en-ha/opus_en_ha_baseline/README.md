# English to Hausa

Author: Adewale Akinfaderin

## Data

	- The JW300 English-Hausa dataset.
	- The Tanzil (Quran) English-Hausa dataset. 
	- The Wikimedia English-Hausa dataset.
	- The Tatoeba English-Hausa dataset

## Model

 - Default Masakhane Transformer translation model.
 - Link to google drive folder with model [here](https://drive.google.com/drive/folders/1vukbwb6wqs3WDNsUVfuMr02gctiXMTqq?usp=sharing)
 - Updates on future experiments and other methods can be seen [here](https://github.com/WalePhenomenon/Hausa-NMT)

## Analysis

Example 1
```sh
	Source:     She became pregnant at the age of 17 .
 	Reference:  Alipata mimba akiwa na umri wa miaka 17 .
 	Hypothesis: Alikuwa na mimba akiwa na umri wa miaka 17 .
```

Example 2
```sh
	Source:     The fact that the Bible is available in all major languages on earth is a testimony to what ?
 	Reference:  Wane tabbaci ne ake da shi cewa akwai Littafi Mai Tsarki cikin dukan manyan harsunan duniya ?
 	Hypothesis: Gaskiyar cewa Littafi Mai Tsarki yana da amfani a dukan harsuna da yawa a duniya shaida ne ga menene ?
```

Example 3
```sh
	Source:     But why were there not among the generations before you those possessing understanding , who should have forbidden the making of mischief in the earth , except a few of those whom We delivered from among them ?
 	Reference:  To , don me mãsu hankali ba su kasance daga mutãnen ƙarnõnin da suke a gabãninku ba , sunã hani daga ɓarna a cikin ƙasa ? fãce kaɗan daga wanda Muka kuɓutar daga gare su ( sun yi hanin ) .
 	Hypothesis: To , don me , waɗansu al 'ummõmi daga gabãninku ba su kasance a gabãninku ba , sunã hani daga ɓarna a cikin ƙasa ? fãce kaɗan daga wanda Muka kuɓutar daga gare su ?
```

# Results
	- BLEU train: 35.88
	- BLEU dev: 38.26
	- BLEU test: 41.11




