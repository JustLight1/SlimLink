import os
import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))

try:
    from slimlink_app import app, db
    from slimlink_app.models import URL_map  # noqa
except NameError as exc:
    raise AssertionError(
        'При попытке импорта объекта приложения вознакло исключение: '
        f'`{type(exc).__name__}: {exc}`'
    )
except ImportError as exc:
    if any(obj in exc.name for obj in ['models', 'URL_map']):
        raise AssertionError('В файле `models` не найдена модель `URL_map`.')
    raise AssertionError(
        'При попытке запуска приложения вознакло исключение: '
        f'`{type(exc).__name__}: {exc}`'
    )


@pytest.fixture
def default_app():
    with app.app_context():
        yield app


@pytest.fixture
def _app():
    app.config.update({
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
    })
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()
        db.session.close()


@pytest.fixture
def client(_app):
    return _app.test_client()


@pytest.fixture
def cli_runner():
    return app.test_cli_runner()


@pytest.fixture
def short_python_url():
    url_map_object = URL_map(original='https://www.python.org', short='py')
    db.session.add(url_map_object)
    db.session.commit()
    return url_map_object


@pytest.fixture(scope='session')
def duplicated_custom_id_msg():
    return 'Предложенный вариант короткой ссылки уже существует.'
