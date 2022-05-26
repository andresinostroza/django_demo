## I am docker friendly :D let's keep it easy :D

### initial setup


Create a .env file in the root, follow the instructions of =>  https://docs.docker.com/compose/environment-variables/#the-env-file for example:

DJANGO_SUPERUSER_EMAIL=<your-admin-email>
DJANGO_SUPERUSER_PASSWORD=<your-admin-password>

This is necessary in order to create new users and organizations using the admin django CRUD
### run docker build and run in detached mode using our lovely

```
docker-compose up -d

```

### setup new users or organizations in case you need

goto in your browser:

http://0.0.0.0:8090/admin/


### check the API docs

goto in your browser:

http://0.0.0.0:8090/
