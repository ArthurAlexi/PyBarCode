from typing import Dict

class HttpResponse:
    
    def __init__(self, status_code: int = None, body: Dict | any = None) -> None:
        self.status_code = status_code
        self.body = body
        
        pass
    