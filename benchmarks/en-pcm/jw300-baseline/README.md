# English to Nigerian Pidgin

Author: Kelechi Ogueji

## Data

	- The JW300 English - Nigerian Pidgin dataset.

## Model

- Default Masakhane Transformer translation model with JoeyNMT (trained for 200 epochs)
- [Link to google drive folder with best model](https://drive.google.com/file/d/1KYH7egDLQVE_FYN-Bu5sreMzCj9Xl3yV/view?usp=sharing)

## Analysis

- The model learns some relationships between different references to the same entity. This can be seen in example 2, where David is referred to as a King. 
- In some other examples, the model makes hypothesis that are grammatically and qualitatively correct, but do not exactly match the reference translation. 

Example 1
```sh
	Source:     How have Jehovah’s Witnesses shown that they engage in the preaching work with the right motive ?
	Reference:  Wetin show sey na the correct mind Jehovah Witness people take dey preach ?
	Hypothesis: How Jehovah Witness people take dey preach the good news ?
```

Example 2
```sh
	Source:     The psalmist David wrote : “ O Hearer of prayer , to you people of all sorts will come .
	Reference:  David write sey : ‘ You wey dey hear prayer , na you everybody go come meet .
	Hypothesis: King David write for Bible sey : ‘ E dey pray for una , because na you go choose well .
```

Example 3
```sh
	Source:     How do we know that Jehovah’s Witnesses have God’s spirit ?
	Reference:  How we take know sey Jehovah Witness people get holy spirit ?
	Hypothesis: How we take know sey Jehovah Witness people get holy spirit ?
```

Example 4
```sh
	Source:     Jesus told his disciples : “ If you ask anything in my name , I will do it . ”
	Reference:  Jesus tell im disciple dem sey : ‘ If una use my name beg for anything , I go do am . ’
	Hypothesis: Jesus tell im disciple dem sey : ‘ If una ask me anything , I go do anything wey I fit do . ’
```

# Results
	- BLEU dev :  12.78
	- BLEU test : 24.29
