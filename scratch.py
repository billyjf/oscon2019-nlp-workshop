from pprint import pprint as pp
from common import *
# from frequency_distribution import *
# from stopwords import *
from pos_tagging import *
# from word_net import *

scrape_sentences = ["Open source is at the core of the software development. But today, you have to go deeper. You need to know how to implement new technologies like Kubernetes and TensorFlow. You need to work in a cloud environment that isn't always open source-friendly. To know how machine learning can make or break your code. Whether you're looking to understand where software development is headed, or want to dive into the key technologies that you need to build resilient, useful, innovative software, the O'Reilly Open Source Software Conference is where you'll find the answers you need."]
scrape_words = get_word_tokens(get_sent_tokens(scrape_sentences))

# pp(words)
# plot_freq_dist(scrape_words, num_words=30)

# Using stop words
# clean_sentences = get_clean_sentences(scrape_sentences, remove_digits=True)
# filtered_sample_words = filter_stopwords(get_word_tokens(clean_sentences))

# pp(filtered_sample_words)

# Using POS Tagging
scrape_tags = get_pos_tags(scrape_words)

# Using word net
# pp(get_wordnet_properties(scrape_words))

# joey_dialogue = ['they', 'are', 'warm', 'nice', 'people', 'with', 'big', 'hearts']
# get_wordnet_properties(joey_dialogue)

# Word sense disambiguation
# from nltk.wsd import lesk
# sent = ['I', 'went', 'to', 'the', 'bank', 'to', 'deposit', 'money', '.']
# print(lesk(sent, 'bank', 'n'))

# Stemming
# from stemming import *
# pp(get_stems(scrape_words))

# Lemmatization
# from wordnet import *
# pp(scrape_tags)
# pp(get_lemma(scrape_tags))

# Bag of Words
# from bag_of_words import *
# get_bag_of_words(scrape_sentences)

# Sentiment Analysis
# from sentiment_analysis import *
# reviews = ["I've watched this movie for the record, cause I had no particular expectations for it.",
#           "It's fine.",
#           "Not bad, not great either.",
#           "Captain Marvel is another fine Marvel adventure.",
#           "Captivating story and great visuals.",
#           "Confusing boring childish.",
#           "Strong Hero. Weak Film."]
#
# get_sentiment(reviews)

# Topic Modeling
from fetch_wikipedia import *
from wikipedia_cleaner import *

from gensim import corpora, models
import gensim

article_names = ['Music', 'Grace Hopper', 'Omaha', 'Data', 'Compiler']
wikipedia_articles = fetch_data(article_names)
wikipedia_articles
wikipedia_articles_clean = list(map(clean, wikipedia_articles))

article_contents = [article[1] for article in wikipedia_articles_clean]
dictionary = corpora.Dictionary(article_contents)
corpus = [dictionary.doc2bow(article) for article in
          article_contents[:-1]] # All except 'Compiler'

lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=6,
                                            id2word = dictionary,
                                            passes=100)

topic_results = lda_model.print_topics(num_topics=6, num_words=5)
topic_results

from word_cloud import *
display_wordcloud(lda_model)
