# English to Sesotho

Author: [Jason Webster](https://github.com/jasonrobwebster/)

A `en_st_process.ipynb` and `en_st_train_from_drive.ipynb` notebook are present in order to be able to run the processing and training steps at two different times. The `fuzzywuzzy` preprocessing step took long enough to consume a full Google Colab instance's time allocation, so a seperate notebook was needed in order to train the model from the preprocessed data. The `en_st_train_from_drive.ipynb` notebook also contains code for testing on the Autshumato dataset, though these results are reported in a seperate folder.

## Training Data

	- The JW300 dataset.

## Preprocessing

	- Removed duplicate sentences
	- Removed similar sentences with fuzzywuzzy and a similarity score above 0.95
	- 40 000 BPE codes used

## Model

	- Default Masakhane Transformer translation model (see `en_st_train_from_drive.ipynb` for detailed config)
	- Link to google drive folder with model (https://drive.google.com/drive/folders/1--C5IwyI_P0B4_-nAsBDaBgrGqm5ABvY?usp=sharing)
	- Trained for approx 9h30min

## Analysis

 	- TODO

# Results
	- JW300 `test.en` and `test.st`
	- BLEU dev: 46.15
	- BLEU test: 41.23

	- Note: It is probably best to train this model for longer, as it was close to timing out on Google Colab (was manually stopped)
	- Note: Will likely benefit from optimising the number of BPE codes