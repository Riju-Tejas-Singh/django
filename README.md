http://127.0.0.1:8000/chatbot/start/ 
Chatbot Started!

Steps to start:
Download python version from web -> python3 --version will automatically point to that (Python 3.13.9)
python3 -m pip install --user pipenv

echo 'export PATH="$HOME/Library/Python/3.13/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

pipenv --version (check version)
pipenv install (create virtual env, similar to python3 -m venv .venv -> Installs whatever is already listed in the Pipfile, If no Pipfile exists, it simply creates one)
pipenv install django (install whatever you want)
pipenv shell (activate virtual env, similar to source .venv/bin/activate)

python3 manage.py runserver

Alternate:
python3 -m venv .venv
source .venv/bin/activate
pip install django (after activating venv to install within venv)
python3 manage.py runserver (django-admin runserver --pythonpath=. --settings=chatbot.settings)
deactivate (exit in above case to go back to global python env)

Git commands:
git config --global user.name "Riju"
git config --global user.email "yourmail@gmail.com"
git add .
git commit -m "learning-django"
git remote add origin https://github.com/Riju-Tejas-Singh/django.git
git remote -v (to check origin)
git push -u origin main

VsCode:
Cmd+Shift+P -> Preferences -> Settings(JSON) -> {"git.path": "/usr/bin/git"}

Working with Django:
Create Django Model in models.py of your class
python3 manage.py makemigrations ->prepares db changes in 0001_initial.py in /migrations
python3 manage.py migrate -> does db changes in db.sqlite3

admin.site.register(Product) in the admin.py to register model
python3 manage.py createsuperuser
http://127.0.0.1:8000/admin
login with superuser creds

serializer:
pip install djangorestframework
add to INSTALLED_APPS in settings.py -> 'rest_framework',

json from browser:
urlpatterns = format_suffix_patterns(urlpatterns) and format=None) in views
req-> http://127.0.0.1:8000/chatbot/products.json

