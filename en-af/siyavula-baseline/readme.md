English-Afrikaans Translation of Siyavula Textbooks
===================================================

Data
----
The data used for this English-Afrikaans MT system was compiled from content
on the [Siyavula website](https://www.siyavula.com/read), specifically using
the Grade 5 and 6 science textbooks with a licence which allows adaptations,
[CC BY](https://creativecommons.org/licenses/by/3.0/).

If the data is further distributed or adapted, it needs to also be released
under the [CC BY](https://creativecommons.org/licenses/by/3.0/) license, with
credit to Siyavula for the content and Herman Kamper for the data compilation.


Changes to model
----------------
I made very limited changes to the setup from the original example codebook,
apart from changing the batch sizes and some of the validation settings.


Example input-output sentences
------------------------------

Example 0:

    Source:     resources about water
    Reference:  hulpbronne oor water
    Hypothesis: bronne oor water

Example 1:

    Source:     what does it mean to purify water ?
    Reference:  wat beteken dit om water te suiwer ?
    Hypothesis: wat beteken dit om water te suiwer ?

Example 2:

    Source:     it means to clean water; to remove pollutants from the water .
    Reference:  om water te suiwer beteken om besoedeling uit water te
                verwyder .
    Hypothesis: dit beteken om skoon water te skoon water om die besoedelende
                stowwe te verwyder .

Example 3:

    Source:     what is clean water ?
    Reference:  wat is skoon water ?
    Hypothesis: wat is water skoon ?


Contributors
------------
- [Herman Kamper](http://www.kamperh.com/)
