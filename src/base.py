class BaseModel:
    def __init__(self,keys):
        self.keys = keys
        self.base_url = "https://api.tradier.com"
        self.streaming_url = "https://stream.tradier.com"
        self.wss_url = "wss://ws.tradier.com"
        self.sandbox_url = "https://sandbox.tradier.com"
        self.headers = {'Authorization': 'Bearer {api_key}', 'Accept': 'application/json'}
    def _get_keys(self,account_id=None,url=None,api_key=None,paper=None):
        key_account_id,key_url,key_api_key = None,None,None
        key_headers = self.headers.copy()
        # resolve by priority
        # account_id -> url -> api_key -> paper
        if account_id:
            if account_id==self.keys['tradier_account_id']:
                key_account_id = account_id
                key_url = self.base_url
                key_api_key = self.keys['tradier_api_key']
            elif account_id==self.keys['tradier_paper_account_id']:
                key_account_id = account_id
                key_url = self.sandbox_url
                key_api_key = self.keys['tradier_paper_api_key'] 
        elif url:
            if url==self.keys['tradier_api_base']:
                key_account_id = self.keys['tradier_account_id']
                key_url = url
                key_api_key = self.keys['tradier_api_key']
            elif url==self.keys['tradier_paper_api_base']:
                key_account_id = self.keys['tradier_paper_account_id']
                key_url = url
                key_api_key = self.keys['tradier_paper_api_key'] 
        elif api_key:
            if api_key==self.keys['tradier_api_base']:
                key_account_id = self.keys['tradier_account_id']
                key_url = self.keys['tradier_api_base']
                key_api_key = api_key
            elif api_key==self.keys['tradier_paper_api_base']:
                key_account_id = self.keys['tradier_paper_account_id']
                key_url = self.keys['tradier_paper_api_base']
                key_api_key = api_key
        elif paper is not None:
            if not paper:
                key_account_id = self.keys['tradier_account_id']
                key_url = self.keys['tradier_api_base']
                key_api_key = self.keys['tradier_api_key']
            elif paper:
                key_account_id = self.keys['tradier_paper_account_id']
                key_url = self.keys['tradier_paper_api_base']
                key_api_key = self.keys['tradier_paper_api_key']
        key_headers['Authorization'] = key_headers['Authorization'].format(api_key=key_api_key)
        return key_account_id,key_url,key_api_key,key_headers
    