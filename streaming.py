import requests
import asyncio
import websockets
from base import BaseModel
class Streaming(BaseModel):
    def __init__(self,keys):
        super().__init__(keys)
    def get_market_stream(self,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/markets/events/session"
        data = {}
        
        return requests.post(url=url,data=data,headers=headers)

    def get_account_stream(self,paper=True):
        account_id,url,api_key,headers = super()._get_keys(paper=paper)
        url += "/v1/accounts/events/session"
        data = {}
        
        return requests.post(url=url,data=data,headers=headers)

    async def stream_market(self,symbols,session_id,filter=["trade","quote","summary","timesale","tradex"],linebreak="false",validOnly="true",advancedDetails="false"):
        uri = self.wss_url + "/v1/markets/events"
        payload = {"symbols":symbols,"sessionid":session_id,"filter":filter,"linebreak":linebreak,"validOnly":validOnly,"advancedDetails":advancedDetails}
        payload_str = json.dumps(payload)
        async with websockets.connect(uri, ssl=True, compression=None) as websocket:
            await websocket.send(payload_str)
            print(f">>> {payload_str}")
            async for message in websocket:
                print(f"<<< {message}")
    async def stream_account(self,events,session_id,excludeAccounts=None):
        uri = self.wss_url + "/v1/accounts/events"
        payload = {"events":events,"sessionid":session_id,"excludeAccounts":excludeAccounts}
        payload_str = json.dumps(payload)
        async with websockets.connect(uri, ssl=True, compression=None) as websocket:
            await websocket.send(payload_str)
            print(f">>> {payload_str}")
            async for message in websocket:
                print(f"<<< {message}")