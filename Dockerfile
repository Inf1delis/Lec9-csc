FROM python:3

RUN pip3 install flask

RUN pip3 install redis

RUN pip3 install pymongo

COPY ./task2/main.py /

COPY ./task2/storage.py /

COPY ./task2/loggin.conf /

COPY ./task2/mylog.log /

EXPOSE 5000

ENTRYPOINT ["python", "main.py"]

