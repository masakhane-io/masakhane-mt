# Efik to English

Author: Max Parkin

## Data

	- The JW300 Efik - English

## Model

	- Default Masakhane Transformer translation model (into English - https://github.com/masakhane-io/masakhane-mt/blob/master/starter_notebook_into_English_training.ipynb). 
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1-00S9U6pud58BcA88pNbHDEc03wg5PKv?usp=sharing)

## Analysis

Example 1
```
	Source: Margaritha esidara ndinọ mme owo oro ẹsidide ẹdidep n̄kpọ ke akwa ufọkurua oro odude ekpere , ikọ ntiense , ndien esop nnyịn ke mfọnido ọmọnọ nnyịn ndusụk efakutom oro ẹkperede ufọk nnyịn , ndien emi esinam edi mmemmem n̄kpọ ọnọ nnyịn ndikwọrọ ikọ adan̄a nte nsọn̄idem nnyịn ayakde .
 	Reference: Margaritha enjoys witnessing to people at a nearby supermarket , and the congregation has kindly set aside some territory for us near our home , which makes it easier for us to preach as our health permits .
 	Hypothesis: Margaritha has been glad to give people who are going to buy the walls near , witnessing , and our congregation has been given us some territory that are near our home , and this is easy to preach as much as our health is allowed .
```

Example 2
```
	Source: Se ikakpade mi idem ikan edi ke enye okosụk ekpe mi se ekesikpede !
 	Reference: Surprisingly , I still got the same pay !
 	Hypothesis: What I was surprised but that he still had to pay me !
```

Example 3
```
	Source: Nte an̄wan̄ade , ibọrọ mbụme oro edi ata akpan n̄kpọ ọnọ nnyịn , ndien iyenen̄ede ineme enye .
 	Reference: Clearly , the answer to that question is of great importance to us , and we will consider it further .
 	Hypothesis: Clearly , the answer is a vital challenge for us , and we will consider it .
```

Example 4
```
	Source: Ẹma ẹsinyụn̄ ẹsịn iduot ke idet erọn̄ emi ẹsidade ẹnam ọfọn̄ .
 	Reference: In addition , wool was often dyed .
 	Hypothesis: The wooden sheep were also used to make clothes .
```

# Results
	- BLEU dev :  28.20 
	- BLEU test : 29.08
