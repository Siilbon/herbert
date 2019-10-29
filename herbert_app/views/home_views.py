from flask import Blueprint
from herbert_app.infrastructure.view_modifiers import response
from herbert_app.services.common import common_herbs, common_conditions, get_team

bp = Blueprint('home', __name__)


@bp.route('/')
@response(template_file='home/home.html')
def home():
    common_herbs_list = common_herbs()

    common_conditions_list = common_conditions()

    example = common_herbs(1)
    example = f'e.g. {example[0]}'

    team = get_team()

    return {
        'common_herbs': common_herbs_list,
        'common_conditions': common_conditions_list,
        'example': example,
        'team': team
    }


@bp.route('/contact')
@response(template_file='home/contact.html')
def contact():
    return {'team': get_team()}


@bp.route('/karl')
def karl():
    return "Karl's bp is working"