# task api demo

This server program uses flask library to define RESTful APIs
and jinja2 library to render the http response.
The tasks are stored in a global dictionary variable.
Each new task gets id from an incremental integer variable.
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
bash start_flask.sh
```

## test

```
pytest
```

## cli

* add task

`bash task.sh add <desc> <expiring date>`

* update task

`bash task.sh set <id> <desc> <expiring date>`

* get task by id

`bash task.sh get <id>`

* get all tasks

`bash task.sh list`

* get all tasks expired today

`bash task.sh list --expiring-today`

* delete task

`bash tasks.sh done <id>`

Examples:

```
bash tasks.sh add "hello world" "02/08/2011"
bash tasks.sh set 1 "hello world" "02/08/2011"
bash tasks.sh get 1
bash tasks.sh list --expiring-today
bash tasks.sh list
bash tasks.sh done 1
```
