from os import times
from select import select
import numpy as np
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import jsons
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

class Stock:
    def __init__(self,url):
        self.url = url
        self.record_str = []
    def __call__(self):
         # Banned from the website
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
        
        sel = Select(driver.find_element_by_xpath("//select"))
        sel.select_by_value("Infinity")
        #timefilter = Select(driver.find_elements(By.CLASS_NAME,"select"))
        # timefilter.select_by_value("Infinity")

        bs4_html = BeautifulSoup(driver.page_source, "html.parser") #爬蟲常用套件BeautifulSoup 把HTML讀成Dictionary(parameter, 原始格式)
        # # find the result box
        result = bs4_html.find(id="__nuxt")
        tbody = result.find("tbody")
        stock_row = tbody.find_all("tr")
        for item in stock_row:
            items = item.find_all("td")
            stock_name = items[2].find("span").text
            self.record_str.append([stock_name])
        return self.record_str
        
if __name__ == "__main__":
    ss = Stock(url="https://brandirectory.com/rankings/global/table") 
    web = ss()
    print(web)
