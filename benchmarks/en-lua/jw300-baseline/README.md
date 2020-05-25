# English to Tshiluba

Author: Salomon KABONGO

## Data

	- The JW300 English- Tshiluba.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/open?id=11doYa-jfV9pwgqP9xQGbD2CYYQJ5ey9P)

## Analysis

Example 1
```sh
	Source: JESUS set a pattern for all Christians by praying to his Father : “ Let , not my will , but yours take place . ”
 	Reference: YEZU wakashila bena Kristo bonso tshilejilu tshia kulonda pakalombaye Tatuende ne : ‘ Bualu buenjibue bu muudi musue , kabuenjibu bu mundi musue . ’
 	Hypothesis: YEZU mmushile bena Kristo bonso tshilejilu tshimpe pa kusambila Tatuende ne : ‘ Kanusankishidi disua dianyi , kadi nuenze bu mundi musue . ’
```

Example 2
```sh
	Source: Because his brothers were jealous and hated him , they forced him to leave the land that legally belonged to him .
 	Reference: Bu muvua bana babu bamumvuile mukawu ne bamukine , bakamuenzeja bua kumbuka mu buloba buvua bumpianyi buende .
 	Hypothesis: Bu muvua bana babu ne mukawu ne bamukine , bakamusaka bua kumbuka mu buloba buvua bumusaka bua kumushiya .
```

Example 3
```sh
	Source: So that Moses would understand His ways , Jehovah made it clear that although he does not approve of sin , he is slow to anger .
 	Reference: Bua kujadika ne : Mose uvua mua kumvua bimpe njila Yende , Yehowa wakaleja patoke ne : nansha mudiye kayi wanyisha mpekatu , kêna ukuata tshiji lubilu .
 	Hypothesis: Nunku , Yehowa wakaleja patoke ne : nansha muvuaye kayi wanyisha mpekatu , kêna ukuata tshiji lubilu to .
```

Example 4
```sh
	Source: I am confident that they are in Jehovah’s memory awaiting the resurrection .
 	Reference: Ndi mutuishibue ne : Yehowa mmubalame mu meji bua kubabisha ku lufu .
 	Hypothesis: Ndi mushindike ne : badi mu tshivulukilu tshia Yehowa bua kuindila dibika dia bafue .
```

# Results
	- BLEU dev :  29.96
	- BLEU test : 42.52
