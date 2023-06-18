

import spacy
from spacy import displacy

# load the language model
# python -m spacy download en_core_web_sm
nlp = spacy.load("en_core_web_sm")

sentence = 'Deemed universities charge huge fees'

# nlp function returns an object with individual token information, linguistic features, and relationships
doc = nlp(sentence)

print("{:<15}|{:<8}|{:<15}|{:<20}".format('Token','Relation','Head','Children'))
print("-" * 70)

for token in doc:
    # print the token, dependency nature, head, and all dependencies of the token
    print("{:<15}|{:<8}|{:<15}|{:<20}"
          .format(str(token.text),str(token.dep_),str(token.head.text),str([child for child in token.children])))

# use displacy to visualize the dependencies
displacy.render(doc, style='dep', jupyter=True, options={'distance': 120})
