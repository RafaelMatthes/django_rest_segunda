import requests

URL_API = 'https://economia.awesomeapi.com.br/json/last/'

class CurrencyRate():

    @classmethod
    def get_price(cls, currency):
        response = requests.get(f"{URL_API}{currency}-BRL", timeout=0.5)

        if response.status_code == 200:
            response_json = response.json()[f'{currency}BRL']

            return {
                "price" : f"R$:{response_json['bid']}",
                "high" : f"R${response_json['high']}",
                "low" : f"R${response_json['low']}",
            }

        return None




# print(CurrencyRate().get_price('USD'))