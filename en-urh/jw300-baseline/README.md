# English to Urhobo

Author: iroro orife

## Data

	- The JW300 dataset was used for training Urhobo

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with models (https://drive.google.com/drive/folders/1-0REUw5fg_Y13wrKgE9RFD_iljOsXykr)

## Analysis

 	- Dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. This will make the model more generally useful outside of religious text translations.


# Results

	|  Tokenization  |  BLEU dev | BLEU test |
	|------------|:-------------:|------:|
	| BPE        |  15.91 | 28.82  |    
	| Word-level |  11.80 | 22.39  | 
