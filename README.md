# Django and RethinkDB

Small repo showing how to use Django and RethinkDB together. App uses Tornado for websockets, RethinkDB for messages, and Django users (with MySQL) for authentication.

## Setup

```
git clone ...
virtualenv venv
pip install
python manage.py migrate
```

### Running

```
export PYTHONPATH=.;export DJANGO_SETTINGS_MODULE=django_and_rethinkdb.settings; python django_and_rethinkdb/tornado_main.py
```
