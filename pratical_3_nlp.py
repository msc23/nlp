import nltk
from nltk.util import ngrams


n=3
Sentence="You will face many defeats in life,but never let it go"
trigrams = ngrams(Sentence.split(),n)


for item in trigrams:
   print(item)
