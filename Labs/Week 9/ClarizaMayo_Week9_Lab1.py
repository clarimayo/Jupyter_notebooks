import requests
from bs4 import BeautifulSoup

URL = 'https://worldpoverty.io/headline'
page = requests.get(URL)

soup = BeautifulSoup(page.content)

if __name__ == '__main__': #letting me call the name of file    
    print(soup.prettify())