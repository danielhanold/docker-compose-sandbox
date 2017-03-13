 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /config  
 RUN mkdir /code
 WORKDIR /code
 ADD ./config/requirements.txt /config/
 RUN pip install -r /config/requirements.txt
 ADD ./src /code/
