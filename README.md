# DjangoPratice

python -m venv .venv
source  .venv/bin/activate
pip install django 
pip freeze  >requirements.txt
django-admin  startproject projectname
cd ..project name
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

// manage image 
// setting
import os

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]

//  static urls links in urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

// app create krne ke leye 
pythone manage.py startapp tweet

sbsbe phloe urls.py file bna lege 

views.py me file bna lege 

setting ko btyege new aap tweet leye

// templates ke leye 
   'DIRS': [os.path.join(BASE_DIR,'templates')],

// tweet me templates ka folder bna lege 
usme index.html 

urls.py main project ko inform krge app ke leye 
from django.urls import path ,include
 path('tweet/', include('tweet.urls')),

// models ke leye //
from django.contrib.auth.models import user


🫖 Chai or Code — Django + Tailwind Project
A simple Django web app demonstrating a Chai (tea) variety catalog built using Django, Tailwind CSS, and SQLite. This app showcases the power of full-stack development using Python and modern frontend styling.

📌 Features
🔍 List of Chai varieties with images and types

📝 Detail page for each Chai item

🎨 Styled with Tailwind CSS

🚀 Live reloading with django-browser-reload

🗂 Media file handling for Chai images

🔧 Admin panel support

🧑‍💻 Tech Stack
Backend: Django 4.2.23

Frontend: Tailwind CSS

Database: SQLite

Tools: django-tailwind, django-browser-reload

📷 Screenshots
(Add screenshots here if available, or you can upload later.)

🚀 Installation & Setup
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/your-username/chai-or-code.git
cd chai-or-code/Django

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Tailwind setup
cd theme
npm install
cd ..

# 5. Apply migrations
python3 manage.py makemigrations
python3 manage.py migrate

# 6. Run the server
python3 manage.py runserver
📁 Folder Structure (Simplified)
php
Copy
Edit
Django/
├── chai/              # App for chai variety logic
├── theme/             # Tailwind CSS app
├── templates/         # HTML templates
├── static/            # Static files
├── manage.py
├── db.sqlite3
└── djangopratice/     # Main project folder
⚙️ Environment Variables (optional)
You may add a .env file to store secret keys and environment-specific settings.

✅ Usage
Visit http://127.0.0.1:8000/chai/ to view all chai varieties

Click on any chai to view detailed info

Admin panel: http://127.0.0.1:8000/admin/

🧑‍🎓 Author
Lokesh Yadav
Full Stack Web Developer — MERN & Django
LinkedIn  = https://www.linkedin.com/in/lokesh-yadav-4507b0277/
Email =lokeshydv5526@gmail.com


