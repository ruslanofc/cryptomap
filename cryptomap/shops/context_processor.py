from bs4 import BeautifulSoup
import requests
import time


def get_crypto_price():
  url='https://www.google.com/search?q=bitcoin+price'
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')
  text = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
  return text


def show_price(request):
  last_price = -1
  while True:
    price = get_crypto_price()
    if price != last_price:
      return {'btc_price': price}
      last_price = price
    time.sleep(3)