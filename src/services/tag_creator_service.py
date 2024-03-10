from src.drivers.barcode_handler import BarcodeHandler
from typing import Dict

class TagCreatorService:
    
    def __init__(self) -> None:
        pass
    
    def create_tag(self, product_code: str)-> Dict:
        path_from_tag = self.__create_tag(product_code)
        return self.__format_response(path_from_tag)
    
    def __create_tag(self, product_code: str)->str:
        bar_code_handler =  BarcodeHandler()
        return bar_code_handler.create_barcode(product_code)
    
    def __format_response(self, path_from_tag: str)-> Dict:
        return {
            'data': {
                'type': 'Tag Image',
                'count': 1,
                'path_from_tag': f'{path_from_tag}.png'
            }
        }
    