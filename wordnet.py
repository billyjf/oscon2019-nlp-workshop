import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')


def get_wordnet_properties(words):
  '''Returns definition, synonyms and antonyms of words'''
  for word in words:
    synonyms = []
    antonyms = []
    #         hyponyms = []
    #         hypernyms = []
    definitions = []
    for syn in wordnet.synsets(word):
      for lm in syn.lemmas():
        synonyms.append(lm.name())
        if lm.antonyms():
          antonyms.append(lm.antonyms()[0].name())
    #             hyponyms.append(syn.hyponyms())
    #             hypernyms.append(syn.hypernyms())
    #             definitions.append(syn.definition())

    print(word)
    print('Synonyms:', synonyms, '\nAntonyms:', antonyms, '\n')
#         print('Definition:', definitions, '\n')

def get_lemma(word_tags):
  '''Reduce the words to their base word (lemma) by using a lexicon'''
  wordnet_lemmatizer = WordNetLemmatizer()
  lemma = []
  for element in word_tags:
    word = element[0][0]
    pos = element[0][1]
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,  # Mapping NLTK POS tags to WordNet POS tags
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    wordnet_pos = tag_dict.get(tag, wordnet.NOUN)
    lemma.append(wordnet_lemmatizer.lemmatize(word, wordnet_pos))

    return lemma
