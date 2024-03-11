from flask import Blueprint, request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.tag_creator_view import TagCreatorView
from src.errors.error_handler import handler_errors

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=['POST'])
def create_tag():
    response = None
    try:
        http_request = HttpRequest(body=request.json)
        tag_creator_view = TagCreatorView()
        response =  tag_creator_view.validate_and_create(http_request)
    except Exception as exception:
       response =  handler_errors(exception)
       
    return jsonify(response.body), response.status_code