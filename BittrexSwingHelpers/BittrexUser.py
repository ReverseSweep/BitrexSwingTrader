from CustomExceptions.BuyTooHighError import BuyTooHighError
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
        from BittrexSwingHelpers.BittrexCalculator import BittrexCalculator
        if not BittrexCalculator.is_profitable(self.buy_price, self.sell_price):
            raise BuyTooHighError("You must sell it for higher if you want to make a profit!")


    def trade(self):
        buy_object = self.api.buy_limit(self.target_market, self.quantity, self.buy_price)
        curOrderID = buy_object['result']['uuid']

        while True:
            self.api.wait()
            isFulfilled = True
            orders = self.api.get_open_orders(self.target_market)
            for order in orders['result']:
                if order['OrderUuid'] == curOrderID:
                    isFulfilled = False
            self.api.wait()
            if isFulfilled:
                self.api.sell_limit(self.target_market, self.quantity, self.sell_price)
                print("placed sell order")
                break




