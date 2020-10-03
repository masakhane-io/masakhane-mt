# English to Kikongo

Author: Berthine Nyunga Mpinda

## Data

	- The JW300 English- Kikongo.

## Model

	- Default Masakhane Transformer translation model.
	- The model can be found [here](https://drive.google.com/file/d/101PotGLqO3yXMLnK-9m4aoxvgPK78aqR/view?usp=sharing)
	
## Analysis

Example 1
```ln
    Source:     Gone will be the need for hospitals and medications .
    Reference:  Ke vekala mfunu a tupitalu ko ngatu nlongo .
    Hypothesis: O muntu kafwete tambula nzenza ye mboka .
	
```

Example 2
```ln
    Source:     Such a circumstance can be very distressing .
    Reference:  Ediadi dilenda kikilu kutukendeleka .
    Hypothesis: E diambu diadi dilenda kendalala .
```

Example 3
```ln
    Source:    If you are unsure of the answers to any of these questions , you may request a copy of the brochure What Does God Require of Us ?
   Reference:  Nkia nkanikinu miakaka mia Nkand’a Nzambi milenda wokesa e kiese muna nzo ?
   Hypothesis: Avo ke tuna ye mvutu za yuvu yayi ko , nga olenda lomba lusadisu lwa finkanda - nkanda O Nzambi Adieyi Kieleka Kevavanga kwa Yeto ? ”
```
# Results
	- BLEU dev :   26.69
	- BLEU test :  36.28
