# English to Ẹ̀dó

Author: iroro orife

## Data

	- The JW300 English-Ẹ̀dó (bin) dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/18P6HH9wavVpaR3UufoiUsTeqMnkvc1He)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. Also it is very small, which is the primary limiting factor on being able to learn anything useful.

Example 1
```sh
	Source:     What are the rewards for being humble ?
	Reference:  Ma ghaa mu egbe rriotọ , de afiangbe na lae miẹn ?
	Hypothesis: De emwi nọ khẹke ne ọmwa nọ dizigha ọyẹvbu ru ?
```

Example 2
```sh
	Source:     One reason is that he rules with love . Indeed , our hearts are touched by how he chooses to exercise his sovereignty .
	Reference:  Ọna ẹre ọ si ẹre ne Arriọba ọghẹe na maan sẹ ọghe emwa ọvbehe , ere ọ vbe si ẹre ne emwa ne irẹn kha yan na mwẹ agbẹkunsotọ .
	Hypothesis: Ọ keghi re odẹ ọkpa ne ima ya rhiẹre ma wẹẹ ima hoẹmwẹ ọnrẹn kevbe wẹẹ , irẹn ẹre ọ gele mwẹ asẹ ne a ya khaevbisẹ .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 7.92 | 12.49
Word-level | 5.99  | 8.24
