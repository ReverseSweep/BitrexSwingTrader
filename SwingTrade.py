from bittrex import Bittrex
from BittrexSwingHelpers.BittrexUser import *

def swing(buy_price, sell_price, market, api, quantity):



if __name__ == '__main__':
    # Usage is Bittrex("API Key", "API secret Key")
    api = Bittrex("", "")

    bittrex_user = BittrexUser(api)

    BittrexUser.select_market(bittrex_user)
    BittrexUser.display_market(bittrex_user)
    BittrexUser.display_info(bittrex_user)

    BittrexUser.get_limits(bittrex_user)

    # api.buy_limit(market,9000,bid_price)
    #print("buy order placed @ %s" % bid_price)


