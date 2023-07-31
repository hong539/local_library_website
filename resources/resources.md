# resources

## install/configure PostgreSQL on Arch Linux

* [PostgreSQL via docker container](https://github.com/docker-library/docs/blob/master/postgres/README.md)
* [install PostgreSQL on Arch Linux](https://wiki.archlinux.org/title/PostgreSQL)
* [PostgreSQL/Chapter 19. Server Setup and Operation](https://www.postgresql.org/docs/15/runtime.html)
* [PostgreSQL/app-createuser](https://www.postgresql.org/docs/current/app-createuser.html)
* [Django/PostgreSQL connection settings](https://docs.djangoproject.com/en/4.2/ref/databases/)
* [PostgreSQL/auth-pg-hba-conf](https://www.postgresql.org/docs/15/auth-pg-hba-conf.html)
* How to import file db.sqlite3 to Postgresql?

```shell
#install postgresql via pacman
sudo pacman -S postgresql

#change user to postgres for setting up PostgreSQL on Arch Linux
sudo -iu postgres

#check encoding
echo $LANG
locale -a

#init data
initdb -D /var/lib/postgres/data

#status your PostgreSQL server
sudo systemctl status postgresql.service
#start your PostgreSQL server
sudo systemctl start postgresql.service
#stop your PostgreSQL server
sudo systemctl stop postgresql.service

#Create your first database/user
createuser --interactive
#Which user to use createdb myDatabaseName?
createdb local_library

#test db
psql local_library

#Configure PostgreSQL server
sudo vim /var/lib/postgres/data/postgresql.conf
sudo vim /var/lib/postgres/data/pg_hba.conf
sudo systemctl restart postgresql.service

#Configure User for PostgreSQL server
sudo -u postgres psql
\du

#change exist USER with pwd 'new_password'
#add password for user via commands
sudo -u postgres psql
ALTER USER username WITH PASSWORD 'new_password';

#add attribute "CREATEDB" for exist user
ALTER USER username CREATEDB;

#could not save history to file "/var/lib/postgres/.psql_history": No such file or directory
sudo mkdir /var/lib/postgres
sudo touch /var/lib/postgres/.psql_history
sudo chown postgres:postgres /var/lib/postgres/.psql_history

#How to import file db.sqlite3 to Postgresql?
sqlite3 db.sqlite3 .dump > db.sql
```

## Tips

* [Running the website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website#running_the_website)