# Xhosa to English

Author: Samantha Ball
Student Number: 1603701

## Data

	- The JW300 English-Xhosa.

## Model

	- Masakhane Reverse Machine Translation - Transformer.
	- [Link to google drive folder with models] (https://drive.google.com/drive/folders/1jK2ur0rb_iWPB0Q9tUfX2F5x2LXAU1Lp?usp=sharing)

## Analysis

The model still struggles with tense and seems to exhibit confusion with respect to double negatives.

Example 1
```
	Source:     Ngaba umprofeti uYeremiya wayevuyiswa ngumsebenzi wakhe ?
	Reference:  Did the prophet Jeremiah find joy in his work ?
	Hypothesis: Was the prophet Jeremiah rejoice in his work ?
```

Example 2
```
	Source:     UPawulos wabongoza amaKristu awayekhonza nawo esithi : “ Nizeke kade umsindo kubo bonke . ” ( 1 Tesalonika 5 : 14 ) Ekubeni sonke singafezekanga yaye sisenza iimpazamo , ngokuqinisekileyo sifuna abantu babe nomonde kuthi , bazeke kade umsindo xa sibaphatha ngendlela engafanelekanga .

	Reference:  Paul urged fellow Christians : “ Be long-suffering toward all . ” ( 1 Thessalonians 5 : 14 ) Since all of us are imperfect and make mistakes , surely we want people to be patient with us , to be long-suffering when we err in our dealings with them .
	
	Hypothesis: Paul urged Christians to serve him : “ You must be long-suffering to all . ” ( 1 Thessalonians 5 : 14 ) Since all of us are imperfect and make mistakes , we certainly want men to be patient to us , even when we treat the wrong way .
```

Example 3
```
	Source:     Nathi ke , xa siyamkela ingqeqesho kaYehova , njengoko inikelwa ngabadala abangamaKristu , sitsho sihlale kwindlela esa ebomini . — IMize . 4 : 13 .
	Reference:  And accepting discipline from Jehovah , as given by Christian elders , keeps us on the way to life. — Prov . 4 : 13 .
	Hypothesis: When we accept Jehovah ’ s discipline , as given by Christian elders , we do not stay in the way we live in life. — Prov . 4 : 13 .
```


# Results
	- BLEU dev :  28.56 
	- BLEU test : 34.59 