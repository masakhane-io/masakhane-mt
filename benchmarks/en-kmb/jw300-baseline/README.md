# English to Kimbundu

Author: Daniel Whitenack

## Data

- JW300 en-kmb + `fast_align` based corpus fitering
- Test sets from the Masakhane common test sets:
    - [test.en-kmb.en](https://github.com/masakhane-io/masakhane/tree/master/jw300_utils/test/test.en-kmb.en)
    - [test.en-kmb.kmb](https://github.com/masakhane-io/masakhane/tree/master/jw300_utils/test/test.en-kmb.kmb)

## Model

```
    initializer: "xavier"
    bias_initializer: "zeros"
    init_gain: 1.0
    embed_initializer: "xavier"
    embed_init_gain: 1.0
    tied_embeddings: True
    tied_softmax: True
    encoder:
        type: "transformer"
        num_layers: 6
        num_heads: 8
        embeddings:
            embedding_dim: 512
            scale: True
            dropout: 0.
        # typically ff_size = 4 x hidden_size
        hidden_size: 512
        ff_size: 2048
        dropout: 0.3
    decoder:
        type: "transformer"
        num_layers: 6
        num_heads: 8
        embeddings:
            embedding_dim: 512
            scale: True
            dropout: 0.
        # typically ff_size = 4 x hidden_size
        hidden_size: 512
        ff_size: 2048
        dropout: 0.3
```

The pre-trained model can be found [here](https://drive.google.com/drive/folders/1-3nvjGFn1gpzpLgubOf7obhs_IJFWqj5?usp=sharing).

## Analysis

Example 1:
```
Source:     ( read philippians 2 : 5 - 8 . )
Reference:  ( tanga filipe 2 : 5 - 8 . )
Hypothesis: ( tanga filipe 2 : 5 - 8 . )
```

Example 2:
```
Source:     today , more than ever before , there are so many things that can distract us .
Reference:  lelu , kuene ima iavulu i tena ku tu landukisa , m’ukulu ndenge .
Hypothesis: lelu , m’ukulu , kuene ima iavulu i tena ku tu landukisa .
```

Example 3:
```
Source:     the apostle paul warned about what can happen if we please ourselves first .
Reference:  ( 1 nzuá 2 : 16 ) o poxolo phaulu ua tu dimuna ku ima i tena kubhita se tu suua ngó o ima i tua uabhela .
Hypothesis: o poxolo phaulu ua dimuna o ima i tu tena kubhanga , se tu dióndo dianga kusota o kitambuijilu kia poxolo .
```

Example 4:
```
Source:     what a privilege it is to live in these last days and to be part of jehovah’s incredible organization !
Reference:  tua tokala ku lembalala izuua ioso kuila , ujitu ua dikota ku tokala mu kilunga kia jihova mu ixi , mu izuua isukidila - ku !
Hypothesis: ujitu ua dikota ku kala mu izuua íii isukidila - ku , ni ku bhanga mbandu ku kilunga kia jihova mu kilunga kiê !
```

## Results

- BLEU train: 28.57
- BLEU dev: 28.81
- BLEU test: 32.76

