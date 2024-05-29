# Create Virtual Environment (VEnv)
C:\> python -m venv myenv

# Activate Virtual Environment
C:\>  myenv\Scripts\activate

# Upgrade pip
(myenv) C:/> python -m pip install --upgrade pip

# Install Django modules
(myenv) C:/> python -m pip install Django

# Creating Django Project
(myenv) C:/> django-admin startproject cart

# Open Project Folder
(myenv) C:/> cd cart

# Run Project
(myenv) C:/cart> python manage.py runserver

# File upload support
(myenv) C:/cart> pip install pillow

settings.py
=============
# Setting default static directory
STATICFILES_DIRS = [BASE_DIR / "static"]
# File uploads
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

urls.py (Project main urls file/default urls.py)
================================================
from django.contrib import admin
from django.urls import path

# For File upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

# For File upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# Encrypt Password

from django.conf import settings
settings.configure()
print(settings.PASSWORD_HASHERS)

copy paste the printed hashes to settings.py
===========================================
PASSWORD_HASHERS = [
    #paste here
]


To get installed packages from current project
===============================================
pip freeze > requirements.txt

To install packages to copied project
===============================================
pip install -r requirements.txt


To Check Password correct or not from python prompt
===================================================

from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
settings.configure()

check_password('your password','password hash copied from admin panel')

#will show true if password is correct