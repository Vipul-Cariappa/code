# code

To Setup, Run <br>

<pre><code>git clone https://github.com/Vipul-Cariappa/code.git
cd code
python3 -m venv venv
source venv/bin/activate  # linux
venv\scripts\activate     # windows
pip install django django-crispy-forms py-utility django-cors-headers
cd coder
python manage.py makemigrations challenge
python manage.py migrate
python manage.py runserver
</code></pre>

Go to http://127.0.0.1:8000/ to access the site.
