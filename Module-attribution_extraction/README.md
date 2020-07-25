## expected output
dictionary (called triple_tuple_dict)
contains *lists* of triples (tuples) as values plus a text source category
triples are ordered as (attribution source, attribution cue (verb), attribution content)

can be accessed by key name (key names are same as in metadate.csv with .conll extension stripped as in metadata.csv - File_ID)

To access the text_source category: 
> triple_tuple_dict[key][-1]

## Files required (in local folder ./data):

- text_source_category.csv (a list of the publishers and their respective categorisation (news, journal) - manually annotated
- metadata.tsv
- directory of allenNLP (semantic role label) .conll files (in folder '../vaccination-nlp/')

Atrribtuion relations verb list taken from: 
Pareti, S. (2015). Attribution: A Computational Approach. PhD thesis, University of Edinburgh.

## Run
execute ipynb
