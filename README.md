# code

To Setup, Run <br>
Note: This web application will not run on windows as it uses 
py-utility library and py-utility does support windows.
<pre><code>git clone https://github.com/Vipul-Cariappa/code.git
cd code
python3 -m venv venv
source venv/bin/activate  # linux
pip install django django-crispy-forms py-utility
cd coder
python manage.py makemigrations challenge
python manage.py migrate
python manage.py runserver
</code></pre>

Go to 127.0.0.1:8000 to access the site.
