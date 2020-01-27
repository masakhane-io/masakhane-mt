# English to Ẹ̀sán

Author: iroro orife

## Data

	- The JW300 English-Ẹ̀sán (ish) dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1FhIlYmQVlVBCUL5t_BJv6fOcVdAGHqZg)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. Also it is very small, which is the primary limiting factor on being able to learn anything useful.

Example 1
```sh
	Source:     In contrast with the people who show the widespread lack of love today , those who worship Jehovah have genuine love for their fellow man .
	Reference:  Ene ga iJehova ẹlẹnan wo mhọn oyẹẹ da ibo ele , ele bha diabe ene iga Jehova ne bha hoẹmhọn ibo ele .
	Hypothesis: Ene ẹbho ne bunbun wo manman ha mhọn urẹọbhọ da ẹbho n
```

Example 2
```sh
	Source:     We should also strive to help others spiritually .
	Reference:  Ahamiẹn mhan re ẹghe bhi otọ rẹ ha luẹ iBaibo , yẹ deba ene gene guanọ nin ele ga iJehova ha muobọ , ọ dẹ rẹkpa mhan rẹ ziẹn ikolu nin mhan bi Jehova koko mhọnlẹn .
	Hypothesis: Mhan dẹ sabọ rẹkpa mhan rẹ sabọ ha mhọn urẹọbhọ bọsi eria .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 4.94 | 6.25
Word-level | 3.39  | 5.30
