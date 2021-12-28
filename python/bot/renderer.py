'''
http://myhttpheader.com/
'''

import requests
import lxml
from bs4 import BeautifulSoup


class Renderer:
    def __init__(self):
        self.url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
        self.header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

    def get_soup(self):
        response = requests.get(self.url, headers=self.header)
        soup = BeautifulSoup(response.content, "lxml")
        return soup

    def find_price(self):
        soup = self.get_soup()
        print(soup.prettify())

        price = soup.find(id="size_name_0_price").get_text()
        price_without_currency = price.split("$")[1]
        price_as_float = float(price_without_currency)
        return price_as_float


