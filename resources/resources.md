# resources

## What to do?

~~* [Django Tutorial: The Local Library website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)~~
~~* [Django Tutorial Part 2: Creating a skeleton website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)~~
~~* [Django Tutorial Part 3: Using models](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)~~
~~* [Django Tutorial Part 4: Django admin site](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)~~
~~* [Django Tutorial Part 5: Creating our home page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)~~
    * [creating_the_index_page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page#creating_the_index_page)
* [Django Tutorial Part 6: Generic list and detail views](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
    * Challenge yourself
* [Django Tutorial Part 7: Sessions framework](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions)
* [Django Tutorial Part 8: User authentication and permissions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication)
* [Django Tutorial Part 9: Working with forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
* [Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
* [Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

## install PostgreSQL on Arch Linux

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

#Configure User for PostgreSQL server
sudo -u postgres psql
\du

#change exist USER with pwd 'new_password'
sudo -u postgres psql
ALTER USER username WITH PASSWORD 'new_password';

#add attribute "CREATEDB" for exist user
ALTER USER username CREATEDB;
```

## Tips

* [Running the website](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website#running_the_website)