from bs4 import BeautifulSoup
import requests

#initial version of scraper
file = open('data.txt','a+')

#Beautiful Soup is a web scraper library
url = 'https://a856-cityrecord.nyc.gov/RequestDetail/20200219019'

#Steps of scraping
'''
Getting the URL
using the requests library to get the html from the url
using BeautifulSoup to parse the response
'''
#I'm passing in the url and waiting at least 5 seconds for the server to respond
response = requests.get(url,timeout=5)
# print(response.content)
content = BeautifulSoup(response.content,"html.parser")

'''
BeautifulSoup has different commands to select.
find & find_all are essentially the same find is only getting one


'''

yes = content.find('div', attrs={"class":"col-md-6"})
# print(yes)


#

yes1 = yes.find_all('div',attrs={"class":"form-group form-md-line-input"})

for elem in yes1:
    #This is a fail safe for if any elements are empty
    if len(elem.contents) > 1:
        label = elem.find('label').text
        val = elem.find('div').text.strip()
        file.write(f'{label}|{val}\n')


# file.write(yes1.text.strip())

file.close()
