Workshop Content
================

All slides - http://bengfort.com/presentations/discourses-in-language-processing/
Github - https://github.com/bbengfort

Introduction
------------
- http://bengfort.com/presentations/discourses-in-language-processing/introduction/
- NLP as a subset of AI
- NLTK is one of many NLP suites of libraries available
  - great because it's open source (not a black box) and source can be easily be browsed (unlike many Java jars)
- Quick Python review


A 10,000 foot view of NLP and NLTK
----------------------------------
- http://bengfort.com/presentations/discourses-in-language-processing/skyview/
- google has been successful because they have had a huge training set from people clicking on the right 'answer'
- what is required?
  1. Domain knowledge
  2. A corpus in the domain
- the NLP pipleline: http://bengfort.com/presentations/discourses-in-language-processing/img/skyview/pipeline.png
  - today, we are ignoring the first two columns
  - morphology: the study of the forms of things, words in particular:
    - orthographic rules: puppy -> puppies
    - morphological rules: goose -> geese or fish
    - parsing task: stemming (lemmatization) and tokenization
      - tokens = symbols of language
      - words = tokens with meaning
      - stem = what you would look up in the dictionary
  - syntax = the study of the rules for formation of sentences
    - a sentence diagram: http://bengfort.com/presentations/discourses-in-language-processing/img/skyview/parse.png
      - hierarchical and ordered
      - S = sentence, NP, NP = noun phrase, VP = verb phrase
  - semantics = the study of meaning
- Leveraging NLTK (https://github.com/nltk/nltk)
  - "NLP is perfect for MapReduce" (Hadoop)
  - major packages:
    - Utilities:
      - probability (Frequency and Conditional Distributions)
      - text, data, grammar, and corpus
      - tree (An impressive tree data structure and subclasses)
      - draw (Visualizations in Tkinter)
    - Language Processing
      - tokenize, stem (Morphological Processing, Segmentation)
      - collocations, models (NGram Analysis)
      - tag, chunk (Tagging and named entity Recognition)
      - parse (Syntactic Parsing)
      - sem (Semantic Analyses)
      - more: classification, clustering

Organizing text - The management of large bodies of natural language - copora
-----------------------------------------------------------------------------
- http://bengfort.com/presentations/discourses-in-language-processing/task_one/
-

My own thoughts
===============
- things to look into
  - what other projects like http://overview.ap.org/ exist?
  - http://www.antlr.org/ - ANother Tool for Language Recognition
  - NLTK being "Production ready analytics with Numpy or Pandas"
  - hadoop streaming w/ NLTK