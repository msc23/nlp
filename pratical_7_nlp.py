import spacy
from spacy import displacy
# python -m spacy download en_core_web_sm
NER = spacy.load("en_core_web_sm")
raw_text2="The Indian Space Reasearch Organisation or is the national space agency."
text1 = NER(raw_text2)
for word in text1.ents:
    print(word.text,word.label)
#use displayCy to visualize the dependencies
    displacy.render(text1,style='ent',jupyter=True)
