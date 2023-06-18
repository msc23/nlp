#word Tokenization
from nltk.tokenize import word_tokenize
str=input("Enter Info/Data for tokenization:")
print(word_tokenize(str))
print("Number of tokens for word:",len(str))


#Sentence Tokenization
from nltk.tokenize import sent_tokenize
str1=sent_tokenize(str)
print(str1)
print("Number of tokens for sentence:",len(str1))
