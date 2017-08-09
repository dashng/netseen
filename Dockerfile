FROM python:3.5
MAINTAINER Peng Xiao <xiaoquwl@gmail.com>

COPY ./netseen /netseen/netseen
ADD ./gunicorn.sh /netseen
ADD ./requirements.txt /netseen
ADD ./manage.py /netseen

WORKDIR /netseen

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN chmod +x gunicorn.sh

CMD ["./gunicorn.sh"]