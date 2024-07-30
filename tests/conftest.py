import sys
from pathlib import Path

import pytest
from dotenv import load_dotenv
from mixer.backend.flask import mixer as _mixer

load_dotenv()

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(BASE_DIR))


try:
    from slimlink_app import app, db
    from slimlink_app.models import URL_map
except NameError:
    raise AssertionError(
        'Не обнаружен объект приложения. Создайте экземпляр класса Flask и назовите его app.',
    )
except ImportError as exc:
    if any(obj in exc.name for obj in ['models', 'URL_map']):
        raise AssertionError('В файле models не найдена модель URL_map')
    raise AssertionError(
        'Не обнаружен объект класса SQLAlchemy. Создайте его и назовите db.')


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
def mixer():
    _mixer.init_app(app)
    return _mixer


@pytest.fixture
def short_python_url(mixer):
    with app.app_context():
        short_url = mixer.blend(
            URL_map, original='https://www.python.org', short='py')
        db.session.add(short_url)
        db.session.refresh(short_url)
    return short_url
