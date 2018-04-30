class BittrexInfo:

    def __init__(self, api, selected_market):
        self.api = api
        self.selected_market = selected_market

    def display_info(self):
        # gets the Bittrex account BTC balance
        btc_balance = float(self.api.get_balance("BTC")[u'result'][u'Available'])
        print("You have %f BTC" % btc_balance)

        # gets the selected Alt coin balance
        alt_balance = self.api.get_balance(self.selected_market)[u'result'][u'Available']
        print("You have %s %s coins" % (alt_balance, self.selected_market))

    def display_market(self):
        alt_ticker = self.api.get_ticker(self.selected_market)

        bid_price = alt_ticker[u'result'][u'Bid']
        ask_price = alt_ticker[u'result'][u'Ask']

        print("The bid price is %s" % bid_price)
        print("and the ask price is %s" % ask_price)