# https://groww.in/

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
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

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
    driver.quit()

    return cur_url


def scrap_stock_url(stock):

    # cur_url = get_stock_url(stock)
    cur_url = 'https://groww.in/stocks/infosys-ltd'

    url_text = requests.get(cur_url).text

    soup = BeautifulSoup(url_text, 'html.parser') 
    all_results = soup.find_all('div', class_ = "col l12")

    all_results = all_results[3]

    all_results = all_results.find_all('div', id = 'stf545Stock')

    # all_results = all_results.find_all


    for result in all_results:
        print (result.prettify())
        print()
        print()
        print('******************************************')
        print()
        print()
        # print(all_results)


    # todays_low = soup.find_all('div', class_ = 'pbar29SubDiv left-align')
    # print(todays_low)

    # documentObjectModel = etree.HTML(str(soup)) 
    # print (documentObjectModel.xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[4]/div[1]')[0].text)
    # # //*[@id="root"]/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[4]/div[1]


def startpy():

    scrap_stock_url('INFY')




if __name__ == '__main__':
    startpy()

    