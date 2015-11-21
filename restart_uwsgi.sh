#! /bin/bash

source venv/Dj1.8/bin/activate
ps aux | grep  uwsgi | awk {'print $2'} | xargs kill
uwsgi uwsgi.ini &
