import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag,word_tokenize,RegexpParser
#Example text
sample_text="The little yellow dog barked at the cat"
#Find all parts of speech in above sentence
tagged=pos_tag(word_tokenize(sample_text))
#Extract all parts of speech from any text
chunker =RegexpParser("""             NP:{<DT>?<JJ>*<NN>}  
                                      P:{<IN>}
                                      V:{<V.*>}
                                      PP:{<P> <NP>}
                                      VP:{<V> <NP|PP>*}
                     """)
#print all parts of speech in above sentence.
output = chunker.parse(tagged)
print("After Extracting\n",output)
output.draw()
