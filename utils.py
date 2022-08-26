# https://groww.in/

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# #from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import ActionChains
# import time 
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# from fake_useragent import UserAgent
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time 
import numpy
import yfinance as yf
import requests
import pandas as pd
import csv
from datetime import datetime
import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv()
MONGO_URI = os.environ.get('MONGO_URI')
client = MongoClient(MONGO_URI)
SECRET_KEY = os.environ.get('SECRET_KEY')
db = client["trials"]
col = db["products"]






PATH = "/home/vedha/softwares/chromedriver"

TICKER_LIST = ['TSLA','AMZN','AAPL','w','AMD']


# chrome_options = Options()
# ua = UserAgent()
# userAgent = ua.random

# print(userAgent)

# chrome_options.add_argument(f'user-agent={userAgent}')
# chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# action = ActionChains(driver)

def get_stock_url(ticker):

    driver.get("https://groww.in/search")

    # gets first element from the given tag
    # search = driver.find_element_by_name("q")
    time.sleep(3)


    stock_selection = driver.find_element(By.CSS_SELECTOR, '#searchPage > div.web-align > div.sp23SearchBox.absolute-center.clrText130 > div.sp23EntitySelect.fs15 > div > div > div > div > div.pos-rel.valign-wrapper.se55SelectBox.clrText > input')
    stock_selection = stock_selection.send_keys(Keys.ARROW_DOWN)

    search = driver.find_element(By.XPATH, '//*[@id="sp23Input"]')
    search.click()
    search.send_keys(ticker, Keys.ENTER)

    time.sleep(3)

    reqd_stock = search.find_element(By.XPATH, '//*[@id="searchPage"]/div[2]/div[2]/div[2]/div/div[1]').click()

    cur_url = driver.current_url

    # time.sleep(2)
    # driver.quit()

    return cur_url

def get_indian_stock_low_value(stock):

    cur_url = get_stock_url(stock)

    # print(driver.get(cur_url))

    all_data = {}
    
    values = driver.find_elements('xpath','//*[@class="pbar29Value fs16"]/div/span')
    titles = driver.find_elements('xpath','//*[@class="pbar29KeyText fs14"]')
    for i in range(len(values)):
        all_data[titles[i].text] = values[i].text

    low_val = all_data['Today’s Low']

    # print (low_val)

    return low_val


def get_ticker(company):
       #String that you want to search
    with open("stocks.csv") as f_obj:
        reader = csv.reader(f_obj, delimiter=',')
        for line in reader:      #Iterates through the rows of your csv
                #line here refers to a row in the csv
            if company in str(line):      #If the string you want to search is in the row
                # print("String found in first row of csv")
                # print(type(line))
                # print (line[0])
                return line[0]
            else:
                continue


def classify_company(company):

    pass

def get_low_value(tickerSymbol):

    cur_date = datetime.today().strftime('%Y-%m-%d')

    # tickerSymbol = "AAPL"

    # get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)

    # get the historical prices for this ticker
    tickerDf = tickerData.history(period = '1d', start = cur_date, end = cur_date)
        
    l = tickerDf['Low'].values[0]

    # print(l)

    return l

def get_all_low_values(TICKER_LIST):

    low_values_list = []

    for ticker in TICKER_LIST:
        low_values_list.append(get_low_value(ticker))
    
    # print(low_values_list)

    return low_values_list
def cmp_name():
    l=[]
    # j=0

    for i in col.find():
        l.append(i["Company name"])
    return l

        # print(type(i))

    # Database Name
def get_each_ticker():
    l=[]
    m=[]
    a=cmp_name()
    for item in a:
        l.append(get_ticker(item))
    # print(l)
    m= get_all_low_values(l)
    result_dict = dict(zip(a, m))
    print(result_dict)
    # print(m)



def startpy():
    get_each_ticker()
    # get_low_value('CAJ')

    # get_low_value('AAPL')
    # getTicker('Apple')
    # a= cmp_name()
    # get_ticker('google')




if __name__ == '__main__':
    startpy()

    