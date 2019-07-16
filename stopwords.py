import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def filter_stopwords(words):
  '''Removing stopwords from given words'''
  filtered_words = [w for w in words if w not in stop_words]
  print('Filtered words:', filtered_words)
  return filtered_words