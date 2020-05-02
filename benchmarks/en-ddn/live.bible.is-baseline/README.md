# English to Dendi

Author: Jamiil Toure Ali

## Data

	- Live.bible.is English-Dendi dataset.

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/file/d/10gRY0Z-awPLJRsCYhfuRvn1RsDWg7ifH/view?usp=sharing)

## Analysis

Example 1

````sh
        Source:     I thank him that enabled me, even Christ Jesus our Lord, for that he counted me faithful, appointing me to his service;
        Reference:  A go sɑɑbu i Kpe Yesu Mɛsiyɑ sɛ, ngɑ kɑ ɑ̀ nɑ ɑ no gɑɑbi. A gɑ kɑ ɑ̀ sɑɑbu domi ɑ̀ nɑ ɑ lɑsɑbu nɑɑnekpɛ kɑ ɑ dɑm ngɑ gbei kunɑ.
        Hypothesis: A go kɑ ɑ hɔngɑndi kɑ Yesu Mɛsiyɑ nɑ ɑ no ngɑ suuji sɑbu sɛ. À go kɑ ɑ cɛbɛ no tɑlikɑ yom sɛ kɑ ǹ ci ɑ sɛ hinɑbunutɛrɛ hɛ kɑ ɑ gundɑ ɑ sɛ ndɑ.
````
Example 2

````sh
        Source:     Now lettest thou thy servant depart, Lord, According to thy word, in peace;
        Reference:  Mɑɑsɑnkulu Kpe, n mɑ tu n bɑnyɑ mɑ kpei ndɑ bɑɑni zɑngɑ n Sendɑ cii.
        Hypothesis: A nyɑizei, n mɑ wɔne cii ɑ sɛ, Kpei, Setɑm. N mɑ n bine yeenɑndi kɑ n bine yom kɔnkɔm.
````

Example 3
````sh
        Source:     if so be that God is one, and he shall justify the circumcision by faith, and the uncircumcision through faith.
        Reference:  Ikpɛ fɔlɔnku yɑ gɑ bɑnguize yom cɛɑndi susu nɑɑne gɑɑ. À go zɑm kɑ dɑmbɑnguize yom mo cɛɑndi susu nɑɑne gɑɑ.
        Hypothesis: Zɑngɑ yɑ no Ikpɛ go hungu, ngɑ kɑ ɑ̀ gɑ cɛɑndi susu. À gɑ bɔrɔ cɛɑndi susu. À gɑ nɑɑne nɑɑne gɑɑ nɑɑne gɑɑ, nɑɑne kɑ ɑ̀ gɑ nɑɑne cini.
````

Example 4
````sh
        Source:     And from that city many of the Samaritans believed on him because of the word of the woman, who testified, He told me all things that ever I did.
        Reference:  Wɑngɑrɑ ngɑ di, Sɑmɑriɑncɛ boobo nɑɑne Yesu gɑɑ weibɔrɔ di sendɑ sɑbu sɛ. Weibɔrɔ di tɛ sɛdɑ kɑ cii: Hɛ kulu kɑ ɑ jinɑ kɑ tɛ, ɑ̀ nɑ ɑ̀ cii ɑ sɛ.
        Hypothesis: Zɑ Sɑmɑri lɑɑbu bɔrɔ boobo nɑɑne ɑ̀ gɑɑ kɑ Yesu mɑɑ sendɑ sɑbu sɛ. À nɑɑne ɑ̀ gɑɑ no ɑ̀ cii bɔrɔ kulu kɑ ɑ̀ sɛ ɑ go sendi hɛ kulu kɑ ɑ̀ sɛ ndɑ hɛ kulu kɑ ɑ̀ ci lɑɑli li boobo.
````

## Results

      - BLEU train : 14.18
      - BLEU dev : 13.32
      - BLEU test : 22.30
