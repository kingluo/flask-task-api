# task api demo

This server program uses flask library to define RESTful APIs
and jinja2 library to render the http response.
The tasks is stored in a global dictionary.
Each new task gets id from an incremental id counter.
The RESTful API uses task id in url to identify the task.

The cli shell script `tasks.sh` uses curl program to access the APIs.

Start the flask server and run cli shell script to do operations.

## Install requirements

Require python >= 2.8.

```
pip install -r requirements.txt
```

## Start flask server

```
./start_flask.sh
```

## test

```
pytest
```

## cli

* add task

`./task.sh add <desc> <expiring date>`

* update task

`./task.sh set <id> <desc> <expiring date>`

* get task by id

`./task.sh get <id>`

* get all tasks

`./task.sh list`

* get all tasks expired today

`./task.sh list --expiring-today`

* delete task

`./tasks.sh done <id>`

Examples:

```
./tasks.sh add "hello world" "02/08/2011"
./tasks.sh set 1 "hello world" "02/08/2011"
./tasks.sh get 1
./tasks.sh list --expiring-today
./tasks.sh list
./tasks.sh done 1
```
