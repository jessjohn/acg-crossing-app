# acg-crossing-app
ACG Crossing Guard App (RHoK #11)

### Basic Run Instructions for now

You'll need to install
- django
- python3
- pip

Make sure to install pip *after* you install python3

```bash
cd /<path-to-code>/acg-crossing-app/ACGCrossingApp/
pipenv install
pipenv shell
python manage.py runserver
```

# Postgres setup, what we know so far
We're working off of local postgres for now.
The defaults configured are to use the database `crosswatch` with username:password `crosswatch:crosswatch`.

To set up the user in postgres:
Get into the postgres shell with
```
sudo -u postgres psql
```
And run the following to set up the database and db user.
```
CREATE USER crosswatch WITH PASSWORD 'crosswatch'; CREATE DATABASE crosswatch WITH OWNER crosswatch;
```

# Setting up the admin user
You can set up an admin user with: 
```
python manage.py createsuperuser
```

To access the admin page via `http://localhost:8000/admin/` assuming you're running on localhost and haven't changed the configured port.

# API DOCS
`/api/v1/users` 
GET - list the users resgistered

`/api/v1/rest-auth/login