from WebScraper1 import WebScraper

url = 'https://a856-cityrecord.nyc.gov/RequestDetail/20200219019'
saveFilePath = 'data.txt'

scrape = WebScraper(url, saveFilePath)
scrape.run(timeout=5)
