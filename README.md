# local_library_website

## Abstract

1. For Doing Django Tutorial: The Local Library website steps by steps.
    * [source codes](https://github.com/mdn/django-locallibrary-tutorial/tree/main)
2. Extend and prepare My skills to find some good web-backend/devops/architecture jobs.
3. Practice system architecture design.
4. Try RDBMS(Relational Database Management System):　SQLite, PostgreSQL



## Prerequisites

* Python == 3.8.16
* [pyenv+poetry](https://github.com/hong539/setup_dev_environment/blob/main/programing_languages/python/python.md)
* Project dependcy detialls will be in pyproject.toml/poetry.lock
* PostgreSQL == 15.3 or Django builtin SQLite
    * [pacman directly install PostgreSQL on Arch Linux](https://wiki.archlinux.org/title/PostgreSQL)
    * [PostgreSQL 15.4 Documentation](https://www.postgresql.org/docs/15/index.html)
    * [PostgreSQL with docker](https://hub.docker.com/_/postgres)
* tree
    * a CLI tools to list contents of directories in a tree-like format.

## To-do-list and troubleshooting

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
* [~~Django Tutorial Part 9: Working with forms~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)
    * [django_form_handling_process](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#django_form_handling_process)
    * [renew-book_form_using_a_form_and_function_view](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#renew-book_form_using_a_form_and_function_view)
    * [Testing the page](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#testing_the_page_2)
    * [challenge_yourself](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms#challenge_yourself)
    * decimalfield
    * [How to create custom model fields](https://docs.djangoproject.com/en/4.2/howto/custom-model-fields/)
        * [writing-a-field-subclass](https://docs.djangoproject.com/en/4.2/howto/custom-model-fields/#writing-a-field-subclass)
    * INTEGER
        * [Django/models/fields/IntegerField](https://docs.djangoproject.com/en/4.2/ref/models/fields/#integerfield)
    * [VARCHAR](https://docs.aws.amazon.com/redshift/latest/dg/r_Character_types.html#r_Character_types-varchar-or-character-varying)
    * [year-field-in-django](https://stackoverflow.com/questions/49051017/year-field-in-django)

```Python
#src: https://docs.djangoproject.com/en/4.2/ref/models/fields/#decimalfield
#Add IntegerField with "YYYY" year format
    year_of_birth = models.IntegerField(null=True, blank=True)
    year_of_death = models.IntegerField(null=True, blank=True)
```
* [~~Django Tutorial Part 10: Testing a Django web application~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
    * [challenge_yourself](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#challenge_yourself)
        * [src:test_views.py](https://github.com/mdn/django-locallibrary-tutorial/blob/main/catalog/tests/test_views.py)
    * [LocalLibrary tests](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#locallibrary_tests)
        * [ImportError: 'tests' module incorrectly imported from 'somepath/locallibrary/catalog/tests'. Expected 'somepath/locallibrary/catalog'. Is this module globally installed?](https://ithelp.ithome.com.tw/articles/10276107)
            * filename "test.py" and module directory name "tests" 
            * change the duplicate filename or remove it
        * execute "python3 manage.py test"
            * psycopg.errors.CannotCoerce: cannot cast type date to integer
                * [django.db.utils.ProgrammingError: cannot cast type integer to date](https://stackoverflow.com/questions/72459658/django-db-utils-programmingerror-cannot-cast-type-integer-to-date)
            * psycopg.errors.UndefinedTable: relation "auth_user" does not exist
                * [psycopg.errors.UndefinedTable: relation "auth_user" does not exist](https://stackoverflow.com/questions/72096130/getting-programmingerror-relation-auth-user-does-not-exist-while-running-test)
            * Solution: Reset/Remove Migrations files under catalog module and don't forget our "\_\_init\_\_.py" file                
                * [Python/modules/\_\_init\_\_.py](https://docs.python.org/3.8/tutorial/modules.html)  
    * [types_of_testing](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#types_of_testing)
        * Unit tests/Regression tests/Integration tests...etc
        * [Python/module-unittest](https://docs.python.org/3/library/unittest.html#module-unittest)
        * [liveservertestcase](https://docs.djangoproject.com/en/4.2/topics/testing/tools/#liveservertestcase)
        * [using-different-testing-frameworks](https://docs.djangoproject.com/en/4.2/topics/testing/advanced/#using-different-testing-frameworks)
        * [test_structure_overview](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing#test_structure_overview)
        ```shell
        tree .
        #structure
        .
        ├── __init__.py
        ├── test_forms.py
        ├── test_models.py
        └── test_views.py
        ```              
* [Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)    
    * [Getting your website ready to publish](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment#getting_your_website_ready_to_publish)
    * [Deployment checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
    * deploy via docekr/podman conainter
* [web_application_security](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/web_application_security)
* [Assessment: DIY Django mini blog](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog)
* Relational Database Management System (RDBMS) and Object Relational Mapping (ORM) part:
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

## Quick Start

```shell
#check out prerequisites to prepare your environment

#setting up for start postgresql on every bootup
sudo systemctl enable postgresql.service

#running postgresql server with this commands
#if everything is setting up!
sudo systemctl status postgresql.service

#spawns a virtual environment
poetry shell

#add packages
poetry add django
poetry add diagrams

#for help
python3 manage.py help

#Creating a superuser for Django CMS system
python3 manage.py createsuperuser

#run devserver
python3 manage.py runserver

#Warning: You'll need to run these commands every time your models change in a way that will affect the structure of the data that needs to be stored (including both addition and removal of whole models and individual fields).
python3 manage.py makemigrations
python3 manage.py migrate

#run test
python3 manage.py test
#Showing more test information
python3 manage.py test --verbosity 2
#Speeding things up
python3 manage.py test --parallel auto
#Running specific tests
python3 manage.py test catalog.tests.test_models
python3 manage.py test catalog.tests.test_views
python3 manage.py test catalog.tests.test_forms


#Starts the Python interactive interpreter
python3 manage.py shell

#src: https://docs.python.org/3.8/library/sys.html#sys.path
#A list of strings that specifies the search path for modules. 
#Initialized from the environment variable PYTHONPATH, plus an installation-dependent default.
python -c "import sys; print(sys.path)"

#add env PYTHONPATH
export PYTHONPATH=/path/to/your/module:$PYTHONPATH

#add packages by poetry
poetry add "psycopg[binary,pool]"

#deploy check
python3 manage.py check --deploy
```

## Others

* [flake8](https://flake8.pycqa.org/en/latest/)
* [pandas](https://github.com/pandas-dev/pandas)
* [gunicorn](https://github.com/benoitc/gunicorn)
* [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
* [distrochooser](https://distrochooser.de/)
    * [Dockerfile example from distrochooser](https://github.com/distrochooser/distrochooser/blob/master/backend/Dockerfile)
    * Vue
    * Django
* [How to deploy with WSGI](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/)
* [PEP 3333 – Python Web Server Gateway Interface(WSGI)](https://peps.python.org/pep-3333/)
* [Python/load test/locust](https://docs.locust.io/en/stable/quickstart.html)
* [Scaffold_(programming)](https://en.wikipedia.org/wiki/Scaffold_(programming))
* [django-roadmap](https://github.com/HHHMHA/django-roadmap)
* [nodejs](https://nodejs.org/en)
* [expressjs](https://expressjs.com/)
* [react](https://react.dev/)
* [Vue.js](https://vuejs.org/)
* [tailwindcss](https://tailwindcss.com/)
* [Diagrams](https://diagrams.mingrammer.com/)
    * Diagram as Code
    * architecture design
* [Django plugins/packages](https://djangopackages.org/)
    * [markdown](https://pypi.org/project/Markdown/)
    * [django-markdownify](https://pypi.org/project/django-markdownify/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Django REST framework（DRF）](https://www.django-rest-framework.org/)
