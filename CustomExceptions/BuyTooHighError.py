class BuyTooHighError(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("BittrexUser defined exception: ",self.msg)