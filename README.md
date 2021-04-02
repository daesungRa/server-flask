# My Flask

My Flask is based on the [Flask](https://github.com/pallets/flask) project owned by [pallets team](https://github.com/pallets).
This is to provide a quick start to the Flask web application.

**Anyone can modify and distribute this project.**

## Structure

- DEFAULT:
    - **_app_** with api, db
    - **_conf.d/_** << **_config.py_** for configuration
    - Run at once with **_run_app.sh_** using _gunicorn_, _gevent worker_

- ADDS-ON:  <small># in _app/\_\_init\_\_.py_</small>
    - Project logger
    - Blueprint APIs
    - Error pages

## Installation

> At least python ```version 3.6``` or higher is recommended.

> Clone this github project to your desktop root path.

```shell
/project/root/path $ pip install -U virtualenv
/project/root/path $ virtualenv venv
/project/root/path $ . ./venv/bin/activate
(venv) /project/root/path $ pip install -r requirements.txt
```

## Configuration

1. You can change the application name **by changing _app/_**

2. Add **yaml file** to _conf.d/_
    - Change sample file's app name in _conf.d/_
    - Copy and paste the sample file to create a yaml file > _conf.d/\[NEW_APP\].yaml_
    - Setting project variables in yaml file

3. Enabling **CONFIG variable in _config.py_** and Insert APP_NAME to config path

## When you start this app

#### Run as development mode

```shell
(venv) /project/root/path $ FLASK_DEBUG=1 flask run
```

#### Run as production

```shell
/project/root/path $ sh run_app.sh
```

## Activate pytest

```shell
(venv) /project/root/path $ ptw  // pytest-watch
```

## Version info

| Tool | Description | Version |
|:--|:--|:--|
| Python | Main lang | 3.6 |

