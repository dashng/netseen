netseen
=======

|Python Version| |License| |Build Status| |Test Coverage|

A basic REST API server which could provide layer 2 topology data.

quick start
-----------


manage.py
^^^^^^^^^

Before start, please set environment ``DATABASE_URL``, or it will use sqlite by default.

.. code-block:: bash

    $ pip install -r requirements.txt
    $ python manage.py createdb
    $ python manage.py create_admin
    $ python manage.py runserver
        * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        * Restarting with stat
        * Debugger is active!
        * Debugger PIN: 330-625-128


docker-compose
^^^^^^^^^^^^^^

First, please install ``docker-compose``, then

.. code-block:: bash

    $ docker-compose build -f docker-compose.yml
    $ docker-compose up -f docker-compose.yml


Running on http://127.0.0.1:8080


.. |Python Version| image:: https://img.shields.io/pypi/pyversions/Django.svg
    :target: https://github.com/ciscochina/netseen

.. |License| image:: https://img.shields.io/hexpm/l/plug.svg
   :target: https://github.com/ciscochina/netseen/blob/master/LICENSE

.. |Build Status| image:: https://travis-ci.org/ciscochina/netseen.svg?branch=master
   :target: https://travis-ci.org/ciscochina/netseen

.. |Test Coverage| image:: https://coveralls.io/repos/ciscochina/netseen/badge.svg?branch=master
   :target: https://coveralls.io/r/ciscochina/netseen
   