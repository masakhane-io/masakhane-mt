## Data 
JW300 : English-Southern Ndebele

## Model Architecture
  ### Text Preprocessing
    - Remove blank/empty rows : 1856(1.78 %) samples
    - Removed duplicates from source text : 6335(6.20 %) samples
    - Removed duplicates from target text : 410(0.43 %) samples
    - Removed all numeric-only text :39(0.04 %) samples
    - Removed rows where text is fewer than orequal to 8 characters long from source text: 1653(1.73 %) samples
    - Removed rows where text is fewer than orequal to 8 characters long from target text: 133(0.14 %) samples
    - Removed rows where text is in test set: 1049(1.12 %) samples
    
   ### BPE Tokenization
    - vocab size : 4000 (superior results than 10X)
    
   ### Model Config
    - Details in supplied config file but used fewer transformer layers than in default notebook, with more attention heads and lower embedding size
    - Trained for 75000 steps
    - Took few hours on a single P100 GPU on Google colab over a two days (stopped training  saved best model then reloaded that model the next day)
    
## Results

> 019-11-28 13:37:38,730 Hello! This is Joey-NMT.
>
>2019-11-28 13:38:08,636  dev bleu:  14.93 [Beam search decoding with beam size = 5 and alpha = 1.0]
>
>2019-11-28 13:39:12,496 test bleu:   4.01 [Beam search decoding with beam size = 5 and alpha = 1.0]

Download model weights from : [here](https://drive.google.com/open?id=11uI8GOx0meBiEAv7sHrLVF1sjkiSIZ0g)
.
