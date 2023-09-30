# resources

## notes when doing MDN Django Tutorial and any others

* Relational Database Management System (RDBMS) and Object Relational Mapping (ORM) part:
    * [postgresql-notes](https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes)    
    * ~~fix this error : django.db.utils.OperationalError: no such table: catalog_book~~
        * [reinstall-the-db-sqlite3-file-in-django](https://stackoverflow.com/questions/64808378/how-do-i-reinstall-the-db-sqlite3-file-in-django)
    * change to another separate DB such as PostgreSQL
    * WARNING: password file ".my_pgpass" has group or world access; permissions should be u=rw (0600) or less
    * django.db.migrations.exceptions.MigrationSchemaMissing: Unable to create the django_migrations table (permission denied for schema public...etc
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
    * [libpq](https://www.postgresql.org/docs/current/libpq.html)
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
* [~~Django Tutorial Part 11: Deploying Django to production~~](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)    
    * [Getting your website ready to publish](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment#getting_your_website_ready_to_publish)
    * [How to deploy Django](https://docs.djangoproject.com/en/4.2/howto/deployment/)    
    * [Deployment checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)    
    * deploy via docekr/podman conainter
        * [Publish Container Images to Docker Hub / Image registry with Podman](https://computingforgeeks.com/how-to-publish-docker-image-to-docker-hub-with-podman/)
        * [Use an access token](https://docs.docker.com/docker-hub/access-tokens/#use-an-access-token)
        * [How to manage Linux container registries](https://www.redhat.com/sysadmin/manage-container-registries)
        * [How To Deploy a Scalable and Secure Django Application with Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-scalable-and-secure-django-application-with-kubernetes)
        * [How to Build a Django and Gunicorn Application with Docker](https://www.digitalocean.com/community/tutorials/how-to-build-a-django-and-gunicorn-application-with-docker)
        * Dockerfile part for build docker images with this Django project via "podman build"
            * Update/Modify Dockerfile.dev and Dockerfile.prod
            * [--no-cache](https://github.com/containers/podman-compose/issues/205)            
            * [production-dockerfile](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/#production-dockerfile)
            * [Multi-stage builds](https://docs.docker.com/build/building/multi-stage/)
            * [What is the use of PYTHONUNBUFFERED in docker file?](https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file)
            * [PYTHONDONTWRITEBYTECODE](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDONTWRITEBYTECODE)
            * [PYTHONUNBUFFERED](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONUNBUFFERED)
            * [ENV PATH="${PATH}:/root/.local/bin"](https://github.com/python-poetry/poetry/issues/525)
            * podman run -d --env-file=.env.dev --name local_library -p 8000:8000 localhost/dev-test
                * django.core.exceptions.ImproperlyConfigured: Set the DB_USER environment variable
                * django.core.exceptions.DisallowedHost: Invalid HTTP_HOST header: 'x.x.x.x:8000'. You may need to add 'x.x.x.x' to ALLOWED_HOSTS.
                    * ALLOWED_HOSTS in settings.py
        * Container part
            * [why-it-is-recommended-to-run-only-one-process-in-a-container](https://devops.stackexchange.com/questions/447/why-it-is-recommended-to-run-only-one-process-in-a-container)
            * [containers-single-or-multiple-processes](https://www.tutorialworks.com/containers-single-or-multiple-processes/)
        * Update locallibrary/settings.py for reading env eaisly from file or runtime?
            * [django-environ](https://github.com/joke2k/django-environ)
                * [Path issues with read_env since 11.0+](https://github.com/joke2k/django-environ/issues/497)
                    * ~~rollback to version 0.10.0~~
                    * Setting Up Right PATH for BASE_DIR
            * Maybe yaml loader 
            * [os.path](https://docs.python.org/3.8/library/os.path.html)
            * [correspondence-to-tools-in-the-os-module](https://docs.python.org/3.8/library/pathlib.html#correspondence-to-tools-in-the-os-module)
            * [settings tips for Django](https://github.com/django/djangoproject.com/tree/main/djangoproject/settings)
            * [Configuring Django Settings: Best Practices](https://djangostars.com/blog/configuring-django-settings-best-practices/)
* [web_application_security](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/web_application_security)
* [Assessment: DIY Django mini blog](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/django_assessment_blog)

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
#Client authentication
sudo vim /var/lib/postgres/data/pg_hba.conf
sudo systemctl restart postgresql.service

#Configure User for PostgreSQL server
sudo -u postgres psql
\du

#Create your first database/user
createuser --interactive

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

## Others

* [CSRF (Cross-Site Request Forgery)](https://developer.mozilla.org/en-US/docs/Glossary/CSRF)
* Design parts
    * [The Twelve Factors](https://www.12factor.net/)
* Deployment parts    
    * [PEP 3333 – Python Web Server Gateway Interface(WSGI)](https://peps.python.org/pep-3333/)
    * [uWSGI 2.0 documentation](https://uwsgi-docs.readthedocs.io/en/latest/)
    * [How to deploy with WSGI](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/)
    * [gunicorn](https://github.com/benoitc/gunicorn)
    * [Werkzeug](https://werkzeug.palletsprojects.com/en/2.3.x/)
    * [tornado](https://github.com/tornadoweb/tornado)
    * [Docker Registry](https://docs.docker.com/registry/)
* Test parts
    * [Python/load test/locust](https://docs.locust.io/en/stable/quickstart.html)
    * [hey is a tiny program that sends some load to a web application.](https://github.com/rakyll/hey) 
* [restful-demo.pdf](https://github.com/TritonHo/slides/blob/master/restful-demo.pdf)
    * [RESTful API Design-tw-2.2.pdf](https://github.com/TritonHo/slides/blob/master/Taipei%202019-06%20talk/RESTful%20API%20Design-tw-2.2.pdf)
* [flake8](https://flake8.pycqa.org/en/latest/)
* [pandas](https://github.com/pandas-dev/pandas)
* [stable-diffusion-webui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
* [distrochooser](https://distrochooser.de/)
    * [Dockerfile example from distrochooser](https://github.com/distrochooser/distrochooser/blob/master/backend/Dockerfile)
    * Vue
    * Django
* [Scaffold_(programming)](https://en.wikipedia.org/wiki/Scaffold_(programming))
* javascript part
    * [nodejs](https://nodejs.org/en)
    * [expressjs](https://expressjs.com/)
    * [react](https://react.dev/)
    * [Vue.js](https://vuejs.org/)
    * [tailwindcss](https://tailwindcss.com/)
* [django-roadmap](https://github.com/HHHMHA/django-roadmap)
* [Diagrams](https://diagrams.mingrammer.com/)
    * Diagram as Code
    * architecture design
* [djangoproject.com/docker-entrypoint.sh](https://github.com/django/djangoproject.com/blob/main/docker-entrypoint.sh)
* [plugins/packages that can combine with Django projects](https://djangopackages.org/)
    * [markdown](https://pypi.org/project/Markdown/)
    * [django-markdownify](https://pypi.org/project/django-markdownify/)
    * [yaml](https://yaml.org/)
        * [PyYAML](https://pyyaml.org/)
    * [django-environ](https://github.com/joke2k/django-environ)
    * [python-dotenv](https://pypi.org/project/python-dotenv/)
* [uploadserver](https://pypi.org/project/uploadserver/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Django REST framework（DRF）](https://www.django-rest-framework.org/)
* Matrix digital rain
    * [Implementation of a Falling Matrix](https://www.geeksforgeeks.org/implementation-falling-matrix/)
    * [matrix-rain](https://github.com/flightcrank/matrix-rain)
* Python with Rust part
    * [Rust and Godot 3.2](https://hagsteel.com/posts/godot-rust/)
    * [The Rust Programming Language](https://doc.rust-lang.org/book/)