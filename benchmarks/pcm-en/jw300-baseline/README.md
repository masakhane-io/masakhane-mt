## ENGLISH TO SWAHILI
Author:  Sackey Freshia
## DATA

```sh
- The JW300 English-Swahili dataset
```

## Model

Transformer model (Using JoeyNMT)

Link  to model:

```sh
https://drive.google.com/file/d/1XB00wUjQsZL81GeCLreE5Iclss4m7LgY/view?usp=sharing
```

## Analysis

Example 1
```sh
Source:     Katika mwaka wa 1997 wasichana 90,000 walipata mimba huko Uingereza .
Reference:  There were almost 90,000 conceptions to teenagers in England in 1997 .
Hypothesis: In 1997 90,000 girls became pregnant in Britain .
```
Example 2
```sh 

Source:     Lazima ujikakamue kujua kile isemacho Biblia kusudi usadikishwe na kutegemeka kwake .
Reference:  You must exert yourself to find out what the Bible says so as to be convinced of its reliability .
Hypothesis: You must decide to know what the Bible says to be convinced and reliable to him .
```
Example 3
```sh
Source:     Kwenye kituo kikuu katika jiji la Strasbourg , ambalo ni makao ya Mahakama ya Ulaya ya Haki za Kibinadamu , wasafiri walipanga foleni wakisubiri kupata nakala yao .
Reference:  In Strasbourg , home of the European Court of Human Rights , travelers at the central station line up patiently to receive their copy .
Hypothesis: At the center in the city of Strasbourg , a European Court of Human Rights , travelers arranged to send up in waiting for their copy .
```
Example 4
```sh
Source:     Kukumbatia kwingi na busu nyingi .
Reference:  Lots of hugs and kisses .
Hypothesis: Membering many and discreet .
```

## RESULTS
- BLEU train: 36.14
- BLEU dev: 36.08
- BLEU test: 48.79
