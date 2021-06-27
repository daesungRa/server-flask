FROM server-nginx:21.06.1
MAINTAINER Ra Daesung "daesungra@gmail.com"

### Write commands for flask docker image ###
# Make a default config and Deploy server source
RUN mkdir -p /serve/server-flask

WORKDIR /serve/server-flask
COPY . /serve/server-flask/

# Set pip virtual environment
RUN pip install --upgrade pip virtualenv
RUN virtualenv venv && \
    . ./venv/bin/activate && \
    pip install -r requirements.txt

# Default commands to be executed when instance starts
# CMD /bin/sh /serve/server-flask/run_app.sh

