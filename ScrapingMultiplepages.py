import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

for i in range(1,66):
    Names = []
    Location=[]
    City=[]
    Phone=[]
    POBOX=[]
    Companylink=[]
    r = requests.get(f"https://www.yellowpages-uae.com/uae/restaurant-{i}.html")
    soup = BeautifulSoup(r.text, "lxml")
    box=soup.find("div",id="listings")
    names = box.find_all("div",class_="col-lg-11 col-md-10 col-sm-8 col-xs-8 col-12 title-div")
    location=box.find_all("span",itemprop="streetAddress")
    city=box.find_all("strong",{ "itemprop":"addressLocality"})
    phone=box.find_all("span",class_="phone")
    pobox=box.find_all("span",class_="pobox")
    companylink = soup.find_all('a',title="Restaurant suppliers in UAE")
    for i in names:
        n=i.text
        Names.append(n)
    print(Names)
    for i in location:
        l=i.text
        Location.append(l)
    print(Location)
    for i in city:
        c=i.text
        City.append(c)
    print(City)
    for i in phone:
        p=i.text
        Phone.append(p)
    print(Phone)
    for i in pobox:
        po=i.text
        POBOX.append(po)
    print(POBOX)
    for link in companylink:
        href = link.get('href')
        Companylink.append(href)
    print(Companylink)
    data = zip(Names, Location, City, Phone, POBOX, Companylink)
    with open("result.csv","a+",newline="\n") as f:
        writer=csv.writer(f)
        writer.writerow(['Name', 'Location', 'City', 'Phone','P.O BOX','Companylink'])
        writer.writerows(data)
