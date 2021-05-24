"""
# Installation

1. vagrant up
2. vagrant ssh
3. cd /vagrant
4. python -m venv ./env
5. source ./env/bin/activate
6. in (env), touch requirements.txt, insert two line: django==2.2, djangorestframework==3.9.2
7. pip install -r requirements.txt
8. django-admin.py startproject profiles_project .
9. python manage.py startapp profiles_api
10. add installed_apps into INSTALLED_APPS of settings.py

# Account SUPERUSER
trung.beno149@gmail.com
trung1409

# Register model to the admin site
Example: admin.site.register(UserProfile)
"""