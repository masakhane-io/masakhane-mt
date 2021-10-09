# Kimbundu to English

Author: Kavilan Nair and Thishen Packirisamy

## Data

	- The JW300 Kimbundu - English.

## Model

	- Default Masakhane Transformer translation model.
	- The model https://drive.google.com/drive/folders/1XJKcm-w6kbAOYJuxNGSm7gSXV2IrqKmI?usp=sharing 

## Analysis

Example #0

```sh	
    Source:     Muhatu’ami Nora ni eme , tu sakidila kiavulu Jihova mu ioso ia tu bhana , etu tuene mu suinisa ue akuetu phala ku lola Jihova . — Malakiia 3 : 10 .
    Reference:  Nora and I are very grateful to Jehovah for all his kind provisions , and we encourage others also to test Jehovah out. — Malachi 3 : 10 .
    Hypothesis: My wife Noran and I are grateful to Jehovah for all we have given , and we encourage others to make sure that Jehovah is pleasing to him. — Malachi 3 : 10 .
```

Example #1
```sh
    Source:     Kiki ki kuatekesa benge - benge o jiphange a sola mimbu phala o madiskursu .
    Reference:  This can be helpful , for example , when a brother needs to choose a song for a public talk .
    Hypothesis: This is especially helpful for the brothers who choose songs to talk .
```

Example #2
```sh
    Source:     Kuene ngó maubhezelu a iiadi — o ubhezelu ua kidi ni ubhezelu ua makutu .
    Reference:  The Bible teaches that there are two types of religion — true religion and false religion .
    Hypothesis: There are two religious beliefs — true worship and false worship .
```

Example #3
```sh
    Source:     Eie ua buika o kidifuanganu kia Nzambi , o diiala . ” — TERTULIANO , O TRAGE DAS MULHERES , KU HAMA IA KAIIADI , K . K .
    Reference:  You destroyed so easily God ’ s image , man . ” — TERTULLIAN , ON THE APPAREL OF WOMEN , SECOND CENTURY C.E.
    Hypothesis: You will destroy God ’ s image , and the man who is the man . ” — TERTERTANS , THE WORD , BEAR , BEAR .
```
# Results
	- BLEU dev :   28.64 
	- BLEU test :  30.57
