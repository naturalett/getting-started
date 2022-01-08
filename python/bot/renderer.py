import requests
from bs4 import BeautifulSoup
import lxml

class Renderer:
    def __init__(self):
        self.url = "https://www.amazon.com/Luby-GT606-Pressure-Cooker-340320340mm/dp/B07DWHSPCF/ref=psdc_3117954011_t1_B07WL1XBBD"
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
        price = soup.find(id="attach-base-product-price").get('value')
        price_as_float = float(price)
        return price_as_float




# <class 'bs4.element.Tag
#     priceprice: < input
#     id = "attach-base-product-price"
#     type = "hidden"
#     value = "81.99" / >
