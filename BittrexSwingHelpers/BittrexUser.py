from CustomExceptions.BuyTooHighError import BuyTooHighError
from BittrexCalculator import BittrexCalculator
import time


class BittrexUser:

    buy_price = None
    sell_price = None
    target_market = None
    quantity = None

    def __init__(self, api):
        self.api = api

    def select_market(self, market_name):
        try:
            self.target_market = 'BTC-' + str(market_name)
        except TypeError:
            print ('Enter a valid market.')

    def set_limits(self, buy_price, sell_price, quantity):
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.quantity = quantity
        if not BittrexCalculator.is_profitable(self.buy_price, self.sell_price):
            raise BuyTooHighError("You must sell it for higher if you want to make a profit!")


    def trade(self):
        buy_object = self.api.buy_limit(self.target_market, self.quantity, self.bid_price)
        #check every 10 seconds to see if the buy order has been filled. If it has, place a sell order, else keep checking

        print(buy_object)

