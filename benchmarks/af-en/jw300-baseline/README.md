# Afrikaans to English

Author: Michael Beukman

## Data

	- The JW300 English-Afrikaans dataset.

## Model

- Default Masakhane Transformer translation model, [into-english notebook](https://github.com/masakhane-io/masakhane-mt/blob/master/starter_notebook_into_English_training.ipynb), with some changes, specifically changing the model parameters to be larger, as specified in the TODOs. We trained for 23 epochs.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1XOgy2VNkQ_7oDWvW2EKiaJvNGf13qT29?usp=sharing)



## Analysis
At the end of the training, the results were:


Example 0
```
Source:     My pa was die groepkneg , die term wat destyds gebruik is vir die broer wat die leiding in ’ n gemeente geneem het .
Reference:  Father was the company servant , the term then used for the one taking the lead in a congregation .
Hypothesis: My father was the group servant , the term used at that time for the brother who took the lead in a congregation .
```
Example 1
```
Source:     Die aantrekkingskrag is verstaanbaar , want adolessensie is ’ n tyd wanneer ’ n mens jouself leer ken en jou gevoelens op ’ n manier uitdruk wat tot ander spreek en hulle ontroer .
Reference:  The appeal is understandable , for adolescence is a time of learning about oneself and revealing one ’ s feelings in a way that reaches and moves others .
Hypothesis: The attraction is understandable , for adolescence is a time when one comes to know oneself and expresses feelings in a way that speaks to others and touches them .
```
Example 2
```
Source:     Hy het selfs die woorde “ u seun Dawid ” met verwysing na homself gebruik , moontlik om eerbiedig te erken dat Nabal ouer as hy was .
Reference:  He even referred to himself as “ your son David , ” perhaps a respectful acknowledgment of Nabal ’ s greater age .
Hypothesis: He even used the words “ your son David ” with reference to himself , perhaps to respectfully acknowledge that Nabal was older than he was .
```

Example 3
```
Source:     HOEKOM MOET ONS GEESTELIKE DOELWITTE STEL ?
Reference:  WHY SET SPIRITUAL GOALS ?
Hypothesis: HOW DO WE SHOULD WE STECTS DOELVITS ?
```


## Qualitative Analysis
It looked like the model struggles with sentences that only contain capital letters (see Example 3).

In addition to this, the model seems to do translation much more literally than the reference, as in the following examples:


Source: `Hy het selfs die woorde “ u seun Dawid ” met verwysing na homself gebruik`

Hypothesis: `He even used the words “ your son David ” with reference to himself`

Reference: `He even referred to himself as “ your son David , ”`

The model's translation above is very literal, almost word for word, whereas the reference is more holistically translated, even though both mean the same thing.

## Observations
The dataset was quite large, comparably larger than other African languages, and this made training quite slow, and 20 epochs took about 32 hours to train.

# Results

 BLEU dev | BLEU test
 --- | ---
 51.47 | 57.22