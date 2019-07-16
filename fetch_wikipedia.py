import wikipedia, random


def fetch_data(article_names):
  '''Fetching the data from given Wikipedia articles'''
  wikipedia_random_articles = wikipedia.random(2)
  wikipedia_random_articles.extend(article_names)
  wikipedia_random_articles
  print(wikipedia_random_articles)

  wikipedia_articles = []
  for wikipedia_article in wikipedia_random_articles:
    wikipedia_articles.append([wikipedia_article,
                               wikipedia.page(wikipedia_article).content])
  return wikipedia_articles
