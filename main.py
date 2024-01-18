import selenium
sys.path
sys.executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
from openpyxl import Workbook, load_workbook 

service = Service()
option = webdriver.ChromeOptions()
option.add_argument('--no-sandbox')
option.add_argument('--headless')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=option)

name=[]
# program read information from people.csv file and put all data in name list.
with open("people.csv", "r") as file:
    next(file)
    for line in file:
        row=line.rstrip().split(",") 
        name.append(row)
csv_file_path = 'people.csv'

Full_names = []
with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',', quotechar='"')
    for row in csv_reader:
        # Combine the first and last names if both columns are present.
        if 'First Name' in row and 'Last Name' in row:
            Full_names.append(f"{row['First Name']} {row['Last Name']}")
print (Full_names)
url = "https://emn178.github.io/online-tools/crc32.html"
driver.get(url)
time.sleep(2)
name_input = driver.find_element(By.ID, "input")
decoded_input = driver.find_element(By.ID, "output")
temp1 = []