# local_library_website

For Doing Django Tutorial: The Local Library website steps by steps

## prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* Project dependcy detialls will be in pyproject.toml/poetry.lock
* PostgreSQL or builtin SQLite
    * [PostgreSQL via docker container](https://github.com/docker-library/docs/blob/master/postgres/README.md)
    * [install PostgreSQL on Arch Linux](https://wiki.archlinux.org/title/PostgreSQL)
    * [PostgreSQL/Chapter 19. Server Setup and Operation](https://www.postgresql.org/docs/15/runtime.html)
    * [PostgreSQL/app-createuser](https://www.postgresql.org/docs/current/app-createuser.html)
    * [Django/PostgreSQL connection settings](https://docs.djangoproject.com/en/4.2/ref/databases/)
    * [PostgreSQL/auth-pg-hba-conf](https://www.postgresql.org/docs/15/auth-pg-hba-conf.html)

```shell
#install postgresql via pacman
sudo pacman -S postgresql

#change user to postgres for setting up PostgreSQL on Arch Linux
sudo -iu postgres

#check encoding
[postgres]$ echo $LANG
[postgres]$ locale -a

#init data
[postgres]$ initdb -D /var/lib/postgres/data

#status your PostgreSQL server
sudo systemctl status postgresql.service
#start your PostgreSQL server
sudo systemctl start postgresql.service
#stop your PostgreSQL server
sudo systemctl stop postgresql.service

#Create your first database/user
[postgres]$ createuser --interactive
#Which user to use createdb myDatabaseName?
createdb local_library

#test db
psql local_library

#Configure PostgreSQL server
sudo vim /var/lib/postgres/data/postgresql.conf
sudo vim /var/lib/postgres/data/pg_hba.conf
sudo systemctl restart postgresql.service
```

## to-do-list

* ~~fix this error : django.db.utils.OperationalError: no such table: catalog_book~~
    * [reinstall-the-db-sqlite3-file-in-django](https://stackoverflow.com/questions/64808378/how-do-i-reinstall-the-db-sqlite3-file-in-django)
* change to another separate DB such as PostgreSQL
    * FATAL:  password authentication failed for user
    * [postgresql-notes](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)
    * [QuerySet API](https://docs.djangoproject.com/en/4.2/ref/models/querysets/)
    * [libpq](https://www.postgresql.org/docs/current/libpq.html)

## quick start

```shell
#check out prerequisites to prepare your environment

#for help
python3 manage.py help

#Creating a superuser for Django CMS system
python3 manage.py createsuperuser

#run devserver
python3 manage.py runserver

#Warning: You'll need to run these commands every time your models change in a way that will affect the structure of the data that needs to be stored (including both addition and removal of whole models and individual fields).
python3 manage.py makemigrations
python3 manage.py migrate
```