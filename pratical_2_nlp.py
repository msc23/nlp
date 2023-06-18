import nltk
from nltk.stem import PorterStemmer
# Initialize Python porter stemmer
ps = PorterStemmer()
# Example inflections to reduce
example_words = ["program","programming","programer","programs","programmed"]
# Perform stemming
print("{0:20}{1:20}".format("--Word--","--Stem--"))
for word in example_words:
  print ("{0:20}{1:20}".format(word, ps.stem(word)))
  
#########################################
import string
from nltk.tokenize import word_tokenize

example_sentence = "Python programmers often tend like programming in python because it's like english. We call people who program in python pythonistas."
# Remove punctuation
example_sentence_no_punct = example_sentence.translate(
    str.maketrans("", "", string.punctuation))
# Create tokens
word_tokens = word_tokenize(example_sentence_no_punct)
# Perform stemming
print("{0:20}{1:20}".format("--Word--", "--Stem--"))
for word in word_tokens:
    print("{0:20}{1:20}".format(word, ps.stem(word)))
