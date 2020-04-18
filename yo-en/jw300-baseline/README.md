# English to Yoruba

Author: Kolawole Tajudeen

## Data

	- The JW300 English-Yoruba dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/open?id=1W6XW7ldm2OjPmBsM-PGI25FShYoITd5W)

## Analysis

TO DO

Example 1
```sh
	Source:     Ìlú Áńtíókù , tá a ti kọ́kọ́ pe àwọn ọmọ ẹ̀yìn Jésù ní Kristẹni , ni Pọ́ọ̀lù ti bẹ̀rẹ̀ ìrìn àjò míṣọ́nnárì rẹ̀ àkọ́kọ́ .
	Reference:  On his first missionary tour , he started from Antioch , where Jesus ’ followers were first called Christians .
	Hypothesis: Paul began his first missionary journey in Antioch , who was called Christians .
```

Example 2
```sh
	Source:     Torí pé mò ń tẹ̀ lé àwọn ìlànà Bíbélì ló jẹ́ kí n wà láàyè títí dòní
	Reference:  I am alive today because of applying Bible principles
	Hypothesis: Because I live by Bible principles , I am living forever
```

Example 3
```sh
	Source:     Àjíǹde àkọ́kọ́ tí Bíbélì mẹ́nu kàn nìyẹn .
	Reference:  That was the first resurrection of Bible record .
	Hypothesis: That is the first resurrection mentioned in the Bible .
```

Example 4
```sh
	Source:     Bíi ti afinimọ̀nà tá a mẹ́nu kàn nínú àpèjúwe wa yẹn , Jèhófà sọ pé òun máa ran àwọn tó bá fẹ́ bá òun rìn lọ́wọ́ , ó sì ní kí wọ́n wá bá òun dọ́rẹ̀ẹ́ .
	Reference:  Like the guide in our illustration , Jehovah kindly extends his helping hand and his friendship to those who seek to walk with him .
	Hypothesis: Like the guidance mentioned in our illustration , Jehovah said that he would help those who want to walk with him and invite them to come to him .
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE| 30.48 | 39.44

## BPE

- [Link to google drive folder with bpes](https://drive.google.com/open?id=1Og5bjxC6Je4d_qzp6XwayWy1nNp5_F5q)
