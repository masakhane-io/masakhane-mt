# English to Arabic

Author: 
* Abdallah Bashir
* Amr Muhammad ALAMEEN Khalifa

## Data

* The JW300 English-Arabic (bin) dataset.
* The [TED-Multilingual-Parallel-Corpus](https://github.com/ajinkyakulkarni14/TED-Multilingual-Parallel-Corpus) English Arabic dataset	

## Test Data
the test data files for evaluating the model was not taken from the repo like the rest of the baselines but instead taken as a portion from the total merged datasets and in hte same size of the entries in test.en-any.en.  

## Model

- Default Masakhane Transformer translation model.
- [Link to google drive folder with models](https://drive.google.com/drive/folders/18P6HH9wavVpaR3UufoiUsTeqMnkvc1He)

## Analysis

The dataset requires more preprocessing to remove special characters and Scripture chapters/verse names & figures. Also it is very small, which is the primary limiting factor on being able to learn anything useful.

Example 1
```ar
	Source:     at the same time , the police gave free passage to busloads of mkalavishvili’s followers , who were bent on destroying the convention site .
	Reference:  وفي الوقت نفسه ‏ فتحت الشرطه الطريق لباصات اخري تنقل اتباع مكالاڤيشڤيلي الذين كانوا مصمين علي تدمير موقع المحفل ‏
	Hypothesis: وفي الوقت نفسه ‏ اعطي الشرطه مقطع مجاني لكثير من اتباع مالكالڤيليڤيليڤيل ‏ الذين كانوا منزعجين في تدمير موقع المحفل ‏
```

Example 2
```sh
	Source:      a big attraction was the man roland lithoman web - offset press that prints up to 90,000 magazines an hour .
	Reference:  وما لفت انتباه الزوار الي حد كبير هو مطبعه الوب اوفست المتطوره جدا ‏ man roland lithoman‏ ‏ التي يمكن ان تطبع ٠‏٩٠ مجله في الساعه ‏ 
	Hypothesis: كان جذب كبير هو الصحافه الرومانيه ليتوماان ‏ التي تطلق الي ٠‏٩٠ مجله في الساعه ‏
```

# Results

Tokenization | BLEU dev | BLEU test
--- | --- | ---
BPE | 15.45  | 9.28
