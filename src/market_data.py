import requests
from base import BaseModel
class MarketData(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def get_quotes(self,symbols,greeks="false"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/quotes"
        params = {"symbols":symbols,"greeks":greeks}
        
        return requests.get(url=url,params=params,headers=headers)

    def search_quotes(self,symbols,greeks="false"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/quotes"
        data = {"symbols":symbols,"greeks":greeks}
        
        return requests.post(url=url,data=data,headers=headers)

    def get_option_chains(self,symbol,expiration,greeks="false"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/options/chains"
        params = {"symbol":symbol,"expiration":expiration,"greeks":greeks}
        
        return requests.get(url=url,params=params,headers=headers)
        
    def get_option_strikes(self,symbol,expiration):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/options/strikes"
        params = {"symbol":symbol,"expiration":expiration}
        
        return requests.get(url=url,params=params,headers=headers)
        
    def get_option_expirations(self,symbol,includeAllRoots="false",strikes="false",contractSize="false",expirationType="false"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/options/expirations"
        params = {"symbol":symbol,"includeAllRoots":includeAllRoots,"strikes":strikes,"contractSize":contractSize,"expirationType":expirationType}
        
        return requests.get(url=url,params=params,headers=headers)
        
    def get_option_symbols(self,underlying):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/options/lookup"
        params = {"underlying":underlying}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_history(self,symbol,interval="daily",start="2019-05-04",end="2019-05-05",session_filter="all"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/history"
        params = {"symbol":symbol,"interval":interval,"start":start,"end":end,"session_filter":session_filter}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_timesales(self,symbol,interval="tick",start="2019-05-04 09:30",end="2019-05-04 16:00",session_filter="all"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/timesales"
        params = {"symbol":symbol,"interval":interval,"start":start,"end":end,"session_filter":session_filter}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_etb(self):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/etb"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_clock(self):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/clock"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_calendar(self,month="02",year="2024"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/calendar"
        params = {"month":month,"year":year}
        
        return requests.get(url=url,params=params,headers=headers)

    def search_company(self,q,indexes="true"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/search"
        params = {"q":q,"indexes":indexes}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_symbols(self,q,exchanges="All",types="All"):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/v1/markets/lookup"
        params = {"q":q,"exchanges":exchanges,"types":types}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/company"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_calendars(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/calendars"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_dividends(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/dividends"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_actions(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/corporate_actions"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_ratios(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/ratios"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_financials(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/financials"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_company_statistics(self,symbols):
        account_id,url,api_key,headers = super()._get_keys(paper=False)
        url += "/beta/markets/fundamentals/statistics"
        params = {"symbols":symbols}
        
        return requests.get(url=url,params=params,headers=headers)
