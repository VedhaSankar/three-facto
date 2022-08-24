# https://groww.in/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time 

PATH = "/home/vedha/softwares/chromedriver"
# driver = webdriver.Chrome(service)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



def startpy():
    driver.get("https://www.google.com/")

    # gets first element from the given tag
    # search = driver.find_element_by_name("q")
    search = driver.find_element(By.NAME, "q")
    search.send_keys("cats")
    search.send_keys(Keys.RETURN)
    time.sleep(5)

    driver.quit()


if __name__ == '__main__':
    startpy()