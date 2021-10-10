# Southern Ndebele to English

Author: Michael Beukman

## Data

	- The JW300 English-Southern Ndebele dataset.

## Model

- Default Masakhane Transformer translation model, [into-english notebook](https://github.com/masakhane-io/masakhane-mt/blob/master/starter_notebook_into_English_training.ipynb), with some changes, specifically changing the model parameters to be larger, as specified in the TODOs. We trained for 100 epochs.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1-sejnAAX40Vhtj7416Us64NSTjexsJTu?usp=sharing)



The notebook contains the results of training the smaller model too, but the larger one showed superior results, an improvement of 34.97 to 40.56 on the test BLEU.

## Analysis
At the end of the training, the results were:


Example 0
```
Source:     Ngokukhamba kwesikhathi , watjhada nomkakhe wanje , uRiley .
Reference:  Later , he married his present wife , Riley .
Hypothesis: Later , she married her wife now , Riley .
```
Example 1
```
Source:     Ebujamwenobu , inengi labazesiweko libeke isibonelo esihle .
Reference:  In this connection , most anointed ones have set a wonderful example .
Hypothesis: In these situations , many of the anointed set a good example .
```
Example 2
```
Source:     ( IzE . 3 : 17 ; 17 : 30 ) Yeke nasizimisele ukwenza intando kaZimu akunalitho uSathana angasenza yona bona singathembeki kuZimu . — Job . 2 : 3 ; 27 : 5 .
Reference:  ( Acts 3 : 17 ; 17 : 30 ) If we are resolved to do God ’ s will , there is nothing Satan can do to break our integrity. — Job 2 : 3 ; 27 : 5 .
Hypothesis: ( Acts 3 : 17 ; 17 : 30 ) So if we are determined to do God ’ s will , Satan can do nothing to disobey him. — Job 2 : 3 ; 27 : 5 .
```
Example 3
```
Source:     Kubayini amaKrestu kufuze alwele ukuhlala aphapheme ngokomoya ?
Reference:  Why must Christians strive to stay spiritually awake ?
Hypothesis: Why should Christians strive to remain spiritually alert ?
```

# Results

 BLEU dev | BLEU test
 --- | ---
 36.14 | 40.56