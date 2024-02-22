import requests
from base import BaseModel
class Watchlist(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def get_watchlist(self,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/watchlists"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_watchlist_id(self,watchlist_id,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += f"/v1/watchlists/{watchlist_id}"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def create_watchlist(self,name,symbols,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/watchlists"
        data = {"name":name,"symbols":symbols}
        headers.update({"Content-Type":"application/x-www-form-urlencoded"})
        
        return requests.post(url=url,data=data,headers=headers)

    def update_watchlist(self,watchlist_id,name,symbols="",paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += f"/v1/watchlists/{watchlist_id}"
        data = {"name":name,"symbols":symbols}
        headers.update({"Content-Type":"application/x-www-form-urlencoded"})
        
        return requests.put(url=url,data=data,headers=headers)

    def delete_watchlist(self,data,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += f"/v1/watchlists/{watchlist_id}"
        data = {}
        
        return requests.delete(url=url,data=data,headers=headers)

    def add_symbols(self,watchlist_id,symbols,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += f"/v1/watchlists/{watchlist_id}/symbols"
        data = {"symbols":symbols}
        headers.update({"Content-Type":"application/x-www-form-urlencoded"})
        
        return requests.post(url=url,data=data,headers=headers)

    def remove_symbol(self,watchlist_id,symbol,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += f"/v1/watchlists/{watchlist_id}/symbols/{symbol}"
        data = {}
        
        return requests.delete(url=url,data=data,headers=headers)