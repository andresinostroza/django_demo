# Iconic chain -Task

## For local development with no Docker with virtual env

### Install Python 3.8.X

User the link 

https://www.python.org/downloads/release/python-3813/

### Create your virutal environment 

```
python -m venv env
```

### Access to your virutal environment 


```
source env/bin/activate  
```

### Install dependencies

```
pip install -r requirements.txt
```


### Run initial setup
```
python manage.py makemigrations api
python manage.py migrate  
python manage.py loaddata organization
python manage.py createsuperuser --email <choose a root email> --password <choose your password>
```

### Run the app

```
python manage.py runserver

```

## For local development with Docker

### Coming soon