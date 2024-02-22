import json
import datetime

from authentication import Authentication
from account import Account
from trading import Trading
from market_data import MarketData
from streaming import Streaming
from watchlist import Watchlist

class Tradier:
    def __init__(self,keys={}):
        if not keys:
            keys = json.load(open('keys.json','r'))
        self.authentication = Authentication(keys)
        self.account = Account(keys)
        self.trading = Trading(keys)
        self.market_data = MarketData(keys)
        self.streaming = Streaming(keys)
        self.watchlist = Watchlist(keys)
        
        self.today = datetime.datetime.today().strftime('%Y-%m-%d')
