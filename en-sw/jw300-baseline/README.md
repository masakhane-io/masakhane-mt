# English to Swahili

Author: Kathleen Siminyu

## Data

	- The JW300 English-Swahili dataset.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1k2wUwWGc1JLBGlV5Ed0WMNnvp_GV_gm2?usp=sharing)

## Analysis

	Example 1
```sh
	Source:     She became pregnant at the age of 17 .
 	Reference:  Alipata mimba akiwa na umri wa miaka 17 .
 	Hypothesis: Alikuwa na mimba akiwa na umri wa miaka 17 .
```

	Example 2
```sh
	Source:     The Bible does not promote credulity .
 	Reference:  Biblia haipendekezi wepesi wa kuamini bila ushuhuda .
 	Hypothesis: Biblia haisemi kwamba mtu ana sifa ya kukubali sababu .
```

	Example 3
```sh
	Source:     What are some things that cause anxiety , and what can anxiety result in ?
 	Reference:  Ni baadhi ya mambo gani yanayosababisha hangaiko , na hangaiko laweza kutokeza nini ?
 	Hypothesis: Ni mambo gani yanayosababisha mahangaiko , na mahangaiko yanaweza kukufanyaje ?
```

	Example 4
```sh
	Source:     Lots of hugs and kisses .
 	Reference:  Kukumbatia kwingi na busu nyingi .
 	Hypothesis: Mabusu na mabusu .
```
# Results
	- BLEU train: 37.97
	- BLEU dev: 37.64
	- BLEU test: 48.94

