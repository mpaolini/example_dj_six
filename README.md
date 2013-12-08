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

    
## AWS Elasicbeanstalk

Download and install `eb` utility http://aws.amazon.com/code/6752709412171743

Optional: Configure PATH reading `README.TXT`

Initialize eb environment (XXX):

    eb init
    git checkout -- .gitignore
    git checkout -- .elasticbeanstalk/config

Store credentials in `.secrets`

    mkdir .secrets

Get credentials from passpack (copy into clipboard)

    xsel -b > .secrets/aws_credentials

Test setup:

    eb status


# Testing

    python manage.py test dj_six.perf


## Heroku

1) install heroku CLI
2) login to heroku from the CLI
3) configure git:

    heroku git:remote -a djsix


## Activate developer environment

    source activate.sh



# Server deploy

## Local test mode

Initialize db:

    python manage.py syncdb

Run with gunicorn:

    gunicorn -w 10 dj_six.wsgi

Run with uWSGI:

    uwsgi -p 10 --http-socket localhost:8000 -w dj_six.wsgi


## AWS

XXX this needs to be fixeed a bit

1) Create elasticbeanstalk app with `eb start`
2) set environment variables (XXX)


Deploy to elasticbeanstalk:

    git aws.push

Access via ssh:

- create a `djsix` keypair from EC2 aws console
- copy `djsix.pem` in `.secrets/`
- change permission:

    chmod og-rwx .secrets/djsix.pem

- ssh -i .secrets/djsix.pem <server-name>


To access django shell:

    source /opt/python/run/venv/bin/activate && source /opt/python/current/env &&  cd /opt/python/current/app
    python manage.py shell_plus

Also try:

    elastic-beanstalk-describe-configuration-settings -a djsix -e djsix-env -j

**NOTE** check RDS set security groups (open inbound port to beanstalk security group)


## Heroku

### Initial setup (altready done by marco)

    heroku apps:create djsix --region=eu
    heroku addons:add heroku-postgresql:dev --app djsix
    heroku config:add DJANGO_SETTINGS_MODULE=dj_six.settings.heroku
    heroku run python manage.py syncdb --noinput -a djsix

### Deploy code

    git push djsix master



# Client usage

Benchmarking the API:

    python manage.py dj_six_bench --host=localhost:8000
