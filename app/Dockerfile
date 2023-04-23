FROM python:3.8.8-buster
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

ENV PYTHONPYCACHEPREFIX=/root/pycache

WORKDIR /root/opt
COPY . .

ENV HOST db
ENV DBNAME todoproject
ENV USERNAME rustrust
ENV PASSWORD rustrust

RUN apt-get install -y vim less sqlite3
RUN pip install --upgrade pip setuptools --user
RUN pip install -r requirements.txt

EXPOSE 80

CMD [ "python", "main.py" ]
