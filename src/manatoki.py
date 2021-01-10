from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import datetime
import time

class manatoki:
    def __init__(self, name):
        self.name = name
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('headless')
        self.driver = \
            webdriver.Chrome('../chromedriver/chromedriver.exe', \
            chrome_options=self.options)
        self.url = "https://manatoki92.net/"

    def initSiteAndSearch(self):
        self.driver.get(self.url)
        self.driver.find_element_by_xpath(\
            '//*[@id="top-search"]/a/div').click()
        self.driver.find_element_by_xpath(\
            '//*[@id="top-search"]/ul/li/form/div/div[1]/input')\
                .send_keys(self.name)
        self.driver.find_element_by_xpath(\
            '//*[@id="top-search"]/ul/li/form/div/div[2]/button')\
                .click()

    def specifyToon(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        toonList = soup.select_one('#webtoon-list-all')
        for li in toonList.select('li'):
            href = li.find('div', class_='img-item').find('a').get('href')
            candidate = li.find('div', class_='in-lable trans-bg-black').string
            if candidate == self.name:
                self.driver.get(href)
                return 1
        return None

    def getDate(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        date = soup.select_one('#serial-move > div > ul > li:nth-child(1) > '\
            + 'div.wr-date.hidden-xs').get_text().strip()
        try:
            formalDate = datetime.datetime.strptime(date, "%Y.%m.%d")
        except ValueError:
            return "Today"
        return formalDate
        
    def routine(self):
        self.initSiteAndSearch()
        if self.specifyToon() == None:
            return 2

        dateData = self.getDate()
        if dateData == "Today":
            return 0

        dataSub = datetime.datetime.now() - dateData
        if dataSub.days < 3:
            return 0
        else: 
            return 1