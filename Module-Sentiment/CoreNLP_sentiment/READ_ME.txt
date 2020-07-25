requires pycorenlp
requires stanfordnlpcore: https://stanfordnlp.github.io/CoreNLP/
requires running srever from within coreNLP folder (run from command line within the stanford-corenlp-full-2018-10-05)
(java -mx6g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -timeout 5000)

requires the attribution content - available in 294_triples_only.json file

produces json file of sentiment analysis - total number of positive/ negative/ neutral sentiments at the document level. 

