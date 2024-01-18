import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://220.lv/lv/"
driver.get(url)
time.sleep(3)
find=driver.find_element(By.LINK_TEXT, "Informācija")
find=driver.find_element(By.LINK_TEXT, "Garantijas")
find.click()
find=driver.find_element(By.LINK_TEXT, "Preces pieņemšana/nodošana Servisā vai veikalā")
find.click()
find=driver.find_element(By.LINK_TEXT, "Neatbilstības novēršanas termiņi un nosacījumi")
find.click()
input()