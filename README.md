# code
code is a web application where you can test your program solving skills. Create and upload your own programming questions and puzzles for others to solve. And get evaluated based on the memory and execution time.
<br><br>
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
python manage.py loaddata questions.json
python manage.py runserver
</code></pre>

Go to http://127.0.0.1:8000/ to access the site.
