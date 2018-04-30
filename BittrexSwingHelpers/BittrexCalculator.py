# Bittrex's minimum order total in BTC
BITTREX_MINIMUM_ORDER = 0.0005
# Bittrex's commission fee (converted to decimal)
BITTREX_COMMISSION_FEE = 0.0025


class BittrexCalculator:

    def __init__(self):
        pass

    # Calculates the amount of alts to keep/sell for BTC based on the % of the profit that user wants to keep in BTC
    # Profits are calculated as: profits = # altcoins bought - # altcoins sold to recover original buy cost
    # Example: BTC_split = 1 results in all profits kept as BTC
    # BTC_split = 0.5, half of profits sold for BTC
    # BTC_split = 0, keep profits in alts
    # REQUIRES: profitable swing

    @staticmethod
    def calc_profit_keep(self, buy_price, sell_price, quantity, BTC_split=0.5):
        BTC_profit = (sell_price - buy_price) * quantity  # profit in BTC
        alts_to_sell = (BTC_profit(1 - BTC_split)) / sell_price

        return alts_to_sell

    @staticmethod
    def is_min_order_fulfilled(self, buy_price, quantity):
        return buy_price * quantity > BITTREX_MINIMUM_ORDER

    @staticmethod
    def is_profitable(buy, sell):
        commission1 = buy * BITTREX_COMMISSION_FEE
        commission2 = sell * BITTREX_COMMISSION_FEE
        return (sell - buy) - (commission1 + commission2) > 0
