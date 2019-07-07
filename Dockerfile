FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /cyg
WORKDIR /cyg
ADD requirements.txt /cyg/
RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /cyg/
RUN apt-get update