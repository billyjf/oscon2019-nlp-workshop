import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

nltk.download('stopwords')


def clean(article):
    '''Cleaning the article contents and getting the word stems'''
    title, document = article
    tokens = RegexpTokenizer(r'\w+').tokenize(document.lower())
    tokens_clean = [token for token in tokens if token not in
                    stopwords.words('english')]
    tokens_stemmed = [PorterStemmer().stem(token) for token
                      in tokens_clean]
    return (title, tokens_stemmed)
