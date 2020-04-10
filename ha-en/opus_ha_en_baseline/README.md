# Hausa to English

Author: Moshooo O. Yekini

## Data

	- The JW300 English-Hausa dataset.
	- The Tanzil (Quran) English-Hausa dataset. 
	- The Wikimedia English-Hausa dataset.
	- The Tatoeba English-Hausa dataset

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model [here](https://drive.google.com/open?id=1q8gPqJM8NGLuweosN1aqRnMxnOywrZM7)
	- Updates on future experiments and other methods can be seen [here](https://github.com/WalePhenomenon/Hausa-NMT)

## Analysis

Example 0
```sh
	Source:     " Ka dũba yadda Muke sarrafa ãyõyi , tsammãninsu sunã fahimta ! "
	Reference:  Note how We explain the revelations , so that they may understand . ”
	Hypothesis: See how We make clear signs so that they may understand .
```
Example #1
```sh
	Source:     Dã Mun so , dã Mun mayar da shi ruwan zartsi . To don me bã ku gõdẽwa ?
	Reference:  If We pleased , We would have made it salty ; why do you not then give thanks ?
	Hypothesis: If We willed , We would have removed him with water , so why do you not give thanks ?
```
Example #2
```sh
	Source:     Kuma waɗanda suka kãfirta da ãyõyinMu , sũ ne ma 'abũta shu 'umci
	Reference:  and [ as for ] those who are bent on denying the truth of Our revelations , they are the people of the left hand ,
	Hypothesis: Those who disbelieve in Our signs are the people of the wicked .
```
Example #3
```sh
	Source:     Kuma Yanã sassaƙa jirgin cikin natsuwa , kuma a kõ yaushe waɗansu shugabanni daga mutãnensa suka shũɗe a gabansa , sai su yi izgili gare shi .
	Reference:  And he was building the ship , and every time that chieftains of his people passed him , they made mock of him .
	Hypothesis: He will send the ships in the bones , and when the leaders of his people have passed before him , they mock him .
```

# Results
	- BLEU train: 24.57
	- BLEU dev: 24.95
	- BLEU test:  25.27


