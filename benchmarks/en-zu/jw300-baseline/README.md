## Data 
JW300 : English-Zulu

## Model Architecture
  ### Text Preprocessing
    - Remove blank/empty rows : 9037(0.85 %) samples
    - Removed duplicates from source text : 82999(7.88 %) samples
    - Removed duplicates from target text : 5045(0.52 %) samples
    - Removed all numeric-only text : 182(0.02 %) samples
    - Removed rows where text is fewer than orequal to 8 characters long from source text: 6272(0.65 %) samples
    - Removed rows where text is fewer than orequal to 8 characters long from target text: 713(0.07 %) samples
    - Removed rows where text is in test set: 1068(0.11 %) samples
    
   ### BPE Tokenization
    - vocab size : 4000 (superior results than 10X)
    
   ### Model Config
    - Details in supplied config file but used fewer transformer layers than in default notebook, with more attention heads and lower embedding size
    - Trained for 235000 steps
    - Took few hours on a single P100 GPU on Google colab over a three days (stopped training  saved best model then reloaded that model the next day)
    
## Results

### Curious analysis of the tokenization
  > There are 66255 english tokens in the test set vocab, 2072 are unique 
  >
  > There are 67851 zulu tokens in the test set vocab, 2336 are unique
  >
  > These results are in the same notebook as used for training. (Could something similar help inform BPE vocab size choices ?)

### Translation results
> 2019-11-13 07:43:32,728 Hello! This is Joey-NMT.
>
> 2019-11-13 07:44:03,502  dev bleu:  13.64 [Beam search decoding with beam size = 5 and alpha = 1.0]
>
> 2019-11-13 07:44:24,289 test bleu:   4.87 [Beam search decoding with beam size = 5 and alpha = 1.0]`

Download model weights from : [here](https://drive.google.com/open?id=1-QLxP7xLqu-AqDQkm1XaCtDEex1Oseo0)
