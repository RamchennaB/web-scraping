import requests
from bs4 import BeautifulSoup

req = requests.get("https://cs.fyi/guide/how-does-internet-work")
soup = BeautifulSoup(req.content, "html.parser")
file = open("Scrapeddata.txt", "w+", encoding="utf-8")
file.write(soup.prettify()) 
print("file created successfully")
