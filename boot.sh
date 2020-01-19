#!/bin/sh
source venv/bin/activate

while true; do
    sleep 5
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Upgrade command failed, retrying in 5 secs...
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app