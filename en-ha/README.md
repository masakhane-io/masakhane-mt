# Hausa-NMT: Empirical Study of Neural Machine translation for English-Hausa-English

This is an ongoing work on Neural Machine Translation for English-Hausa. According to [Sebastian Ruder](https://ruder.io/4-biggest-open-problems-in-nlp/), one of the biggest open problems for NLP is NMT for low-resource languages. NMT suffers a language diversity problem and growing up in a multi-lingual community with about 300 languages and thousands of dialects, I decided to work on NMT for the second largest Afro-Asiatic language after Arabic — Hausa Language. Hausa is also the third largest trade language across a larger swathe of West Africa after English and French. I have started working on this and the results are pretty good so far. I’m currently collaborating with scholars from the [Niger-Volta Language Technologies Institute](https://github.com/Niger-Volta-LTI) and working with some starter notebooks created by the [Masakhane](https://www.masakhane.io) community.

# First Run (Test BLEU: 34.22)

### Dataset used for first trial run

- English - Hause Parallel Corpus from JW300 Dataset on Opus
- 237,065 parallel sentences
- Reduced to 212,320 after dropping duplicates
- Split into train (168,856), test (41,464) and dev (1,000) set

### Pre-Processing and Training

- Byte Pair Encoding (BPE) was used to tokenize and “boost” performance
- Trained using the Transformer Encoder-Decoder architecture on [JoeyNMT](https://joeynmt.readthedocs.io/en/latest/)
- 30 epochs
- Plateau scheduling
- Learning rate: 0.0003
- 4096 batch size
- Xavier initializer (same used for embedding layer)
- For transformer encoder and decoder: 6 layers, 4 heads, 256 embedding dim, 0.2 embedding dropout rate, 0.3 dropout rate, 256 hidden layer size

### Results: Validation Loss and Bleu Score

![Validation Loss and Bleu Score for Dev Test from first run](https://github.com/WalePhenomenon/Hausa-NMT/blob/master/Images_Results/Dev_Test_1.png)

For this first run, I had a bleu/validation test score of 34.22 and  a Test Bleu of 30.12. See samples of the translations below.

![Sample Translation](https://github.com/WalePhenomenon/Hausa-NMT/blob/master/Images_Results/Dev_Test_1_Examples.png)


## Second Run (Test BLEU: 41.11)

- Trained on more datasets
- Added Tanzil (Quran), Wikimedia and Tatoeba parallel corpus to it.
- Total number of en-ha parallel sentences: 351,024
- Training set: 98%, dev: 1000, test: 2%
- Used BPE and the same architecture

### Results on Dev Test for Second Run

![Validation Loss and Bleu Score for Dev Test from second run](https://github.com/WalePhenomenon/Hausa-NMT/blob/master/Images_Results/Dev_Test_2.png)

For this first run, I had a bleu/validation test score of 38.26 and  a Test Bleu of 41.11. See samples of the translations below.

Finally, a Test Bleu of 41.11 is pretty good. I have some other ideas and experiment I'm currently working on like using a Linguistically Motivated Vocabulary Reduction (LMVR) vs BPE. Some of my thoughts can be viewed in this [slide deck](https://docs.google.com/presentation/d/1UF0lED6jCIQdKwxY7XErvmq5Nr57MT1lU5pLHSRUhiI/edit?usp=sharing) and I update from time to time. You can also reach out to me via email: waleakinfaderin@gmail.com.





