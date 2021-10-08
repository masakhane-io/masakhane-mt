# English to Nigerian Pidgin

Author: Olatomiwa Akinlaja

## Data

	- The JW300 English - Nigerian Pidgin dataset.

## Model

- Default Masakhane Transformer translation model with JoeyNMT (trained for 30 epochs)
- [Link to google drive folder with best model](https://drive.google.com/drive/folders/1f1CE3Gf_CUAvO1xqR1dqzzfJkAILmGnZ?usp=sharing)

## Analysis

Example 0
```sh
	Source:     Jehovah tell Ezekiel sey make e write on top two stick .
	Reference:  MY INTEREST in Bible truth had already been aroused earlier .
	Hypothesis: Jehovah told Ezekiel that he was written on two two two two two men .
```

Example 1
```sh
	ource:     BEFORE that time , I don dey like the truth wey I dey learn from Bible .
	Reference:  MY INTEREST in Bible truth had already been aroused earlier .
	Hypothesis: BEING THE Bible truth was a real real understanding .
```

Example 2
```sh
	Source:     But because Ireland na Catholic country , e come be like sey , ‘ trouble dey sleep yanga go wake am . ’
	Reference:  What “ silly ” things to do in such a Catholic country !
	Hypothesis: But in Ireland was a Catholic , the Catholic , “ I was sick . ”
```

Example 3
```sh
	Source:     For 1987 , one brother tell me sey make I go check one person wey like our message for Balykchy .
	Reference:  In 1987 a brother asked me to visit an interested person living in the town of Balykchy .
	Hypothesis: In 1987 , one brother told me that I would be a person who is in Balyky .
```

# Results
	- BLEU dev :  17.09
	- BLEU test : 24.95
