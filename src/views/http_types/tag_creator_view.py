from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.services.tag_creator_service import TagCreatorService


class TagCreatorView:
    
    def __init__(self) -> None:
        pass
    
    def validate_and_create(self,http_request: HttpRequest)-> HttpResponse:
        body = http_request.body
        product_code = body.get('product_code')
        tag_creator_service = TagCreatorService()
        response =  tag_creator_service.create_tag(product_code)
        http_response = HttpResponse(status_code= 200, body= response)
        return http_response
    