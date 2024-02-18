# import spacy
# put two garden path sentences into a list: gardenpathSentences
# add three sentences to the list
# tokenize each sentence
# perform named entity recognition
# use spacy.explain to look up and print the meaning of entities you dont understand. 
# eg. print(spacy.explain("FAC"))
# finally, write a comment about two entities you looked up
# 1. what was the entity and its explanation you looked up?
# 2. did the entity make sense in terms of the word associated?

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

# Below, I have added my original idea- where I kept the list as a list for the duration of the task.
# This made it a lot more complicated for me. When I realised I could join all of the sentences of the list together,
# It seemed like a better and more simplified approach. 

# I have included my original workings below in case the task does require me to keep the list intact.
# It definitely made the presentation easier to read in the terminal- but I feel like the above captures 
# more accurately what we were asked to do in the task and teachings.
'''

import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["After the young Londoner had visited his parents prepared to celebrate their anniversary.", 
                       "While I was surfing the internet went down",
                       "While visiting the Louvre the guide discussed the Mona Lisa a famous portrait by Leonardo da Vinci that had a mysterious smile."] # trying to create my own
new_sentences = ["Mary gave the child a Band-Aid.", 
                 "That Jill is never here hurts.", 
                 "The cotton clothing is made of grows in Mississippi."]
gardenpathSentences.extend(new_sentences)

tokenized_sentences = [nlp(sentence) for sentence in gardenpathSentences] #tokenisation

for i, doc in enumerate(tokenized_sentences): #tokenisaiton is more complicated in this task due to the list.
    tokens = [token.text for token in doc]
    print(f"Sentence {i + 1} tokens: {tokens}")

for i, doc in enumerate(tokenized_sentences): # named entity recognition
    entities = [(ent.text, ent.label_, ent.label) for ent in doc.ents] 
    print(f"Sentence {i + 1} entities: {entities}")

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