# Rescue Maps
We here at Rescue Maps strive to help those caught in distress situations by creating a network of organizations and people who can share their resources in their proximity for the needy, thus speeding up the overall process of disaster relief


## Getting Started
Clone the repository into your system by browsing to [this repository](https://www.github.com/deveshd2k/weather)
...

### Prerequisites
```
Django 2.1
Postgresql
Python
```


### Installing

1. To install Postgresql
```
   $ sudo apt-get update
   $ sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql contrib
```


2. Log into an interactive Postgres session by typing:
```
$ sudo -u postgres psql
```


3. Create DATABASE using
```
postgres=# CREATE DATABASE flood_data;
```


4. Next, we will create a database user which we will use to connect to and interact with the database.
```
postgres=# CREATE USER flood_user WITH PASSWORD 'Aezakmicar1';
```


5. To connect with the Postgresql database, follow this [guide](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04) here



6. For python 3, install virtual environment using
```
sudo pip3 install virtualenv
```


7. Move into the directory of the cloned django project
```
 cd ~/(project_name)
```


8. create a virtual environment to store our Django project's Python requirements by typing:
```
$ virtualenv myprojectenv
```


9. Activate virtual environment using
```
$ source myprojectenv/bin/activate
```


10. you can install Django with pip
```
$ pip3 install django
```


11. Install the psycopg2 package
```
$ pip install django psycopg2
```


## Starting the project

1. Browse to the directory of the project in your terminal

2. Now you're good to go, fire up the application from 
```
python manage.py runserver
```

## Built With


## Contributing

## Acknowledgements
