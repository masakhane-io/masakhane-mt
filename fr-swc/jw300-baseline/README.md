# French to Swahili Congo

Author: Murhabazi B. Espoir

## Background

Swahili Congo is quite different from the Swahili spoken in Kenyan.
It's spoken in the large part Eastern Congo, in Burundi and Rwanda.
Since many people have french as their official language I found that it may be useful to French to Swahili Congo

## Data

	- The JW300 French-Swahili Congo.

## Model

	- Default Masakhane Transformer translation model.
	- The model can be found [here](https://drive.google.com/ToBe Updated)

## Analysis

Example 1
```
    Source:     Avant de passer en cour martiale , j’ai été transféré dans un camp militaire à Héraclion , en Crète .
	Reference:  Kabla ya kupelekwa kortini , nilihamishiwa kwenye kambi ya kijeshi huko Iráklion , Krete .
    Hypothesis: Kabla ya kuingia katika makao ya kijeshi , nilihamishwa hadi kambi ya kijeshi huko Heraclion , Krete .
```

Example 2
```
	Source:     ● La médecine connaît un revirement funeste : certains médicaments “ miracles ” pourraient avoir perdu leur pouvoir .
	Reference:  Magonjwa ya kuambukiza yaliyokuwa yakiwaua mamilioni ya watu miaka mingi iliyopita kama vile , ukoma na kifua kikuu , yalidhibitiwa kwa dawa za kuua viini .
	Hypothesis: ● Mabadiliko makubwa ya kitiba yanatokea , yaani , huenda dawa fulani “ za kimuujiza ” zikapoteza uwezo wao .
```

Example 3
```
Source:     Lisons - ​ nous la Parole de Dieu chaque jour ?
Reference:  Je , tunapendezwa na sheria ya Mungu na kusoma Neno lake kila siku ?
Hypothesis: Je , tunasoma Neno la Mungu kila siku ?
```
## Results
	- BLEU dev :   26.73
	- BLEU test :  33.73
