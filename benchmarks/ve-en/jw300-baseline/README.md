# Tshivenda to English

Author: Michael Beukman

## Data

	- The JW300 English-Tshivenda dataset.

## Model

- Default Masakhane Transformer translation model, [into-english notebook](https://github.com/masakhane-io/masakhane-mt/blob/master/starter_notebook_into_English_training.ipynb), with some changes, specifically changing the model parameters to be larger, as specified in the TODOs
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1YbmCF-xjT-bprVM0F7Sdr2Dj9kK8v_eP?usp=sharing)



The notebook contains the results of training the smaller model too, but the larger one showed superior results.

## Analysis
At the end of the training, the results were:
Example 1
```
Source:     Vhukuma , luvalo lwa ‘ muthu wa nga ngomu ’ lu nga kha ḓi ri xedza .
Reference:  Yes , the voice of “ the man we are inside ” may fail us .
Hypothesis: Yes , the conscience of “ the inner man ” may mislead us .
```
Example 2
```
Source:     • Ri nga vhuyelwa hani nga vhugudisi he Yesu a vhu ṋea vhafunziwa vhawe ?
Reference:  • How can we benefit from the training Jesus gave his disciples ?
Hypothesis: • How can we benefit from the training Jesus gave to his disciples ?
```
Example 3
```
Source:     Zwenezwo zwi ḓo ita uri ri kone u ḓivha phambano vhukati ha zwo lugaho na zwi songo lugaho na u dovha ra ḓivha phambano vhukati ha vhutsilu na vhuṱali . — Vhaheb . 5 : 14 ; Vhaef . 5 : 15 .


Reference:  To remain blameless in today ’ s complex and wicked world , we must train our “ powers of discernment ” so that we can distinguish not just right from wrong but also wise from unwise. — Heb . 5 : 14 ; Eph . 5 : 15 .


Hypothesis: That will enable us to know the difference between right and wrong and to know the difference between foolishness and wisdom and discreet peated. — Heb . 5 : 14 ; Eph . 5 : 15 .

```

# Results

 BLEU dev | BLEU test
 --- | ---
 40.20 | 46.82
