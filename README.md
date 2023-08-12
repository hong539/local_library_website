# local_library_website

For Doing Django Tutorial: The Local Library website steps by steps

* [source codes](https://github.com/mdn/django-locallibrary-tutorial/tree/main)

## prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* Project dependcy detialls will be in pyproject.toml/poetry.lock
* PostgreSQL or builtin SQLite
* tree
    * a CLI tools to list contents of directories in a tree-like format.

## to-do-list and troubleshooting

* [~~Django Tutorial: The Local Library website~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Tutorial_local_library_website)
* [~~Django Tutorial Part 2: Creating a skeleton website~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website)
* [~~Django Tutorial Part 3: Using models~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models)
* [~~Django Tutorial Part 4: Django admin site~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site)
* [~~Django Tutorial Part 5: Creating our home page~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page)
    * [~~creating_the_index_page~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page#creating_the_index_page)
    * [static-files](https://docs.djangoproject.com/en/4.2/howto/static-files/)
* [~~Django Tutorial Part 6: Generic list and detail views~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views)
    * ~~Challenge yourself~~
    * [author_list.html](https://github.com/mdn/django-locallibrary-tutorial/blob/main/catalog/templates/catalog/author_list.html)
    * Multi Authors own one book. How to change it to work?
* [~~Django Tutorial Part 7: Sessions framework~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions)
    * [How to use sessions](https://docs.djangoproject.com/en/4.2/topics/http/sessions/)
* [~~Django Tutorial Part 8: User authentication and permissions~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication)
    * [permissions](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication#permissions)
* [Django Tutorial Part 9: Working with forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
    * [django_form_handling_process](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#django_form_handling_process)
    * [renew-book_form_using_a_form_and_function_view](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#renew-book_form_using_a_form_and_function_view)
* [Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
* [Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
* ~~fix this error : django.db.utils.OperationalError: no such table: catalog_book~~
    * [reinstall-the-db-sqlite3-file-in-django](https://stackoverflow.com/questions/64808378/how-do-i-reinstall-the-db-sqlite3-file-in-django)
* change to another separate DB such as PostgreSQL
    * WARNING: password file ".my_pgpass" has group or world access; permissions should be u=rw (0600) or less
    * django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table (permission denied for schema public
LINE 1: CREATE TABLE "django_migrations" ("id" bigint NOT NULL PRIMA...
        
        * [create-table-django-migrations-id-bigint-not-null-prima](https://stackoverflow.com/questions/74217259/create-table-django-migrations-id-bigint-not-null-prima)
        ```shell      
        ALTER DATABASE <db_name> OWNER TO <db_user>;
        ```
    
    * django.db.utils.OperationalError: connection is bad: definition of service "my_service" not found
        * [34.17. The Connection Service File](https://www.postgresql.org/docs/15/libpq-pgservice.html)
        * [Trouble hooking up postgres to django](https://stackoverflow.com/questions/71337173/django-4-connection-to-postgresql-using-passfile-fe-sendauth-no-password-supp)
    * ~~django.core.exceptions.ImproperlyConfigured: Error loading psycopg2 or psycopg module~~
        ```shell
        poetry add "psycopg[binary,pool]"
        ```
    * [How do I reinstall the db.sqlite3 file in django](https://stackoverflow.com/questions/64808378/how-do-i-reinstall-the-db-sqlite3-file-in-django)
    * ~~could not save history to file "/var/lib/postgres/.psql_history": No such file or directory~~
        * touch file and chown user/usergroup
    * ~~FATAL:  password authentication failed for user~~
        * add password for user via commands
    * [psycopg3: an engine for postgresql](https://www.psycopg.org/psycopg3/docs/basic/install.html#supported-systems)
    * [SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.](https://www.sqlalchemy.org/)
    * [postgresql-notes](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)    
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

#add packages by poetry
poetry add "psycopg[binary,pool]"
```