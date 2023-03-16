This folder contains corrected (post-edited/pe-d) translations from Maskhane JoeyNMT models (https://github.com/masakhane-io/masakhane-mt/tree/master/benchmarks, June 2020).

There are two English sources that are translated into the African languages:
1. Covid survey: https://coronasurveys.org/
2. TED talks: the Multitarget TED Talks Task (http://www.cs.jhu.edu/~kevinduh/a/multitarget-tedtalks/) 

The files are named according to the source, the language, annotator id for multiple annoators, and sentence numbers for TED talks.
Example: "pe_yo_ted_1-40_81-120.tsv" - Yoruba translations of TED talks, sentences 1-40 and 81-120.

The files itself contain the source, translation, and human correction (post-edit) for selected source sentences, as well as per-sentence BLEU, ChrF and TER scores computed with sacrebleu (sentence_bleu) and pyTER, respectively. The metrics were computed before tokenization, so they slightly diverge from the numbers reported in the paper. To be more correct, translations and corrections need to get tokenized with Polyglot (https://polyglot.readthedocs.io/en/latest/Tokenization.html).

Authors of the corrected translations (Masakhane members):
- ddn_covid: Jamiil Toure ALI
- fon_covid: Jamiil Toure ALI
- ha_covid: Ricky Macharm & Wale Akinfaderin
- ha_ted: Wale Akinfaderin
- ig_covid: Chris Emezue & G.M.T Emezue
- ig_ted: Ignatius Ezeani
- luo_ted: Perez Ogayo
- pcm_covid: Orevaoghene Ahia
- pcm_ted: Kelechi Ogueji
- sn_covid: Blessing Sibanda
- sw_ted: Freshia Sackey
- yo_covid: Jamiil Toure ALI
- yo_ted: Mofetoluwa Adeyemi
 
