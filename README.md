 # Masakhane - A living machine translation project for Africans, by Africans


![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://join.slack.com/t/masakhane-nlp/shared_invite/enQtODM3ODA3ODE0ODIwLTAyYzg3M2E3Nzg4Y2I3NzgxNDg4MmNlZDE4OTBjMzBjMjg4NTcxMWZlYTg3ZDljMTU4M2FjOTk3MDVjOWM2NGM)

<div align="center">
<img src="https://pbs.twimg.com/profile_images/1255858628986384384/d7Lk9I-w_400x400.jpg" >
</div>

**MASAKHANE** is an research effort for machine translation for African languages that is OPEN SOURCE, CONTINENT-WIDE, DISTRIBUTED and ONLINE. This GitHub repository houses the data, code, results and research for building open baseline translation results for African languages.

Website: [masakhane.io](https://masakhane.io)

## Goals

- **For Africa**: To build and facilitate a community of NLP researchers, connect and grow it, spurring and sharing further research, build helpful tools for applications in government, medicine, science and education, to enable language preservation and increase its global visibility and relevance. 

- **For NLP Research**: To build data sets and tools to facilitate NLP research on African languages, and to pose new research problems to enrich the NLP research landscape.

- **For the global researchers community**: To discover best practices for distributed research, to be applied by other emerging research communities.


## Hall of Fame for our Contributors
[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/0)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/0)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/1)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/1)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/2)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/2)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/3)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/3)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/4)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/4)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/5)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/5)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/6)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/6)[![](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/images/7)](https://sourcerer.io/fame/jaderabbit/masakhane-io/masakhane/links/7)

## Progress

- Look at our submitted benchmarks [here](https://github.com/masakhane-io/masakhane/blob/master/language_pairs.md)! Can't see your language? Please submit a benchmark!
- Check out our [paper](https://arxiv.org/pdf/2003.11529) to be published at AfricaNLP Workshop @ ICLR 2020
- Check out papers written by our participants [here](https://github.com/masakhane-io/masakhane/blob/master/publications.md)
- Find our more about our [current initiatives](https://github.com/masakhane-io/masakhane/blob/master/initiatives.md)
- Read our [weekly meeting notes](https://github.com/masakhane-io/masakhane/tree/master/meetingsummaries)

## How can I contribute?

There are many ways to contribute to **MASAKHANE**.

1. Contribute a trained model and related code for your language
2. Contribute analysis of data/models for any African languages. You do not need any technical experience for this! If you're a linguist, we can pair you up with a machine translation practitioner and you can help contribute analysis
3. Contribute to documentation or the base "notebook" that will improve the experience of others
4. Provide advice or help tune models for their languages and datasets
5. Help administrate! Working with so many researchers can be quite a challenge!
6. Help with infrastructure and compute! Do you have spare compute to donate? Let us know! We're always looking for more!
7. Help document our discussions, progress. This is VERY much needed
8. Join our weekly meetings, provide advice or ideas
9. Provide expertise 

Want more details? Check out our [current initiatives](https://github.com/masakhane-io/masakhane/blob/master/initiatives.md)

## How do I join?

1. Join our [Slack](https://join.slack.com/t/masakhane-nlp/shared_invite/enQtODM3ODA3ODE0ODIwLTAyYzg3M2E3Nzg4Y2I3NzgxNDg4MmNlZDE4OTBjMzBjMjg4NTcxMWZlYTg3ZDljMTU4M2FjOTk3MDVjOWM2NGM)
2. Request to join our [Google Group](https://groups.google.com/forum/#!forum/masakhane-mt)

3. This is so we can feature you on our webpage [masakhane.io](https://masakhane.io). Please email the following to masakhanetranslation@gmail.com:
    - Your Full Name
    - A preferred social media link
    - The language(s) you'll be working on (or your general relevant specialty - if you're an expert at machine translation and - would like to boost the community through that)
    - A picture
    - Your affiliation and role.

*Please be patient with a response via our email address, we're very behind on our administration, in the time of COVID-19.*


## Building your first machine translation model

Typically, if you have some programming experience, we encourage you to start on your journey with Masakhane, by building a baseline for your language. 
**Feeling nervous to submit or not sure where to start? Please join our weekly meeting and we will pair you with a mentor!**

### 1. Have a look at the example code
We have an [example colab notebook](https://github.com/jaderabbit/masakhane/blob/master/starter_notebook.ipynb) which trains a model for English-to-Zulu translation. Open it in [Google Colab](google colab) - you can select it by going to the GitHub section when opening a new project.


### 2. Finding data for my language?!

This is a huge challenge, but luckily we have a place to start! At ACL 2019, [this](https://www.aclweb.org/anthology/P19-1310/) paper was published. The short story? Turns out the Jehovah's Witness community has been translating many many documents and not all of them are religious. And their language representation is DIVERSE.

Check out this spreadsheet [HERE](https://docs.google.com/spreadsheets/d/1p_HpKkrAlRDte04pgStsxaN8IJ4I0GgidVGIE_6VtMw/edit?usp=sharing) to see if your language is featured, then go to Opus to find the links to the data:  http://opus.nlpl.eu/JW300.php

We also provide a script for easy downloading and BPE-preprocessing of JW300 data from OPUS: `jw300_utils/get_jw300.py`. It requires the installation of the [opustools-pkg Python package](https://pypi.org/project/opustools-pkg/). Example: For dowloading and pre-processing the Acholi (ach) and the Nyaneka (nyk) portions of JW300, call the script like this:
`python get_jw300.py ach nyk --output_dir jw300`

#### Can't find your language in the JW300 dataset?

Then we still have some options! Our community has been searching wide and far! Join our slack and google group to discuss a way forward! 

### 3. Run the notebook!

Your next step is to use the JW300 dataset in the colab notebook and run it. Most pieces of advice are within the notebook itself. We are constantly improving that notebook and are open to any recommendations. Struggled to get going? Then let's work together to build a notebook that's easier to use! Create a github issue or email us!

### 4. It's done! I have results! Now what?

Amazing! You're created your first baseline. Now we need to get the code and data and results into this github repository

In order for us to consider your result submission official, we need a couple of things:

1. The notebook that will run the code. The notebook MUST run on on someone else account and the data that it uses should be publically accessible (i.e. if I download the notebook and run it, it must work - so shouldn't be using any private files). If you're wondering how to do this, don't fear! Drop us a line and we will work together to make sure the submission is all good! :)

2. The test sets - in order to replicate this and test against your results, we need saved test sets uploaded separately.

3. A README.md that describes the (a) the data used - esp important if it's a combination of sources (b) any interesting changes to the model (c) maybe some analysis of some sentences of the final model

4. The model itself. This can be in the form of a google drive or dropbox link. We will be finding a home for our trained models soon.
For models to be used for transfer learning, further trained, or deployed, you need to provide:
    1. a checkpoint with the parameters (`.ckpt` file),
    2. the source and target vocabulary (`src_vocab.txt`, `trg_vocab.txt`),
    3. the configuration file (`config.yaml`),
    4. and if applicable: the BPE codes or scripts for your pre-processing pipeline.
Joey NMT saves the first three in the model directory.

5. The results - the train, dev, and test set BLEU score

We will be further expanding our analysis techniques so it's super important we have a copy of the model and test sets now so we don't need to rerun the training just to do the analysis

Once you have all of the above, please create a pull request into the repository. See guidelines [here](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork).

#### Structure of my PR:

Also see this as an example for the structure of your contribution

Structure:
 ```
/benchmarks
  /<src-lang>-<tgt-lang>
    /<technique> -- this could be "jw300-baseline" or "fine-tuned-baseline" or "nig-newspaper-dataset"
      - notebook.ipynb
      - README.md
      - test.src
      - test.tgt
      - results.txt
      - src_vocab.txt
      - trg_vocab.txt
      - src.bpe
      - [trg.bpe if the bpe model is not joint with src]
      - config.yaml
      - any other files, if you have any
```

Example:
```
/benchmarks
  /en-xh
    /xhnavy-data-baseline
      - notebook.ipynb
      - README.md
      - test.xh
      - test.en
      - results.txt
      - src_vocab.txt
      - trg_vocab.txt
      - en-xh.4000.bpe
      - config.yaml
      - preprocessing.py
```

Here is a link to a pull request that has the relevant things.

**Feeling nervous about contributing your first pull request or unsure how to proceed? Please don't feel discouraged! Drop us an email or a slack message and we will work together to get your contribution in ship shape!**

### 5. I've got a baseline. What do I do to improve it?

Cool! So there are many ways to improve results. We've highlighed a few of these in [this document](MT4LRL.md). Got other ideas? Drop us a line or submit a PR!

# Code of Conduct

See [Code of Conduct](https://github.com/jaderabbit/masakhane/blob/master/CODE_OF_CONDUCT.md)
