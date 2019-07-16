import matplotlib
from nltk.probability import FreqDist
matplotlib.use('TkAgg')

def plot_freq_dist(words, num_words = 20):
    '''Frequency distribution'''
    fdist = FreqDist(words)
    fdist.plot(num_words, cumulative=False)