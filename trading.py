import requests
from base import BaseModel
class Trading(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def modify_order(self,account_id,order_id,type=None,duration=None,price=None,stop=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders/{order_id}"
        data = {"type":type,"duration":duration,"price":price,"stop":stop}
        
        return requests.put(url=url,data=data,headers=headers)

    def cancel_order(self,account_id,order_id,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders/{order_id}"
        data = {}
        
        return requests.delete(url=url,data=data,headers=headers)

    def place_equity_order(self,account_id,symbol,side,quantity,type,duration,order_class="equity",price=None,stop=None,tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "symbol":symbol,
            "side":side,
            "quantity":quantity,
            "type":type,
            "duration":duration,
            "price":price,
            "stop":stop,
            "tag":tag
        }
        
        return requests.post(url=url,data=data,headers=headers)

    def place_option_order(self,account_id,symbol,option_symbol,side,quantity,type,duration,order_class="option",price=None,stop=None,tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "symbol":symbol,
            "option_symbol":option_symbol,
            "side":side,
            "quantity":quantity,
            "type":type,
            "duration":duration,
            "price":price,
            "stop":stop,
            "tag":tag
        }
        
        return requests.post(url=url,data=data,headers=headers)

    def place_multileg_order(self,account_id,symbol,type,duration,legs,order_class="multileg",price=None,stop=None,tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "symbol":symbol,
            "type":type,
            "duration":duration,
            "price":price,
            "stop":stop,
            "tag":tag
        }
        for leg in legs:
            data.update({
                f"option_symbol[{leg}]":legs[leg]['option_symbol'],
                f"side[{leg}]":legs[leg]['side'],
                f"quantity[{leg}]":legs[leg]['quantity']
            })
        
        return requests.post(url=url,data=data,headers=headers)

    def place_combo_order(self,account_id,symbol,type,duration,legs,order_class="combo",price=None,tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "symbol":symbol,
            "type":type,
            "duration":duration,
            "price":price,
            "tag":tag
        }
        for leg in legs:
            data.update({
                f"side[{leg}]":legs[leg]['side'],
                f"quantity[{leg}]":legs[leg]['quantity']
            })
            if "option_symbol" in legs[leg]:
                data.update({f"option_symbol[{leg}]":legs[leg]['option_symbol']})
        
        return requests.post(url=url,data=data,headers=headers)

    def place_oto_order(self,account_id,duration,legs,order_class="oto",tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "duration":duration,
            "tag":tag
        }
        for leg in legs:
            data.update({
                f"symbol[{leg}]":legs[leg]['symbol'],
                f"type[{leg}]":legs[leg]['type'],
                f"side[{leg}]":legs[leg]['side'],
                f"quantity[{leg}]":legs[leg]['quantity']
            })
            if "option_symbol" in legs[leg]:
                data.update({f"option_symbol[{leg}]":legs[leg]['option_symbol']})
            if "price" in legs[leg]:
                data.update({f"price[{leg}]":legs[leg]['price']})
            if "stop" in legs[leg]:
                data.update({f"stop[{leg}]":legs[leg]['stop']})
                        
        return requests.post(url=url,data=data,headers=headers)

    def place_oco_order(self,account_id,duration,legs,order_class="oco",tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "duration":duration,
            "tag":tag
        }
        for leg in legs:
            data.update({
                f"type[{leg}]":legs[leg]['type'],
                f"side[{leg}]":legs[leg]['side'],
                f"quantity[{leg}]":legs[leg]['quantity']
            })
            if "option_symbol" in legs[leg]:
                data.update({f"option_symbol[{leg}]":legs[leg]['option_symbol']})
            if "symbol" in legs[leg]:
                data.update({f"symbol[{leg}]":legs[leg]['symbol']})
            if "price" in legs[leg]:
                data.update({f"price[{leg}]":legs[leg]['price']})
            if "stop" in legs[leg]:
                data.update({f"stop[{leg}]":legs[leg]['stop']})
                     
        
        return requests.post(url=url,data=data,headers=headers)

    def place_otoco_order(self,account_id,duration,legs,order_class="otoco",tag=None,paper=True):
        account_id,url,api_key,headers = super()._get_keys(account_id=account_id,paper=paper)
        url += f"/v1/accounts/{account_id}/orders"
        data = {
            "class":order_class,
            "duration":duration,
            "tag":tag
        }
        for leg in legs:
            data.update({
                f"type[{leg}]":legs[leg]['type'],
                f"side[{leg}]":legs[leg]['side'],
                f"quantity[{leg}]":legs[leg]['quantity']
            })
            if "option_symbol" in legs[leg]:
                data.update({f"option_symbol[{leg}]":legs[leg]['option_symbol']})
            if "symbol" in legs[leg]:
                data.update({f"symbol[{leg}]":legs[leg]['symbol']})
            if "price" in legs[leg]:
                data.update({f"price[{leg}]":legs[leg]['price']})
            if "stop" in legs[leg]:
                data.update({f"stop[{leg}]":legs[leg]['stop']})
                     
        
        return requests.post(url=url,data=data,headers=headers)
