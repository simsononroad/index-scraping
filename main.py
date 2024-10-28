from bs4 import BeautifulSoup
import requests
from os import system
from time import sleep as wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
#from pathlib import path

is_app_running = True
debugging = True
page = "index.hu"
tag = "h2"
Class = "cikkcim"
tag1 = "div"
Class1 = "img-container"

chrome_option = Options()
if debugging:
    chrome_option.add_experimental_option("detach", True)
else:
    chrome_option.add_argument("--headless")



def scrape():
    system("clear")
    page_to_scrape = requests.get(f"https://{page}")
    wait(0.1)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    focim = soup.find_all(tag, attrs={"class":Class})
    focim1 = soup.find_all(tag1, attrs={"class":Class1})
    
    
    print("--------Legújabb hírek-------")
    print(f"{focim[0].text}")
    what_open = input("Cikk megnyitása (i/n)\n>>>")
    if what_open == "i":
        driver = webdriver.Chrome(options=chrome_option)
        driver.get("https://index.hu")
        links = driver.find_element("xpath", "//div[contains(@class, 'cim')]")
        links.click()
    else:
        system("clear")
        print(f"{focim[0].text}")
        
        
        
        
    if not debugging:
        driver.quit()       

    

if __name__ == "__main__":
    scrape()