import requests
from base import BaseModel
class Account(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def get_profile(self,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/user/profile"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_balances(self,account_id=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/balances"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_positions(self,account_id=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/positions"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_history(self,account_id=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/history"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_gainloss(self,account_id=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/gainloss"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_orders(self,account_id=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        params = {}
        
        return requests.get(url=url,params=params,headers=headers)

    def get_order_id(self,account_id=None,id=None,includeTags="true",paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders/{id}"
        params = {"includeTags":includeTags}
        
        return requests.get(url=url,params=params,headers=headers)