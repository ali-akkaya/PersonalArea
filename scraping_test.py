import  requests
from  bs4 import BeautifulSoup


def get_links():
    url = "https://vymaps.com/sitemap/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"lxml")
    soup.