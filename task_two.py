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

  def generate_text(cfdist, start, num=15):
    for i in xrange(num):
      print start,
      start = cfdist[start].max()

  def __len__(self):
    return len(self.text())


pp = pprint.PrettyPrinter(indent=2)

corpus = MyCorpus()
# print corpus
# print corpus.text()
# print corpus.vocabulary()
print corpus.histogram()
pp.pprint(corpus.histogram())
