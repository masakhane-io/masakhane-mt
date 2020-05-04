# French to Lingala

Author: Murhabazi B. Espoir

## Data

	- The JW300 French - Lingala.

## Model

	- Default Masakhane Transformer translation model.
	- The model can be found <a href="http://34.66.168.159/french_lingala_espoir/models/frln_transformer/340000.ckpt">Here</a>

## Analysis

Example 1
```ln
   	Source:     Peut - être comprenez - ​ vous ses proches .
	Reference:  Ntango mosusu okoki kozala na likanisi ndenge moko na bato ya libota na ye .
 	Hypothesis: Mbala mosusu oyebi bandeko na ye .
```

Example 2
```ln
	Source:     L’endurance face à de telles épreuves est particulièrement précieuse pour Jéhovah .
	Reference:  Koyika mpiko liboso ya komekama wana ezali na motuya mingi na miso ya Yehova .
	Hypothesis: Koyika mpiko na mikakatano ya ndenge wana ezali na ntina mingi mpo na Yehova .
```

Example 3
```ln
	Source:     Résumé : Éliya apporte la preuve que Jéhovah est supérieur à Baal .
	Reference:  Na mokuse : Eliya amonisi ete Yehova aleki Baala .
	Hypothesis: Na mokuse : Eliya amonisaki ete Yehova aleki Baala .
```


Example 4
```ln
	Source:     Dans l’ensemble , David s’est montré un homme de foi .
	Reference:  Mokonzi Davidi azalaki moto ya sembo , mpe Yehova azalaki kolinga ye mingi .
	Hypothesis: Davidi azalaki moto ya kondima .
```

Example 5
```ln
	Source:     J’ai donc décidé de me confesser et , pour pénitence suprême , de mettre fin à mes jours .
	Reference:  Lokola namonaki ete nakokoka te kofuta mbongo yango , nakómaki kaka mawamawa .
	Hypothesis: Yango wana , nazwaki ekateli ya koyambola ngai , mpe mpo na nini nasengeli kotika mikolo na ngai .
```

# Results
	- BLEU dev :   26.41
	- BLEU test :  39.81
