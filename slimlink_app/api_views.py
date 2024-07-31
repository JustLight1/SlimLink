from flask import jsonify, request

from . import app, db
from .models import URL_map
from .error_handlers import InvalidAPIUsage
from .utils import get_unique_short_id, check_custom_id


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_short_link(short_id):
    url = URL_map.query.filter_by(short=short_id).first()
    if url is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url.to_dict()}), 200


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    if not request.is_json:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    data = request.get_json()

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    custom_id = data.get('custom_id')
    if custom_id:
        if not check_custom_id(custom_id) or len(custom_id) > 16:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if (URL_map.query.filter_by(short=data['custom_id']).first()
                is not None):
            raise InvalidAPIUsage(f'Имя "{custom_id}" уже занято.')
    else:
        custom_id = get_unique_short_id()
    url = URL_map(original=data['url'], short=custom_id)
    url.from_dict(data)
    db.session.add(url)
    db.session.commit()
    return jsonify(url.to_dict()), 201
