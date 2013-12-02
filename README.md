# Django sample app number six

Testing performance of a django app.

The testing variables are (should be):

- python version (2.7 - 3.4)
 - wsgi app server (gunicorn, uWSGI)
 - sync/async mode (gevent)
 - storage (postgresql, mongodb, memcache, sqlite)
 - deploy environment (PaaS)


# Developer environment setup

## Python

Python 2.7:

    (install virtualenv)
    virtualenv virtual-2.7 && source virtual/bin/activate

Python 3.3:

    python -m venv virtual-3.3 && source virtual/bin/activate
    wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py
    python ez_setup.py
    wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py
    python get_pip.py

Python 3.4:

    python -m venv virtual-3.4 && source virtual/bin/activate
    python -m ensurepip

All versions:

    pip install -r requirements/server.txt
    pip install -r requirements/client.txt

    

# Testing

    python manage.py test dj_six.perf



# Server deploy

## Local test mode

With sqlite and gunicorn:

    gunicorn dj_six.wsgi



# Client usage

Benchmarking the API:

    python manage.py dj_six_bench --url=localhost:8000
