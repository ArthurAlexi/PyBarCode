from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from barcode import Code128
from barcode.writer import ImageWriter

class TagCreatorView:
    
    def __init__(self) -> None:
        pass
    
    def validate_and_create(self,http_request :HttpRequest)-> HttpResponse:
        body = http_request.body
        product_code = body.get('product_code')
        
        tag = Code128(product_code, writer=ImageWriter())
        path_from_tag = f'{tag}'
        tag.save(path_from_tag)
        return jsonify({'path_from_tag': path_from_tag})
        http_response = HttpResponse(status_code= 200, body= {'response': 'OK'})
        return http_response
    