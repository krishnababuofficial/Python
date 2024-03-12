from bs4 import BeautifulSoup
import requests,openpyxl


response = requests.get("https://en.wikipedia.org/wiki/Tesla,_Inc.")
soup = BeautifulSoup(response.text,"html.parser")
'print(soup)'
anchor = soup.find_all('img')
'print(anchor)'
list = soup.find_all(class_="mw-headline")
print(list)
for x in list:
    print(x)
