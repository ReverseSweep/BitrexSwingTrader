from bittrex import Bittrex

api = Bittrex()
print(api.get_market_history("BTC-NEO"))