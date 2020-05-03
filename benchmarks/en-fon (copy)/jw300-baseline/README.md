# English to Fɔngbe

Author: Kevin DEGILA

## Data

	- The JW300 English- Fɔngbe.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/open?id=11doYa-jfV9pwgqP9xQGbD2CYYQJ5ey9P)

## Analysis

Example 1
```sh
	Source:     I love pioneering in this territory .
 	Reference:  Un yí wǎn nú gbexosin - alijitɔ́zɔ́ wiwa ɖò fí enɛ .
 	Hypothesis: Un yí wǎn nú gbexosin - alijitɔ́zɔ́ ɖò fí e un ɖè é .
```

Example 2
```sh
	Source:     “ Too numerous to recount ” are the “ wonderful works ” we can thank and praise Jehovah for daily !
 	Reference:  “ Nùjiwǔ ” e Jehovah bló bɔ mǐ sixu dokú tɔn n’i bo lɛ́ kpa susu n’i ayihɔngbe ayihɔngbe é “ sukpɔ́ ” tawun .
 	Hypothesis: “ Togun Mawu tɔn ” jiwǔ tawun , bɔ mǐ sixu dokú nú Jehovah , bo dokú n’i .
```

Example 3
```sh
	Source:     Some Christian parents serving in a foreign - language field have come to realize that their children’s interest in the truth has waned .
 	Reference:  Mɛjitɔ́ Klisanwun e ɖò sinsɛnzɔ́ wà wɛ ɖò ayǐ e jí è nɔ dó gbè ɖevo ɖè lɛ é ɖé lɛ wá ɖ’ayi wu ɖɔ jlǒ e vǐ emitɔn lɛ ɖó nú nugbǒ ɔ é ɖò ɖiɖekpo wɛ .
 	Hypothesis: Mɛjitɔ́ Klisanwun ɖé lɛ nɔ sɛ̀n sinsɛnzɔ́ ɖò xá e mɛ vǐ yetɔn lɛ nɔ dó gbè ɖevo mɛ é ɖé lɛ mɔ ɖɔ nugbǒ ɔ ɖó kpɔ́ .
```

Example 4
```sh
	Source:     You certainly recognize that Jewish man as the one who came to be known as the apostle Paul .
 	Reference:  É ɖò wɛn ɖɔ a tuùn nya Jwifu enɛ e è wá ylɔ ɖɔ mɛsɛ́dó Pɔlu é .
 	Hypothesis: É ɖò wɛn ɖɔ a tuùn ɖɔ Jwifu e wá tuùn mɛsɛ́dó Pɔlu é wɛ nyí mɛsɛ́dó Pɔlu .
```
# Results
	- BLEU train: 20.28
	- BLEU dev: 21.61
	- BLEU test: 31.07
