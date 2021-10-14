# Setswana to English

Author: Samukelisiwe Ndlovu

## Data

	- The Autshumato dataset used for training in Ukuxhumana.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/drive/folders/1-579Bc4qTvboWG58cL6-WrpghVlKj00s?usp=sharing)

## Analysis

 	
Example #0
	Source:     Mme fa re tlhaloganya se metsi a a tshelang a tla re direlang sone , ga re kitla re bona fela 			botlhokwa jwa go a nwa mme gape re tla batla go a nwa .
	Reference:  And when we understand what the living waters can mean for us , not only will we see the need to 			partake of them but we will also want to drink them .
	Hypothesis: But if we understand what the water will serve , we will not see the value of drinking and also 			want to drink .
 Example #1
	Source:     Ke Boela Lovech
	Reference:  Coming Back to Lovech
	Hypothesis: I Way Lovech
 Example #2
	Source:     Mo lekgetlhong lengwe , ditsala dingwe tse di rategang tsa ga moaposetoloi Paulo di ile tsa 			tsamaya sekgala sa dikilometara tse di ka nnang 50 go tswa kwa Efeso go ya kwa Mileto go ya go 				kopana 			le ene .
	Reference:  On one occasion , dear friends of the apostle Paul traveled about 30 miles [ 50 km ] from Ephesus 			to Miletus to meet him .
	Hypothesis: On one occasion , some dear friends of the apostle Paul walked about 50 miles [ 50 km ] from 			Ephesus to Mileto meet him .
 Example #3
	Source:     “ Go ne ga isiwa manoko a kola , ga tlhajwa phelehu , ya apewa mme ya jewa ke botlhe ba ba neng ba 			le teng .
	Reference:  “ Kola nuts were offered , and a ram was slaughtered , boiled , and eaten by all those present .
	Hypothesis: “ It was made up , not the lion , but the sleep of all those who were present .
# Results
	- BLEU dev: 28.79
	- BLEU test: 35.15

	- Note: It is probably best to train this model for longer, as it timed out on Google Colab
	- Note: Will likely benefit from optimising the number of BPE codes
