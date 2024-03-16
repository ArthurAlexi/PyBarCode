from src.validators.tag_creator_validator import tag_creator_validator
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntity

class MockRequest:
    def __init__(self, json) -> None:
        self.json = json

def test_tag_creator_validator_sucess(): 
    mock = MockRequest({'procuct_code': '12345'})
    response = tag_creator_validator(mock)
    assert response is None
    

def test_tag_creator_validator_invalid_json(): 
    mock = MockRequest({'procuct_code': 12345})
    try:
        response = tag_creator_validator(mock)
        assert False
    except Exception as exception:
        assert isinstance(exception, HttpUnprocessableEntity)