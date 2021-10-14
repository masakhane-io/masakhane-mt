# IGBO TO ENGLISH
**Authors:**
Dino Anastasopoulos (1900661)
Jesse Bristow (1875955)
Chloe Smith (1877342)

## DATA
```sh
The JW300 Igbo-English dataset
```

## Model

Transformer model (Using JoeyNMT)

Link  to model:

```sh
https://drive.google.com/drive/folders/1tAWvmFu2eiuWqjOfThXaGrYqBI0Yx01U?usp=sharing
```

## Analysis
Example 1
```sh
Source:     N’ọnọdụ ndị dị otú ahụ , ụfọdụ pụrụ iche na nanị ihe a ga - eme bụ ịgba alụkwaghịm . — Ilu 13 : 12 .

Reference:  Under such circumstances , some may feel that the only option is divorce. — Proverbs 13 : 12 .

Hypothesis: In such situations , some may feel that only the only thing will be divorc. — Proverbs 13 : 12 .
```

Example 2
```sh
Source:     Ọ bụ n’ihi na Chineke , bụ́ Isi Iyi nke ndụ , nyere iwu na ụkpụrụ ndị dị na Baịbụl “ maka ọdịmma [ anyị ] , ” ma ọ bụkwanụ “ ka o wee dịrị [ anyị ] mma . ” — Diuterọnọmi 10 : 13 ; Bible Nsọ nke Union Version .

Reference:  Because as the Source of life , God sets out his laws and standards in the Bible “ for [ our ] good , ” or “ for [ our ] own well-being . ” — Deuteronomy 10 : 13 ; New Revised Standard Version .

Hypothesis: Because God , the Source of life , commands and principles that are “ for [ our ] good ” or “ to be good . ” — Deuteronomy 10 : 13 ; The Bible Version .
```

Example 3
```sh
Source:     Iche echiche otú ahụ na - eme ka ọtụtụ ndị ghara ime ihe ga - enyere ha aka ka ahụ́ sie ha ike , ha enwee ike na - eme ihe dịịrị ha ná ndụ .

Reference:  Such a fatalistic view holds many back from improving their health and leading a more productive life .

Hypothesis: Such thinking helps many to do so , they can be able to make their own life .
```   

Example 4
```sh
Source:     Ihe Chineke ga - eme ụwa ọjọọ a ga - egosi nnọọ na ọ na - ekpe ikpe ziri ezi nakwa na ọ hụrụ ndị mmadụ n’anya . — Ọma 92 : 7 ; Ilu 2 : 21 , 22 .

Reference:  God ’ s action against this wicked world will perfectly reflect both his justice and his love. — Ps . 92 : 7 ; Prov . 2 : 21 , 22 .

Hypothesis: God ’ s will be done to the wicked world that he will show that he is justice and that he loves people . — Ps . 92 : 7 ; Proverbs 2 : 21 , 22 .
```

## RESULTS
- BLEU dev: 25.91
- BLEU test: 27.67

