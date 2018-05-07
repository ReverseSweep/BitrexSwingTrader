import BittrexUser


class BittrexInfo:

    def __init__(self, api, selected_market):
        self.api = api
        self.selected_market = selected_market

    def display_info(self):
        # gets the Bittrex account BTC balance
        btc_balance = float(self.api.get_balance("BTC")[u'result'][u'Available'])

        # gets the selected Alt coin balance
        alt_balance = self.api.get_balance(self.selected_market)[u'result'][u'Available']
        return btc_balance, alt_balance

    def display_market(self):
        alt_ticker = self.api.get_ticker(self.selected_market)

        bid_price = alt_ticker[u'result'][u'Bid']
        ask_price = alt_ticker[u'result'][u'Ask']

        return bid_price, ask_price