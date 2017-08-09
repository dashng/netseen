# netseen

## quick start


### manage.py

Before start, please set environment `DATABASE_URL`, or it will use sqlite by default.

```sh
$ pip install -r requirements.txt
$ python manage.py createdb
$ python manage.py create_admin
$ python manage.py runserver
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 330-625-128
```

### docker-compose

First, please install `docker-compose`, then

```sh
$ docker-compose build -f docker-compose.yml
$ docker-compose up -f docker-compose.yml
```

Running on http://127.0.0.1:8080
