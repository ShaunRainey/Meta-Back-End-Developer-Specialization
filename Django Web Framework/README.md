Steps to access Django project:

1) Enter correct directory:
    - Meta-Back-End-Developer-Specialization\Django Web Framework
2) Ensure env file exists:
    - pip install virtualenv
    - python3 -m venv env (could also just use 'python' depending on version)
3) Activate venv:
    - .\env\Scripts\activate
4) Enter project directory:
    - Meta-Back-End-Developer-Specialization\Django Web Framework\testProject
5) Run server:
    - python manage.py runserver

Notes:
When using urls, make sure there is a '/' on the end when required. Otherwise error 404

Steps to make a Template:

1) Create template folder in project base directory (should be on the same level as app)
2) Create template.html files and populate
3) In Settings.py, within 'TEMPLATES = [.....] change DIRS to ['templates']
4) Create a view using 'return render(request, 'page.html', {dictionary})'
