from CustomExceptions.BuyTooHighError import BuyTooHighError
import BittrexCalculator


class BittrexUser:

    buy_price = None
    sell_price = None
    target_market = None
    quantity = None

    def __init__(self, api):
        self.api = api

    def select_market(self):
        alt_balance = None
        while alt_balance is None:
            try:
                target = raw_input("Which market would you like to target? \n")
                alt_balance = self.api.get_balance(target)[u'result'][u'Available']
                self.target_market = 'BTC-' + str(target)
            except TypeError:
                print ('Enter a real market.')

    def get_limits(self):
        print ("Lets swing trade some %s coins! \n" % self.target_market)
        self.buy_price = raw_input("At what price do you want to buy at? "
                              "(Usage: enter price in BTC, or \'BidPrice\' or \'AskPrice\' \n")
        if self.buy_price > self.api.get_ticker(self.target_market)[u'result'][u'Ask']:
            raise BuyTooHighError("your bid price is higher than the Ask price, try again")

        self.sell_price = raw_input("At what price do you want to sell at? "
                               "(Usage: enter price in BTC, or \'SellPrice\' \n")

        if BittrexCalculator.is_profitable(self.buy_price, self.sell_price):
            raise BuyTooHighError("You must sell it for higher if you want to make a profit!")

