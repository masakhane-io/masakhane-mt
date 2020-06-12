## ENGLISH TO SWAHILI
Author:  Sackey Freshia
## DATA

SAWA corpus - A parallel English-Kiswahili corpus (Guy De Pauw, Peter Waiganjo Wagacha, Gilles-Maurice de Schryver)
Link to corpus details - https://www.aclweb.org/anthology/W09-0702/

JW300 - Bibilical text.

SAWA Corpus details:
English words: 542.1k

Swahili words: 442.9k

English Sentences - 33.6k

Swahili sentences - 33.6k

The training data is a combination of SAWA and JW300 data. The test set was created from data derived from both corpora.

## Model
Transformer model (Using JoeyNMT)
Link  to model:
```sh
https://drive.google.com/drive/folders/1i4Mro3_obqKs24XQfgjpcD9I5kkfxhG9?usp=sharing
```

## Analysis

Example 1
```sh
Source:     When I reminded him that the ministers of other religions could visit their people , he became enraged .
Reference:  Nilipomkumbusha kwamba wahudumu wa dini nyingine wangeweza kuwatembelea watu wao , alikasirika sana .
Hypothesis: Nilipomkumbusha kwamba wahudumu wa dini nyingine wangeweza kuwatembelea watu wao , alikasirika .
```
Example 2
```sh 

Source:     Although the water disappears , the salts and the minerals are left behind .
Reference:  Ingawa maji huvukizwa , chumvi na madini hubaki .
Hypothesis: Ingawa maji hutoweka , chumvi na madini huachwa nyuma .

```
Example 3
```sh
Source:     These trends began in earnest in the 1960 ’ s with what came to be called the green revolution .
Reference:  Kilimo hicho kilianza kuenea sana katika miaka ya 1960 kupitia zile zilizojulikana kama harakati za kuboresha uzalishaji .
Hypothesis: Mabadiliko hayo yalianza kwa bidii katika miaka ya 1960 na yale yaliyokuja kuitwa mapinduzi ya kijani - kibichi .
```
Example 4
```sh
Source:     The desire to work in a more fruitful territory is often another motive ​ — and properly so .
Reference:  Mara nyingi kichocheo kingine ni tamaa ya kuhubiri katika eneo lenye matokeo zaidi — nacho chafaa .
Hypothesis: Mara nyingi tamaa ya kufanya kazi katika eneo lenye matokeo ni nia nyingine — na kwa njia inayofaa .
```

## RESULTS
- BLEU train: 34.06
- BLEU dev: 34.99
- BLEU test: 17.61
