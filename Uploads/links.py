from bs4 import BeautifulSoup, SoupStrainer
import requests

url = "https://dailycaring.com/"

page = requests.get(url)
data = page.text
soup = BeautifulSoup(data)

for link in soup.find_all('a'):
    print(link.get('href'))
