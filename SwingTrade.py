from bittrex import Bittrex
from BittrexSwingHelpers.BittrexUser import *


if __name__ == '__main__':
    # Usage is Bittrex("API Key", "API secret Key")
    api = Bittrex("3a1ece39c1cb475b85796d29cc1eef2b", "a4b1e1ec83cf4bf78934bd51903f0e40")

    bittrex_user = BittrexUser(api)
    bittrex_user.select_market("DOGE")
    bittrex_user.set_limits(buy_price=0.00000054, sell_price=0.00000059, quantity=1000)
    bittrex_user.trade()
