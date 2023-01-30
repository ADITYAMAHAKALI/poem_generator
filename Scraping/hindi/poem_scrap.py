import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

prefix = "http://www.kavitakosh.org/kk/"
writer = input("Enter hindi poet's name: ")
url = prefix+writer
print(url)
data = requests.get(url)
soup = bs(data.content,"html.parser")
print(soup)
