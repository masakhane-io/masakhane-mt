## Nigerian Pidgin to English
Author:  Arnol Fokam
## DATA

```sh
- The JW300 English-Nigerian Pidgin dataset
```

## Model

Transformer model (Using JoeyNMT)

Link  to model:

```sh
https://drive.google.com/drive/folders/1-E-FCHU1-ELacdJHLQt5vUhB8Xp1XQDc?usp=sharing
```

## Analysis

Example 1
```sh
Source:     Jehovah tell Ezekiel sey make e write on top two stick .
Reference:  Jehovah told his prophet Ezekiel to write on two sticks .
Hypothesis: Jehovah specifically inspired Ezekiel to write on two sticks .
```
Example 2
```sh 
Source:     BEFORE that time , I don dey like the truth wey I dey learn from Bible .
Reference:  MY INTEREST in Bible truth had already been aroused earlier .
Hypothesis: BEING FORE , I have always enjoyed teaching Bible truths .
```
Example 3
```sh
Source:     But because Ireland na Catholic country , e come be like sey , ‘ trouble dey sleep yanga go wake am . ’
Reference:  What “ silly ” things to do in such a Catholic country !
Hypothesis: But it was as a Catholic country , which was as the none of Ireland , “ hurtful to get air . ”
```
Example 4
```sh
Source:     For 1987 , one brother tell me sey make I go check one person wey like our message for Balykchy .
Reference:  In 1987 a brother asked me to visit an interested person living in the town of Balykchy .
Hypothesis: In 1987 , a brother asked me to look for a public message in Balykchy .
```

## RESULTS
- BLEU train: 21.43
- BLEU dev: 21.56
- BLEU test: 32.55
