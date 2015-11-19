## Installation


make database (by now sqlite) ready

```
python manage.py syncdb
python manage.py makemigrations
python manage.py migrate
```

To test with the python development server:

`python manage.py runserver`


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
