from lxml import html
import requests

# Scraping data from a webpage element
page = requests.get('https://conferences.oreilly.com/oscon/oscon-or')
tree = html.fromstring(page.content)
conference_data = tree.xpath('//*[@id="reasons_row"]/div/p[1]/text()')
print(conference_data)