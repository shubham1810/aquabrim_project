pinax-project-account
=====================

In addition to what is provided by the "zero" project, this project provides
thorough integration with django-user-accounts, adding comprehensive account
management functionality. It is a foundation suitable for most sites that have
user accounts.

=====================================
to access the main web app on the link provided, use the following usernames and passwords:

username : user
password : user
=====================================


Usage:

    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master <project_name>


Getting Started:

    pip install virtualenv
    virtualenv mysiteenv
    source mysiteenv/bin/activate
    pip install Django==1.6.5
    django-admin.py startproject --template=https://github.com/pinax/pinax-project-account/zipball/master mysite
    cd mysite
    pip install -r requirements.txt
    python manage.py syncdb
    python manage.py runserver
