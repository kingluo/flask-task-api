# task api demo

## Install requirements

```
pip install flask pytest
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

```
./tasks.sh add "hello world" "02/08/2011"
./tasks.sh list --expiring-today
./tasks.sh list
./tasks.sh done 1
```
