import nltk
import numpy as np
import pandas as pd
import random
from sklearn .model_selection import train_test_split
import pprint,time
#download the treebank corpus from nltk
nltk.download('treebank')
#download the universal tagset from nltk
nltk.download('universal_tagset')
#reading the treebank tagged sentences
nltk_data=list(nltk.corpus.treebank.tagged_sents(tagset='universal'))
#print the first two sentences along with tags
print(nltk_data[:2])

#######################################

# import nltk
# nltk.download('treebank')
# nltk.download('brown')
# nltk.download('conll2000')
#load POS tagged corpara from nltk
treebank_corpus=nltk.corpus.treebank.tagged_sents(tagset='univrsal')
brown_corpus=nltk.corpus.brown.tagged_sents(tagset='universal')
conll_corpus=nltk.corpus.conll2000.tagged_sents(tagset='universal')
#merging the dataframes to create a master df
tagged_sentences=treebank_corpus+brown_corpus+conll_corpus
