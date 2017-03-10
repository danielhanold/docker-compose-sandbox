FROM python:3.6

ENV PYTHONUNBUFFERED 1


# based on python:2.7-onbuild, but if we use that image directly
# the above apt-get line runs too late.
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

ADD . /code/
