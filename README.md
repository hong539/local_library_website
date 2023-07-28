# local_library_website

For Doing Django Tutorial: The Local Library website steps by steps

## prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* PostgreSQL or builtin SQLite

## to-do

* fix dependency error : django.db.utils.OperationalError: no such table: catalog_book

## quick start

```shell
#check out prerequisites to prepare your environment

#for help
python3 manage.py help

#run devserver
python3 manage.py runserver

#Warning: You'll need to run these commands every time your models change in a way that will affect the structure of the data that needs to be stored (including both addition and removal of whole models and individual fields).
python3 manage.py makemigrations
python3 manage.py migrate
```