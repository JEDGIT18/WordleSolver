from typing import Counter
import requests
import re
import sys
import winsound
import linecache
import os
from bs4 import BeautifulSoup

class WordlePage:

    def __ini__(url):
        self.url = url
    
    def getBoard(self):
        src = requests.get(self.url)
        parsedSrc = src.text
        soup = BeautifulSoup(parsedSrc, "html.parser")
        board = soup.find("div" {'id': 'board'})
        return board 
        
    def getCurrentRow(self):
        pass

    def setFoundLetters(self):
        pass