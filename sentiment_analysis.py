import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')


def get_sentiment(data):
    '''Get sentiment of sentences using VADER algorithm'''
    scorer = SentimentIntensityAnalyzer()
    for sentence in data:
        print(sentence)
        ss = scorer.polarity_scores(sentence)
        for k in ss:
            print('{0}: {1}, ' .format(k, ss[k]), end='')
        print()
