## Data 
JW300 : Zulu to English (English-Zulu Reverse Machine Translation)

Author: Musa Ntuli


## Model 
Link to google drive folder with model(https://drive.google.com/drive/folders/10MSShnH8-V4ssOCpbEvFW4ZdVkop7iVd?usp=sharing)


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

## Analysis

Example #0
Source:     20 Ungaqonda ukuthi kungani kunjalo ngabaningi .
Reference:  20 You can understand why that is the case with many .
Hypothesis: 20 You can understand why so many .

Example #1
Source:     OFakazi BakaJehova endaweni yakini bayokujabulela ukuxoxa nawe okwengeziwe mayelana nemfundo yeBhayibheli eqhutshwa emphakathini wakini . *
Reference:  Jehovah ’ s Witnesses in your area will be glad to share more information with you about the Bible education program that is currently being carried on in your community . *
Hypothesis: Jehovah ’ s Witnesses in your area will enjoy discussing more about Bible education that are conducted in your society . *

Example #2
Source:     Ukuhlakanipha nokuqonda nako kwakubalulekile .
Reference:  Wisdom and discretion were also important .
Hypothesis: Wisdom and discernment was important .

Example #3
Source:     Ngemva komhlangano wezizwe eRome ngalelo hlobo , ngaba nelungelo lokuba khona emhlanganweni owawuseNuremberg , eJalimane .
Reference:  After the international convention in Rome that summer , I was privileged to attend the convention in Nuremberg , Germany .
Hypothesis: After the international convention in Rome that summer , I had the privilege of attending the convention in Nuremberg , Germany .

    
## Results
  - BLEU dev: 28.48
  - BLEU test: 38.33

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
