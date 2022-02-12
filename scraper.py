from typing import Counter
import requests
import re
import sys
import time
import linecache
import os
import selenium
from selenium import webdriver
from bs4 import BeautifulSoup


class WordlePage:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(r'C:/Users/joshu/Documents/GitHub/WordleSolver/chromedriver.exe')

    def expand_shadow_element(self,element):
        shadowRoot = self.driver.execute_script('return arguments[0].shadowRoot.children', element)
        return shadowRoot

    def setBoard(self):
        self.driver.get(self.url)
        root = self.driver.find_element_by_tag_name('game-app')

        shadowBoard = self.expand_shadow_element(root)
        element = shadowBoard[1]
        page=self.driver.execute_script('return arguments[0].innerHTML',element)
        soup = BeautifulSoup(page, "html.parser")
        board = soup.find("div", {'id': 'board'})
        self.board = board
        
    def getCurrentRow(self):
        pass

    def setFoundLetters(self):
        pass