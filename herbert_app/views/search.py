from flask import Blueprint
from herbert_app.infrastructure.view_modifiers import response

bp = Blueprint('search', __name__, template_folder='templates')


@bp.route('/search/<search_term>')
@response(template_file='search/results.html')
def search(search_term):
    return {'search_term': search_term}