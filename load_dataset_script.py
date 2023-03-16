"""
    The script has been modified using the following base script for translation:
    https://github.com/huggingface/datasets/blob/master/datasets/flores/flores.py

"""

import os
import collections
import glob

import datasets
from datasets import load_dataset
from datasets import load

_DATA_URL = "https://object.pouta.csc.fi/Tatoeba-Challenge/eng-epo.tar"

# Tuple that describes a single pair of files with matching translations.
# language_to_file is the map from language (2 letter string: example 'en')
# to the file path in the extracted directory.
TranslateData = collections.namedtuple("TranslateData", ["url", "language_to_file"])


class TatotebaConfig(datasets.BuilderConfig):
    """BuilderConfig for FLoRes."""

    def __init__(self, language_pair=(None, None), **kwargs):
        """BuilderConfig for FLoRes.

        Args:
            for the `datasets.features.text.TextEncoder` used for the features feature.
          language_pair: pair of languages that will be used for translation. Should
            contain 2-letter coded strings. First will be used at source and second
            as target in supervised mode. For example: ("se", "en").
          **kwargs: keyword arguments forwarded to super.
        """
        name = "%s%s" % (language_pair[0], language_pair[1])

        description = ("Translation dataset from %s to %s") % (
            language_pair[0],
            language_pair[1],
        )
        super(TatotebaConfig, self).__init__(
            name=name,
            description=description,
            version=datasets.Version("1.1.0", ""),
            **kwargs,
        )

        # Validate language pair.
        assert "en" in language_pair, (
            "Config language pair must contain `en`, got: %s",
            language_pair,
        )
        source, target = language_pair
        non_en = source if target == "en" else target
        assert non_en in ["epo", "si"], ("Invalid non-en language in pair: %s", non_en)

        self.language_pair = language_pair


class Tatoeba(datasets.GeneratorBasedBuilder):
    """Tatoeba machine translation dataset."""

    BUILDER_CONFIGS = [
        TatotebaConfig(
            language_pair=("en", "epo"),
        ),
    ]

    def _info(self):
        source, target = self.config.language_pair
        return datasets.DatasetInfo(
            features=datasets.Features(
                {
                    "translation": datasets.features.Translation(
                        languages=self.config.language_pair
                    )
                }
            ),
            supervised_keys=(source, target),
        )

    def _split_generators(self, dl_manager=None):

        # the dl_manager is mandatory argument but we do not need that since we are already doing are downloading
        # and preprocessing before hand and then pushing the data ahead

        path_tmpl = "data/"

        files = {}
        for split in ("train", "dev", "test"):
            files[split] = {
                "source_file": os.path.join(path_tmpl, split, f"{split}.src"),
                "target_file": os.path.join(path_tmpl, split, f"{split}.trg"),
                "files": glob.glob(os.path.join(path_tmpl, split, "*")),
            }

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN, gen_kwargs=files["train"]
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs=files["dev"]
            ),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs=files["test"]),
        ]

    def _generate_examples(self, files, source_file, target_file):
        """This function returns the examples in the raw (text) form."""
        source_sentences, target_sentences = (
            open(files[0]).read().split("\n"),
            open(files[1]).read().split("\n"),
        )

        assert len(target_sentences) == len(
            source_sentences
        ), "Sizes do not match: %d vs %d for %s vs %s." % (
            len(source_sentences),
            len(target_sentences),
            source_file,
            target_file,
        )

        source, target = self.config.language_pair
        for idx, (l1, l2) in enumerate(zip(source_sentences, target_sentences)):
            result = {"translation": {source: l1, target: l2}}
            # Make sure that both translations are non-empty.
            if all(result.values()):
                yield idx, result

if __name__ == "__main__":
    load_dataset("load_dataset_script.py")