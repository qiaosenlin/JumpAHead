# Jumpahead Online
Online platform for JumpAhead program

## Local Development Setup:

### Make sure you have Python 3.7.x installed
Whatever the latest 3.7 version is should be fine.

### Set up a virutal environment (Optional, but recommended)
Using a virtual environment is beneficial for a variety of reasons, but primarily, it will create a separate python installation for you to use just for this project. This way, the requirements you install won't affect your OS's default python installation.

Note: This is for MacOS & Linux. I'm not sure what the workflow looks like on PC

1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html): `pip install virtualenvwrapper`
2. Add the following to your shell startup file:
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```
3. Create a python 3.7 virtualenv: `mkvirtualenv jumpahead --python=python3`
Use `workon jumpahead` to activate your virtual environment, `deactivate` to deactivate

### Make sure you have `pg_config` installed
- On Mac run `brew install postgresql`
- On Ubuntu run `sudo apt-get install libpq-dev`

### Clone the repo and install requirements
1. `git clone https://github.com/ethanifenwick/JumpAhead.git
2. `cd jumpahead && pip install -r requirements.txt`
3. `pip install --upgrade django-crispy-forms`

### Set up environment variables
In order to keep the database url and secret key secure, we abstract those values into environment variables. Locally, these will be stored in a file called `.env`. On heroku, they are stored in the `config vars` setting.

1. Create env file: `touch .env`
2. In `.env`, add the `SECRET_KEY` and `DATABASE_URL` from heroku -> jumpahead -> settings -> config vars -> reveal config vars. Also, set `DEBUG=True`
```
SECRET_KEY= ...
DEBUG=True
DATABASE_URL= ...
```

### Run the local dev server
1. In the root of this repo with your virtual environment active, run `python manage.py runserver` 
2. Navigate to [127.0.0.1:8000]() in the browser


### How to clear and seed the database ***Do not clear the Database unless absolutely sure OR save the database on Heroku before you clear it***
1. Navigate to the project directory and run `python manage.py dbshell`
2. Inside the pqsl shell run `truncate modules_course cascade;`
3. Type `\q` and press enter to quit the shell
4. Then run `python manage.py loaddata seedData.json` to seed the database


### Final Requirements
Logic
- Basic Permissions (have to be logged in to view pages)
- Progress Bar Logic
  - Task/Module Logic
  - Progress based of User

Pages
- Base File - Header and Footer
- Module List Page
- Module Page (Details of module and interactions)
  - Progress Bar
