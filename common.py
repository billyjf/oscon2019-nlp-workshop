from nltk.tokenize import sent_tokenize, word_tokenize
import re

def get_sent_tokens(data):
  """Sentence tokenization"""
  sentences = []
  for sent in data:
    sentences.extend(sent_tokenize(sent))
  print('Sentence tokens:', sentences)
  return sentences

def get_word_tokens(sentences):
    '''Word tokenization'''
    words = []
    for sent in sentences:
      words.extend(word_tokenize(sent))
    print('Word tokens:', words)
    return (words)


def get_clean_sentences(sentences, remove_digits=False):
  '''Cleaning sentences by removing special characters and optionally digits'''
  clean_sentences = []
  for sent in sentences:
    pattern = r'[^a-zA-Z0-9\s]' if not remove_digits else r'[^a-zA-Z\s]'
    clean_text = re.sub(pattern, '', sent)
    clean_text = clean_text.lower()
    clean_sentences.append(clean_text)
  print('Clean sentences:', clean_sentences)
  return clean_sentences
