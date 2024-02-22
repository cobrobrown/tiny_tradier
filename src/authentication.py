import requests
from base import BaseModel
class Authentication(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def get_authorization(self,client_id,scope,state,paper=False):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/oauth/authorize"
        params = {"client_id":client_id,"scope":scope,"state":state}
        
        response = requests.get(url=url,params=params,headers=headers)
        return response
        
    def post_access_token(self,client_id,client_secret,code,paper=False):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/oauth/accesstoken"
        data = {"grant_type":"authorization_code","code":code}
        auth = (client_id,client_secret)
        headers = {"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"}
        
        response = requests.post(url=url,data=data,headers=headers,auth=auth)
        return response
        
    def post_refresh_token(self,client_id,client_secret,refresh_token,paper=False):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/oauth/refreshtoken"
        data = {"grant_type":"refresh_token","refresh_token":refresh_token}
        auth = (client_id,client_secret)
        headers = {"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"}
        
        response = requests.post(url=url,data=data,headers=headers,auth=auth)
        return response