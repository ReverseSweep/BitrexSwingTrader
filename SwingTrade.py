from bittrex import Bittrex
from Exceptions import BuyTooHighError

#Bittrex API -> String
#sets which valid coin to trade
def target_market(api):
    alt_balance = None
    while (alt_balance == None):
        try:
            target_mark = raw_input("Which market would you like to target? \n")
            alt_balance = api.get_balance(target_mark)[u'result'][u'Available']
            return target_mark
        except TypeError:
            print ('enter a real market lol')

def SwingTime(api, market_name):
    print ("Lets swing trade some %s coins! \n" %market_name)
    buy_low = raw_input("At what price do you want to buy at? (Usage: enter price in BTC, or \'BidPrice\' or \'AskPrice\' \n")
    if(buy_low > api.get_ticker(market_name)[u'result'][u'Ask']):
        raise BuyTooHighError("your bid price is higher than the Ask price, try again")



if __name__ == '__main__':
    # Usage is Bittrex("API Key", "API secret Key")
    api = Bittrex("", "")

    # gets the Bittrex account BTC balance
    btc_balance = api.get_balance("BTC")[u'result'][u'Available']
    print("You have %f BTC" % btc_balance)

    #sets which coin to trade
    target_mark = target_market(api)
    alt_balance = api.get_balance(target_mark)[u'result'][u'Available']
    print("You have %s %s coins" % (alt_balance,target_mark))


    market_name = 'BTC-' + target_mark
    alt_ticker = api.get_ticker(market_name)

    bid_price = alt_ticker[u'result'][u'Bid']
    ask_price = alt_ticker[u'result'][u'Ask']

    print("The bid price is %s" % bid_price)
    print("and the ask price is %s" % ask_price)

    #api.buy_limit(market_name,9000,bid_price)
    print("buy order placed @ %s" % bid_price)