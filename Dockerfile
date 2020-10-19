FROM base:20.10.1
MAINTAINER Ra Daesung "daesungra@gmail.com"

### Write commands for flask docker image ###
RUN mkdir -p /serve/server-flask

WORKDIR /serve/server-flask

COPY . /serve/server-flask/

RUN pip install --upgrade pip virtualenv
RUN virtualenv venv && \
    . ./venv/bin/activate && \
    pip install -r requirements.txt

CMD /bin/sh /serve/server-flask/run_app.sh

EXPOSE 8000
