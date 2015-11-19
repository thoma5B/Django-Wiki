## Installation


Start virtualenvironment and install Python packages

```
mkdir venv
virtualenv venv/Dj1.8
source venv/Dj1.8/bin/activate

pip install -r requirements.pip
```


Make database (by now sqlite) ready

```
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
```

To test with the python development server:

`python manage.py runserver`


## Production setup

- set `DEBUG = False` in the file `project/settings.py`

For production run the uwsgi-server together with nginx

`uwsgi uwsgi.ini`

and 

`ln -s /full/path/to/Django-Wiki/nginx.conf /etc/nginx/sites-enabled/djangowiki.conf`

and then

`service nginx reload`

or

`/etc/init.d/nginx reload`





The wiki is cloned from

https://github.com/django-wiki/django-wiki.git

on Nov 19th which is under [GPUv3](LICENSE.md)
