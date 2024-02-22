import requests
import json
import datetime

from authentication import Authentication
from account import Account
from trading import Trading
from market_data import MarketData
from streaming import Streaming
from watchlist import Watchlist

class Tradier:
    def __init__(self,keys={},docs={}):
        if not keys:
            keys = json.load(open('keys.json','r'))
        if not docs:
            docs = json.load(open('docs.json','r'))
        self.authentication = Authentication(keys)
        self.account = Account(keys)
        self.trading = Trading(keys)
        self.market_data = MarketData(keys)
        self.streaming = Streaming(keys)
        self.watchlist = Watchlist(keys)
        
        self.today = datetime.datetime.today().strftime('%Y-%m-%d')

    def atm_call(self,symbols=[]):
        options = {s:{} for s in symbols}
        return options






    
    def get_state(self,return_clock=False):
        state = 'unknown'
        clock={}
        endpoint_clock = "/v1/markets/clock"
        response = requests.get(self.api_base+endpoint_clock,params={},headers=self.headers)
        if response.status_code==200:
            clock = response.json()
            if clock.get('clock'):
                state = clock['clock']['state']
        else:
            print(response.status_code)
            print(response.text)
        if return_clock:
            return clock
        else:
            return state
    
    
    def get_balance(self,paper=True):
        account_id = self.account_id
        api_base = self.api_base
        headers = self.headers
        if paper:
            account_id = self.paper_account_id
            api_base = self.paper_api_base
            headers = self.paper_headers
        balance = 'unknown'
        endpoint_balance = f"/v1/accounts/{account_id}/balances"
        response = requests.get(api_base+endpoint_balance,params={},headers=headers)
        if response.status_code==200:
            balance = response.json()
        else:
            print(response.status_code)
            print(response.text)
        return balance
    def get_orders(self,tag='',paper=True):
        account_id = self.account_id
        api_base = self.api_base
        headers = self.headers
        if paper:
            account_id = self.paper_account_id
            api_base = self.paper_api_base
            headers = self.paper_headers
        orders = []
        endpoint_order = f"/v1/accounts/{account_id}/orders"
        params={'includeTags': 'true'}
        response = requests.get(api_base+endpoint_order,params=params,headers=headers)
        if response.status_code==200:
            r = response.json()
            if isinstance(r.get('orders'),dict):
                orders = [o for o in r['orders']['order'] if tag in str(o)]
        return orders
    def get_quotes(self,symbols=['']):
        quotes = []
        endpoint_quotes = "/v1/markets/quotes"
        if isinstance(symbols,list) & (len(symbols)>1):
            batch_size = 100
            for i in range(0,len(symbols)+1,batch_size):
                symbols_temp = ",".join(symbols[i:i+batch_size])
                response = requests.get(self.api_base+endpoint_quotes,params={'symbols': symbols_temp},headers=self.headers)
                if response.status_code==200:
                    r = response.json()
                    if r.get('quotes'):
                        quotes.extend(r["quotes"]["quote"])
        else:
            response = requests.get(self.api_base+endpoint_quotes,params={'symbols': symbols[0]},headers=self.headers)
            if response.status_code==200:
                r = response.json()        
                if r.get('quotes'):
                    quotes.append(r['quotes']['quote'])
        return quotes
    def get_timesales(self,params={}):
        if not params.get('start'):
            params['start']=self.today+" 07:00" # 6am ET today
        if not params.get('end'):
            params['end'] = self.today+" 20:00" # 9pm ET today
            
        data = []
        endpoint_order = "/v1/markets/timesales"
        
        #params={"symbol":s, 'interval': 'tick', 'start': start, 'end': end, 'session_filter': 'all'}
        response = requests.get(f"{self.api_base}{endpoint_order}",params=params,headers=self.headers)
        if response.status_code==200:
            r = response.json()
            if r.get("series"):
                data = r.get("series").get("data")
                if isinstance(data,dict):
                    data = [data]
                [d.update({"symbol":params['symbol']}) for d in data]
        return data
    def post_order(self,order,paper=True):
        account_id = self.account_id
        api_base = self.api_base
        headers = self.headers
        if paper:
            account_id = self.paper_account_id
            api_base = self.paper_api_base
            headers = self.paper_headers

        result = {}
        endpoint_order = f"/v1/accounts/{account_id}/orders"
        response = requests.post(api_base+endpoint_order,params=order,headers=headers)
        if response.status_code==200:
            result = response.json()
        return result