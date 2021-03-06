### WARNING - task_two.py is a work in progress.
### task_one.py does work as expected though

import pprint
import nltk
from nltk import text
from nltk.corpus import PlaintextCorpusReader
from nltk import FreqDist

CORPUS_ROOT = "/Users/mark/Desktop/nlp-nltk-workshop/corpora/selection_from_gutenberg/"


class MyCorpus(PlaintextCorpusReader):
  def __init__(self):
    super(MyCorpus, self).__init__(CORPUS_ROOT, '.*')

  def text(self):
    return self.words()

  def vocabulary(self):
    return set(self.text())

  def lexical_diversity(self):
    return len(self) / len(self.vocabulary())

  def histogram(self):
    return FreqDist(self.text())

  def tokens(self):
    return nltk.word_tokenize(str(self.text))

  def __len__(self):
    return len(self.text())


pp = pprint.PrettyPrinter(indent=2)

corpus = MyCorpus()
# print corpus
# print corpus.text().__class__
# print corpus.vocabulary()
# print corpus.histogram()
# pp.pprint(corpus.histogram())
#
# print str(corpus.text()).__class__
print corpus.tokens()