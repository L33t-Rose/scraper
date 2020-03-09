from bs4 import BeautifulSoup
import requests
from os import path
import json


class WebScraper:
    '''
    WebScraper is a class that is a skin of Beautiful Soup. It's meant to combine all of it features into multiple methods.
    When you init the function you can set the url, the file you want to save your data to.
    In additon, I just added the auth paramenter to add authentication for websites that require authentitcation
    '''
    def __init__(self, url='', saveFilePath='', auth=('','')):
        self.url = url
        self.saveFilePath = saveFilePath
        self.auth = auth

    def setUrl(self,url):
        self.url = url

    def getAuth(self):
        return self.auth

    def setAuth(self,auth=('','')):
        self.auth = auth

    def getUrl(self):
        return self.url

    def setSave(self, path):
        self.saveFilePath = path

    def getSave(self):
        return self.path

    '''
    Use requests module to get a request from 
    '''
    def run(self, timeout=0):
        res = requests.get(self.url, auth=self.auth, timeout=timeout)
        content = BeautifulSoup(res.content, "html.parser")
        return content

    '''
    find a skin for Beautiful soups find/select methods.
    inputs:
    content -> expected from the run method
    target -> a list of html tags/css selectors that the find function will go through
    
    '''
    def searchElems(self, content, target=[], save=False, all=True):
        data = []

        for elem in target:

            if all:
                data.append(content.select(elem))
            else:
                data.append(content.select_one(elem))
            # print(result)
        print(data)
        if save:
            fileName, fileExtension = path.splitext(self.saveFilePath)
            if path.isfile(self.saveFilePath):
                if fileExtension == ".json":
                    json.dump(data, open(self.saveFilePath,'w+'))
                    return
                else:
                    open(self.saveFilePath,'w+').write(*data)
                    return

        return data



