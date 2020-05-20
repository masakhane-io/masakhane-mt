## ENGLISH TO SWAHILI
Author:  Sackey Freshia
## DATA

SAWA corpus - A parallel English-Kiswahili corpus (Guy De Pauw, Peter Waiganjo Wagacha, Gilles-Maurice de Schryver)
Link to corpus details - https://www.aclweb.org/anthology/W09-0702/

Corpus details:
English words: 542.1k

Swahili words: 442.9k

English Sentences - 33.6k

Swahili sentences - 33.6k


## Model
Default Masakhane transformer model (Using JoeyNMT)

## Analysis

Example 1
```sh
Source:     span
Reference:  shibiri
Hypothesis: kipingo
```
Example 2
```sh 

Source:     administer
Reference:  amuru
Hypothesis: msimamizi

```
Example 3
```sh
Source:     Then as to Samood, they were destroyed by an excessively severe punishment.
Reference:  Basi Thamudi waliangamizwa kwa balaa kubwa mno.
Hypothesis: Basi walipo angamizwa kwa Haki waliangamizwa kwa adhabu ya Moto ulio dhaahiri.

```
Example 4
```sh
Source:     You do not believe but say,
Reference:  Hamjaamini, lakini semeni:
Hypothesis: Hauamini ila husema:
```

## RESULTS
- BLEU train: 15.60
- BLEU dev: 15.00
- BLEU test: 3.60
