from flask import Flask, request
from dataclasses import dataclass
from datetime import date, datetime
from jinja2 import Template
import logging


@dataclass
class Task:
    id: int
    expire: date
    desc: str


tasks_template = (
    "{% for task in tasks -%}"
    "{{ '{:<4}'.format(task.id) }} {{ task.expire }} {{ task.desc }}"
    "{% endfor -%}")

tasks_template = Template(tasks_template)

logging.basicConfig(
    filename="task.log",
    filemode='w',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG)

app = Flask(__name__)

tasks = {}
next_task_id = 1

text_plain_content_type = {'Content-Type': 'text/plain; charset=utf-8'}


@app.post("/task")
def task_post():
    global tasks, next_task_id
    try:
        data = request.form
        desc = data["desc"]
        expire = data["expire"]
        expire = datetime.strptime(expire, '%d/%m/%Y').date()
        task = Task(id=next_task_id, expire=expire, desc=desc)
        tasks[task.id] = task
        next_task_id += 1
        logging.info("create task: %s", task)
        return tasks_template.render(
            tasks=[task]), 201, text_plain_content_type
    except KeyError:
        return "desc and expire must be provided", 400
    except ValueError:
        return "expire: invalid date format, should be %d/%m/%y", 400


@app.get("/tasks")
def task_get_all(task_id=None):
    global tasks
    expiring_today = request.args.get("expiring_today")
    if expiring_today:
        expiring_today = expiring_today.lower() == "true"
    if expiring_today:
        today = datetime.now().date()
        task_list = [task for task in tasks.values() if task.expire <= today]
        logging.info("get all tasks expired today")
    else:
        task_list = list(tasks.values())
        logging.info("get all tasks")
    return tasks_template.render(tasks=task_list), text_plain_content_type


@app.get("/task/<int:task_id>")
def task_get(task_id=None):
    global tasks
    try:
        task = tasks[task_id]
        logging.info("get task: %s", task)
        return tasks_template.render(tasks=[task]), text_plain_content_type
    except KeyError:
        return "task not found", 404


@app.put("/task/<int:task_id>")
def task_put(task_id):
    global tasks
    try:
        task = tasks[task_id]
        data = request.form
        desc = data.get("desc")
        if desc:
            task.desc = desc
        expire = data.get("expire")
        if expire:
            expire = datetime.strptime(expire, '%d/%m/%Y').date()
            task.expire = expire
        logging.info("update task: %s", task)
        return tasks_template.render(
            tasks=[task]), 201, text_plain_content_type
    except KeyError:
        return "task not found", 404
    except ValueError:
        return "expire: invalid date format, should be %d/%m/%y", 400


@app.delete("/task/<int:task_id>")
def task_delete(task_id):
    global tasks
    try:
        task = tasks[task_id]
        logging.info("delete task: %s", task)
        del tasks[task_id]
        return "", 204
    except KeyError:
        return "task not found", 404
