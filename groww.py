# https://groww.in/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time 

PATH = "/home/vedha/softwares/chromedriver"
# driver = webdriver.Chrome(service)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)



def startpy():
    driver.get("https://groww.in/search")

    # gets first element from the given tag
    # search = driver.find_element_by_name("q")
    stock = driver.find_element(By.CSS_SELECTOR, '#searchPage > div.web-align > div.sp23SearchBox.absolute-center.clrText130 > div.sp23EntitySelect.fs15 > div > div > div > div > div.pos-rel.valign-wrapper.se55SelectBox.clrText > input')
    stock = stock.send_keys(Keys.ARROW_DOWN)
    search = driver.find_element(By.XPATH, '//*[@id="sp23Input"]')
    print(search)
    search.click()
    # sm = stock.find_element(By.XPATH, '//*[@id="searchPage"]/div[2]/div[1]/div[1]/div').click()
    search.send_keys("INFY", Keys.ENTER)

    # search = driver.find_element(By.CSS_SELECTOR, "#globalSearch23-suggestionsContainer > div.se28GetDivAboveSuggestion > div > div:nth-child(2)")
    

    # search.send_keys(Keys.RETURN)
    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    startpy()