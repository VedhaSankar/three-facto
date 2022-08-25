# https://groww.in/

from tkinter import CURRENT
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time 
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests

PATH = "/home/vedha/softwares/chromedriver"

chrome_options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)
chrome_options.add_argument(f'user-agent={userAgent}')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
action = ActionChains(driver)

def get_stock_url(stock):

    driver.get("https://groww.in/search")

    # gets first element from the given tag
    # search = driver.find_element_by_name("q")

    stock_selection = driver.find_element(By.CSS_SELECTOR, '#searchPage > div.web-align > div.sp23SearchBox.absolute-center.clrText130 > div.sp23EntitySelect.fs15 > div > div > div > div > div.pos-rel.valign-wrapper.se55SelectBox.clrText > input')
    stock_selection = stock_selection.send_keys(Keys.ARROW_DOWN)

    search = driver.find_element(By.XPATH, '//*[@id="sp23Input"]')
    search.click()
    search.send_keys(stock, Keys.ENTER)

    time.sleep(5)

    reqd_stock = search.find_element(By.XPATH, '//*[@id="searchPage"]/div[2]/div[2]/div[2]/div/div[1]').click()

    cur_url = driver.current_url

    time.sleep(5)
    driver.quit()

    return cur_url


def scrap_stock_url(stock):

    cur_url = get_stock_url(stock)

    url_text = requests.get(cur_url).text

    soup = BeautifulSoup(url_text, 'lxml') 

    print(soup)


def startpy():

    scrap_stock_url('INFY')




if __name__ == '__main__':
    startpy()