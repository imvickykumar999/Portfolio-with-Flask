import requests
from bs4 import BeautifulSoup

url = input('Enter URL : ')
if url == '':
    url = 'https://vixportfoliowithflask.herokuapp.com/contact'
    
headers = {"User-agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html5lib')

for i in range(int(len(soup.findAll(class_= "col mb-4")))):
    print(soup.findAll(class_= "col mb-4")[i].a['href'])
    
