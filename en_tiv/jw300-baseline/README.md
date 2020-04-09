# English to Tiv

Author: Orevaoghene Ahia

## Data

	- The JW300 English - Tiv dataset.

## Model

- Default Masakhane Transformer translation model with JoeyNMT (trained for 150 epochs)
- [Link to google drive folder with best model](https://drive.google.com/file/d/1B_rP5oMzaYCZHcRPNJV7vcF2SpzLnRfj/view?usp=sharing)

## Analysis

Example 1
```sh
	Source:     What will we consider in the following article ?
	Reference:  Kanyi se time sha mi ke ’ kwaghngeren u a dondo nee ?
	Hypothesis: Ka nyi se time sha mi ken ngeren u a dondo nee ?
```

Example 2
```sh
	Source:     Published by Jehovah’s Witnesses but now out of print .
	Reference:  Ka Mbashiada mba Yehova ve gber ú ye , kpa kera ngu hegen ga .
	Hypothesis: Ka Mbashiada mba Yehova ve gber u ye , kpa mba gberen u hegen .
```

Example 3
```sh
	Source:     But another scroll was opened ; it is the scroll of life .
	Reference:  Nahan i bugh uruamabera . I shi i bugh ruamabera ugen kpaa , ka ruamabera u uma je la .
	Hypothesis: Kpa i bugh ruamabera ugen ; ka ihyurenruamabera i uma je la .
```

Example 4
```sh
	Source:     You cannot slave for God and for Riches . ”
	Reference:  Ne fatyô u eren Aôndo tom kua inyaregh kpaa ga . ”
	Hypothesis: Ne fatyô u eren Aôndo tom kua inyaregh kpaa ga . ”
```

# Results
	- BLEU dev :  30.29
	- BLEU test : 44.70
