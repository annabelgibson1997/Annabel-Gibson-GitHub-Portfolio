'''import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("this is a test sentence")
print([(w.text, w.pos_) for w in doc])



import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["After the young Londoner had visited his parents prepared to celebrate their anniversary.", 
                       "While I was surfing the internet went down",
                       "While visiting the Louvre the guide discussed the Mona Lisa a famous portrait by Leonardo da Vinci that had a mysterious smile."] # trying to create my own
new_sentences = ["Mary gave the child a Band-Aid.", 
                 "That Jill is never here hurts.", 
                 "The cotton clothing is made of grows in Mississippi."]
gardenpathSentences.extend(new_sentences)

joined_string = "\n".join(gardenpathSentences) # joining the list to make it a string.
print(joined_string) 

doc = nlp(joined_string)
print([token.orth_ for token in doc if not token.is_punct | token.is_space]) #tokenisation

print([(i, i.label_, i.label) for i in doc.ents]) #named entity recognition

entity_fac = spacy.explain("GPE") # using spacy.explain
print(f"GPE: {entity_fac}")
# GPE: Countries, cities, states. This makes sense as it refers to Mississippi, a state.

entity_fac = spacy.explain("PRODUCT") 
print(f"PRODUCT: {entity_fac}")
# PRODUCT: Objects, vehicles, foods, etc. (not services)
# In the context of this sentence, defining Mona Lisa as an object is correct.
# This is an interesting case because that could have been recognised as a PERSON.
# I think this is due to the DETERMINER, 'the' used before 'Mona Lisa'.
'''
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("dog")
word3 = nlp("banana")

print("The similarity score between cat and dog is: " + str(word1.similarity(word2)))