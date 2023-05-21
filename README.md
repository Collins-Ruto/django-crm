# Django CRM app
This is a CRM app developed using django and mysql database

## Methods

To start the app, run:

```
python manage.py runserver
# starts the django app

python manage.py tailwind install
# installs all required dependencies for styling with tailwind css

python manage.py tailwind start
# runs watch command to compile scss files into static / tailwind folder
```

## Setup mysql

To setup my sql database, I used the digitalOcean's  [How To Install MySQL on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-22-04)

Make models migrations

```
python manage.py makemigrations
```

Push migrations to database

```
python manage.py migrate
```

## Tailwind CSS installation

Styling on this django app was done using Tailwind CSS.  
The tutorial and procedure used can be found at [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) and can be supplemented with [Django Tailwind Setup Made Easy](https://blog.devgenius.io/django-tailwind-setup-made-easy-36043adda97c)
