# Hausa to English

Author: Tunde Ajayi

## Data

	- The JW300 English-Hausa dataset.
	
## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model [here](https://drive.google.com/drive/folders/1tt9kmMQGmD2e1bLDARnPfdcZ-a2gOkYZ?usp=sharing)
	
## Analysis

Example 0
```sh
	Source: ( Romawa 12 : 18 ) Kuma za su sami kwanciyar hankali don suna bin ƙa’idodin Littafi Mai Tsarki . — Ishaya 48 : 18 .
 	Reference: They experience peace in their lives by applying Bible principles . ​ — Isaiah 48 : 18 .
 	Hypothesis: And they will find security because they heed Bible principles . ​ — Isaiah 48 : 18 .
```

Example 1
```sh
	Source: ( Aya ta 20 ) Jehobah yana begen sake ganin yaransa .
 	Reference: * By all means I shall have pity upon him . ” “ datse ” miyagu don nagargarun mutane su ji daɗin zama a duniya .
 	Hypothesis: Jehovah hope to see his children again .
```

Example 2
```sh
	Source:     Masana sun gano cewa wannan ne dalilin da ya sa gwamnatocin duniya ba za su iya kawo ƙarshen cin hanci da rashawa ba .
 	Reference:  Experts admit that this is why human governments cannot eliminate corruption .
 	Hypothesis: The scholars realize that this is why world governments cannot bring an end to corruption and corruption .
```

Example 3
```sh
	Source:     A cikin sura ta 7 ta littafin Romawa , Bulus ya bayyana ikon zunubi a jikinmu ajizi .
 	Reference:  In the 7th chapter of Romans , Paul acknowledged the power of sin on the imperfect flesh .
 	Hypothesis: In chapter 7 of Romans , Paul revealed the power of sin in our imperfect flesh .
```

# Results
	- BLEU train: 28.97
	- BLEU dev: 29.44
	- BLEU test: 34.52
