# English to Nzema
The Nzema are an Akan people numbering about 328,700, of whom 262,000 live in southwestern Ghana and 66,700 live in the southeast of Côte d'Ivoire. In Ghana the Nzema area is divided into three electoral districts of Nzema East Municipal also referred to as Evalue Gwira, Ellembele District and Nzema West, which is also referred to as Jomoro District of Ghana. Their language is also known as Nzima (in Ghana) or Appolo (in the Ivory Coast).Wikepedia

Author: Salomey OSEI

## Data

	- The JW300 English- Nzema.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1WfTLClVQs-wBO7fveVM842-oDPHeT4Oh?usp=sharing)

## Analysis

Example 1
```sh
	Source:     What motivated Moses to live as he did ?
	Reference:  Duzu ati a Mosisi kpale kɛ ɔbabɔ ye ɛbɛla kɛmɔ yɛha nwolɛ edwɛkɛ la ɛ ?
	Hypothesis: Duzu a manle Mosisi dele nganeɛ wɔ mekɛ mɔɔ ɔyɛle ye zɔ la ɛ ?```

Example 2
```sh
	Source:     Writing Committee
 	Reference:  Mbulukuhɛlɛlɛ Kɔmatii
	Hypothesis: Bɛyɛ Ngakyelɛlilɛ
```

Example 3
```sh
	Source:     He was simply expressing a realistic view of how life in this imperfect world turns out .
	Reference:  Mɔɔ kɔ zo wɔ ewiade ɛtane ɛhye anu la anwo edwɛkɛ yɛɛ ɛnee ɔlɛka a .
	Hypothesis: Ɛnee ɔze kɛzi asetɛnla mɔɔ anu yɛ se la wɔ ewiade ɛhye anu .
```

Example 4
```sh
	Source:     From the start , Jacob was in love with his beautiful Rachel .
	Reference:  Mɔlebɛbo ne , ɛnee Gyekɔbo kulo Relahyɛle mɔɔ anwo yɛ ye fɛ la .
	Hypothesis: Mɔlebɛbo ne , Gyekɔbo nee Rachel nyianle ɛlɔlɛ kpole 
```

# Results
	- BLEU dev :  23.49 
	- BLEU test : 35.53

