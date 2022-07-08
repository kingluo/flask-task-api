#!/usr/bin/bash

case $1 in
    add)
        curl --request POST -s --header 'Content-Type: application/x-www-form-urlencoded' --data-urlencode "desc=$2" --data-urlencode "expire=$3" 'http://127.0.0.1:5000/task'
        ;;
    done)
        curl --request DELETE -s "http://127.0.0.1:5000/task/$2"
        ;;
    list)
        if [[ $2 == "--expiring-today" ]]; then
            curl --request GET -s 'http://127.0.0.1:5000/tasks?expiring_today=true'
        else
            curl --request GET -s 'http://127.0.0.1:5000/tasks'
        fi
        ;;
esac
