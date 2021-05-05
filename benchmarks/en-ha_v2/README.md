# English to Hausa

Author: Tunde Ajayi

## Data

	- The JW300 English-Hausa dataset.
	
## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model [here](https://drive.google.com/file/d/1spmmBVGc9riVK7H3f6GlUjh9oxMgShFf/view?usp=sharing)
	
## Analysis

Example 0
```sh
	Source: Her home is a pleasant and comfortable place for the entire family .
 	Reference: 14 : 1 ) Gidanta wuri ne na farin ciki da kwanciyar hankali ga dukan iyalin .
 	Hypothesis: A gidanta , gidanta wuri ne mai kyau kuma mai kyau ne ga dukan iyalin .
```

Example 1
```sh
	Source: Just as a surgeon might remove a cancerous tumor to save a patient’s life , God will “ cut off ” the wicked so that good people can truly enjoy life on earth .
 	Reference: Za a iya kwatanta wannan da yadda likitar fiɗa yakan yi wa marar lafiya aiki saboda ya cire inda cutar kansa take a jikin marar lafiya don ya sami lafiya . Hakan ma Allah zai cire ko “ datse ” miyagu don nagargarun mutane su ji daɗin zama a duniya .
 	Hypothesis: ( 1 : 1 ) A lokacin da haka , ya ce : “ Ku yi wa Jehobah , “ Ku yi wa Jehobah , amma ya yi wa Jehobah , amma ya yi wa Jehobah . ”
```

Example 2
```sh
	Source:     They experience peace in their lives by applying Bible principles . ​ — Isaiah 48 : 18 .
 	Reference:  ( Romawa 12 : 18 ) Kuma za su sami kwanciyar hankali don suna bin ƙa’idodin Littafi Mai Tsarki . — Ishaya 48 : 18 .
 	Hypothesis: ( 1 : 1 ) A lokacin da haka , muna da muka yi wa Jehobah , kuma muna da kuma muka yi wa Jehobah .
```

Example 3
```sh
	Source:     * By all means I shall have pity upon him . ”
 	Reference:  ( Aya ta 20 ) Jehobah yana begen sake ganin yaransa .
 	Hypothesis: ( 1 : 1 ) A lokacin da haka , ya yi wa Jehobah ya yi wa Jehobah .
```

# Results
	- BLEU train: 30.23
	- BLEU dev: 30.77
	- BLEU test: 32.31


