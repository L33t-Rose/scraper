from bs4 import BeautifulSoup
import requests


class WebScraper:
    def __init__(self, url='', saveFilePath=''):
        self.url = url
        self.saveFilePath = saveFilePath

    def setUrl(self,url):
        self.url = url

    def getUrl(self):
        return self.url

    def setSave(self,path):
        self.saveFilePath = path

    def getSave(self):
        return self.path

    def run(self, timeout=0):
        file = open(self.saveFilePath,'a+')

        res = requests.get(self.url,timeout=timeout)
        content = BeautifulSoup(res.content,"html.parser")

        title = content.find('span',attrs={"class":"caption-subject"}).text.strip()
        file.write(f'{title}\n')

        c = content.find_all('div',attrs={"class":"col-md-6"})

        for cols in c:

            yes = cols.find_all('div',attrs={"class":"form-group form-md-line-input"})
            for elem in yes:
                if len(elem.contents)>1:
                    label = elem.find('label').text
                    val = elem.find('div').text.strip()

                    file.write(f'{label}|{val}\n')
            file.write('\n')

        file.close()