<div align=center>
    
# Приложение SlimLink

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/Flask-20232A?style=for-the-badge&logo=flask&logoColor=white)
![Static Badge](https://img.shields.io/badge/sqlalchemy-%23D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=black&logoSize=auto)

</div>

## Описание проекта

**Возможности для пользователей сайта:**

Веб-приложение на Flask для создания коротких ссылок.

Пользователь вводит исходную ссылку которую хочет укоротить, далее пользователь может написать свой вариант короткой ссылки.

Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис сгенерирует её автоматически.

Формат для ссылки по умолчанию — шесть случайных символов, в качестве которых можно использовать:

- большие латинские буквы,
- маленькие латинские буквы,
- цифры в диапазоне от 0 до 9.

Так же у проекта есть API:

- POST-запрос на создание новой короткой ссылки:

```python
http://<your_domain>/api/id/
```

Пример:

- Автоматически сгенерирует короткую ссылку

```json
{
	"url": "https://example.com"
}
```

- Сгенерирует пользовательский вариант короткой ссылки

```json
{
	"url": "https://example.com",
	"custom_id": "string"
}
```

- GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору:

```python
http://<your_domain>/api/id/<short_id>/
```

Пример

```json
{
	"url": {
		"short_link": "http://127.0.0.1:5000/string",
		"url": "https://example.com"
	}
}
```

### Технологии

Python 3.10.11

Flask 3.0.2

flask-sqlalchemy 3.1.1

Flask-WTF 1.2.1

Flask-Migrate 4.0.7

<details>

<summary>
<h4>Как запустить проект:</h4>
</summary>

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:JustLight1/SlimLink.git
```

```bash
cd SlimLink
```

Создать и активировать виртуальное окружение:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

или для пользователей Windows

```bash
source env/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Создать файл `.env` и заполнить его по примеру из файла `.env.example`

Применить миграции

```bash
flask db upgrade
```

Запустить проект:

```bash
flask run
```

</details>

# Автор:

**Форов Александр**

[![Telegram Badge](https://img.shields.io/badge/-Light_88-blue?style=social&logo=telegram&link=https://t.me/Light_88)](https://t.me/Light_88) [![Gmail Badge](https://img.shields.io/badge/forov.py@gmail.com-c14438?style=flat&logo=Gmail&logoColor=white&link=mailto:forov.py@gmail.com)](mailto:forov.py@gmail.com)
