import requests
from bs4 import BeautifulSoup
#random url below 
url='https://'
r= requests.get(url)
soup=BeautifulSoup(r.content,'html.parser')
title=soup.find_all('div',{'class':'header-main_slider'})
for t in title:
    print(t.getText())
