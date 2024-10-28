from bs4 import BeautifulSoup
import requests
from os import system
from time import sleep as wait

is_app_running = True

page = "index.hu"
tag = "h2"
Class = "cikkcim"



def scrape():
    system("clear")
    page_to_scrape = requests.get(f"https://{page}")
    wait(0.1)
    soup = BeautifulSoup(page_to_scrape.text, "html.parser")
    quotes = soup.find_all(tag, attrs={"class":Class})
    print(quotes[0].text)

    

if __name__ == "__main__":
    scrape()