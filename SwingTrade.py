from bittrex import Bittrex
from BittrexSwingHelpers.BittrexUser import *


if __name__ == '__main__':
    # Usage is Bittrex("API Key", "API secret Key")
    api = Bittrex("24f34272a52148d79f63bc8f9fffe299", "2d4e08340f6c4eee8625a0503e6aed5d")

    bittrex_user = BittrexUser(api)
    bittrex_user.select_market("DOGE")
    bittrex_user.set_limits(0.00009, 0.79, 1000)

    # api.buy_limit(market,9000,bid_price)
    #print("buy order placed @ %s" % bid_price)


