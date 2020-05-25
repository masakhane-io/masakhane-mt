# English to Igbo

Author: iroro orife

## Data

	- The JW300 English-Igbo dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/1bVPKPkaivIT9k23ydbSlVj3Qwd3GJZf0)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. 
One very nice aspect of the Igbo translations are the proper tonal and orthographic diacritic forms predicted by 
the model. This is not a feature that is available with Google Translate!

Example 1
```sh
	Source: It’s not about the alcohol .
	Reference: Nsogbu ya abụghị na ịṅụ mmanya na - aba n’anya na - agụ ya .
	Hypothesis:        Ọ bụghị banyere mmanya na - aba n’anya .	
```

Example 2
```sh
	Source: Is this also the case with your neighborhood ?
	Reference:        Ọ̀ bụ otú a ka ọ dịkwa n’agbata obi gị ?
	Hypothesis: Nke a ọ̀ bụkwa ihe banyere ndị agbata obi gị ?
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 33.51 | 34.85
