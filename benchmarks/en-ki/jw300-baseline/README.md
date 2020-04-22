# English to Kikuyu

Author: Kathleen Siminyu

## Data

	- The JW300 English-Kikuyu dataset.

## Model

	- Default Masakhane Transformer translation model.
	- Link to google drive folder with model(https://drive.google.com/open?id=1cb-pp80LaxaOKDFziRUXxtUn6oGIRbMm)

## Analysis

Example 1
```sh
	Source:     He enjoyed special intimacy with Jehovah , who enabled him to display “ awesome power ” as he led the Israelites to the Promised Land . ​ — Deut .
 	Reference:  Aarĩ na ũkuruhanu wa hakuhĩ na Jehova , na nĩ aamũheire ũhoti wa gwĩka “ maũndũ manene ma kũguoyohania ” rĩrĩa aatongoragia Aisiraeli mathiĩ Bũrũri wa Kĩĩranĩro . — Gũcok .
 	Hypothesis: Nĩ aakenagĩra mũno gũkorũo arĩ mwĩhokeku harĩ Jehova , ũrĩa wamũteithirie kuonania “ hinya ” ũrĩa aaheete Aisiraeli nĩguo maatũme Bũrũri wa Kĩĩranĩro . — Gũcok .
```

Example 2
```sh
	Source:     Researchers at the University of Copenhagen tracked almost 10,000 middle - aged people over an 11 - year period and found that participants who frequently argued with someone close to them were far more likely to die prematurely than those who seldom had conflicts .
 	Reference:  Athuthuria yunivasĩtĩ - inĩ ya Copenhagen , nĩ maathuthuririe andũ hakuhĩ 10,000 a mĩaka ĩyo kwa ihinda rĩa mĩaka 11 na makĩona atĩ arĩa maakararanagia na mũndũ wa famĩlĩ kaingĩ , haakoragwo na ũhotekeku mũnene atĩ megũkua tene gũkĩra arĩa mataakoragwo na ngarari kaingĩ .
 	Hypothesis: Athuthuria a maũndũ marĩa meekirũo nĩ andũ 10,000 arĩa maikaraga Amerika ( US ) nĩ meethagathagathagĩte mũno nĩ ũndũ wa andũ 10,000 arĩa maikaraga mĩaka 11 na nĩ moonire atĩ andũ arĩa mahoyaga mahoyaga kaingĩ nĩ maakuĩte .
```

Example 3
```sh
	Source:     HISTORY : ATHEIST
 	Reference:  HISTORĨ : EETĨKĨTIE GŨTIRĨ NGAI
 	Hypothesis: HISTORĨ : ATHITHIO
```

# Results
	- BLEU dev: 23.83
	- BLEU test: 36.06

