import os, requests

class CurrencyConverter:
    currency_api_url = "https://v6.exchangerate-api.com/v6/"

    def __init__(self, api_key):
        self.conversion_rate_cache = {}
        self.api_key = api_key

    def set_source(self, source_currency):
        self.source = source_currency

    def set_target(self, target_currency):
        self.target = target_currency

    def get_rate(self):

        # get the conversion rate
        endpoint = f"{CurrencyConverter.currency_api_url}/{self.api_key}/latest/{self.source}"
        print(endpoint)
        r = requests.get(endpoint)
        print(r.status_code)
        data = r.json()
        self.conversion_rate = data["conversion_rates"][self.target]
    
    def convert(self, amount):
        return self.conversion_rate * amount

def main():

    # get the api key
    api_key = os.environ.get('EXCHANGE_CURRENCY_KEY')

    if not api_key:
        print("The EXCHANGE_CURRENCY_KEY is not present")
        return

    # new currency converter
    my_currency_converter = CurrencyConverter(api_key)

    # set source and target currency and get the amount
    my_currency_converter.set_source("AUD")
    my_currency_converter.set_target("CAD")
    my_currency_converter.get_rate()
    print(f"The new number is {my_currency_converter.convert(4)}")


if __name__ == '__main__':
    main()