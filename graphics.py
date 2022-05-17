from bs4 import BeautifulSoup
import requests
import re

gpu = input("What product do you want to search for")

url = f"https://www.newegg.com/p/pl?d=3080&N=8000%204131"

page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong
print(page_text)



