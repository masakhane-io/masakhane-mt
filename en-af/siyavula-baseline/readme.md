English-Afrikaans Translation of Siyavula Textbooks
===================================================

Data
----
The data used for this English-Afrikaans MT system was compiled from content
on the [Siyavula website](https://www.siyavula.com/read), specifically using
the Grade 5 and 6 science textbooks with a licence which allows adaptations,
[CC BY](https://creativecommons.org/licenses/by/3.0/).

If the data is further distributed or adapted, it needs to also be released
under the same [CC BY](https://creativecommons.org/licenses/by/3.0/) license,
with credit to Siyavula for the content and Herman Kamper for the data
compilation.

The compiled and pre-processed data can be downloaded from:
https://www.kamperh.com/data/siyavula_en_af.noweb.3.zip


Changes to model
----------------
I made very limited changes to the setup from the original example codebook,
apart from changing the batch sizes and some of the validation settings.


Example input-output sentences
------------------------------

Example 1:

    Source:     resources about water
    Reference:  hulpbronne oor water
    Hypothesis: bronne van water

Example 2:

    Source:     what does it mean to purify water ?
    Reference:  wat beteken dit om water te suiwer ?
    Hypothesis: wat beteken dit om water te suiwer ?

Example 3:

    Source:     it means to clean water; to remove pollutants from the water .
    Reference:  om water te suiwer beteken om besoedeling uit water te verwyder .
    Hypothesis: dit beteken om skoon te skoon waterbesoedeling uit die water te verwyder .

Example 4:

    Source:     what is clean water ?
    Reference:  wat is skoon water ?
    Hypothesis: wat is skoon ?

Example 5:

    Source:     try it out and see if this makes a difference .
    Reference:  probeer dit en kyk of dit 'n verskil maak .
    Hypothesis: probeer dit op en kyk as 'n verskil is .


Contributors
------------
- [Herman Kamper](http://www.kamperh.com/)
