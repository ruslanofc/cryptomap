import requests


def get_btc_price():
    headers = {
        'X-CMC_PRO_API_KEY': '07b2b4e0-6cdc-4c7f-8957-7713c0567b98',
        'Accepts': 'application/json',
    }

    parameters = {
      'start': '1',
      'limit': '1',
      'convert': 'RUB'
    }

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    json = requests.get(url, params=parameters, headers=headers).json()

    coins = json['data']

    for x in coins:
        return int(x['quote']['RUB']['price'])