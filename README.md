<p align="center">
  <h2 align="center"> Learn-Django <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"></h2> 
</p>

- #### [Django Documentation](https://docs.djangoproject.com/en/5.0/)

- **Django** : Python based Server Side Web framework
- **Web FrameWork** : Collections of Modules, Packages and librarues designed to speed up depelopment process.
- Django follow MVT architectural pattern.
- **MVC** = View <> Controller <> Model
  - **View (The Customer Who Order food) :** It displays the data to the user and sends user actions to the controller for processing.
  - **Controller(The Waiter) :** Acts as an intermediary between the Model and the View. It processes user requests, retrieves data from the Model, and updates the View accordingly. It handles user input and updates the model and view accordingly.
  - **Model(The chef) :** It manages the data, responds to queries, and interacts with the database. Handles database operations such as CRUD (Create, Read, Update, Delete) operations. Make the receipe for View(Customer based on their requirement) via contoller.
- **MVT** = Template <> View <> Model
  - **Template :** Handles the presentation layer. It consists of HTML files with Django template language (DTL) syntax that allows embedding Python-like code to dynamically generate content based on data from the Model. These templates represent the user interface and are responsible for rendering the final HTML output.
  - **View (Act as a Controller in MVC):** Handles the user requests and business logic. It receives HTTP requests, processes them, interacts with the Model to retrieve or modify data, and then returns HTTP responses. **Despite being called "views" in Django, they function more like controllers in the MVC pattern.**
  - **Model** : Same As MVC
  - **MVC vs MVT** : https://medium.com/dsc-umit/mvc-vs-mvt-architectural-pattern-d306a56dce55

## 1. Setting Environment

- Create Virtual Environment : `python3 -m venv environment_name`
- Activate The Environmet : `source environment_name/bin/activate`
- Install Django : `pip install django`
- Check version: `django-admin --version`
- Available Django Subcommand :`django-admin`
- Create Project : `django-admin startproject project_name`
- Check the tree structure and run the server : `python manage.py runserver`
- Create App : `python manage.py startapp app_name`

#### Project vs App

What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website.
**_A project can contain multiple apps. An app can be in multiple projects._**

**Project : Common files**
StudyHub = Outer Project Folder / Root Directory
StudyHub > StudyHub = Inner Project Folder / Default Application
StudyHub > StudyHub > asgi.py 
StudyHub > StudyHub > __init__.py 
StudyHub > StudyHub > settings.py 
StudyHub > StudyHub > urls.py 
StudyHub > StudyHub > wsgi.py
StudyHub > manage.py

**__init__ .py**
The folder which contains __init__.py is considered as pyhon package. If I want to create StudyHub as a python package, this file tells Python that the directory should be treated as a package and allows you to organize your code into logical modules and sub-packages.

**settings .py**
This file contains all the information or data about project settings. Example: Database congf information, Template, Installed Apps , Validators etc.

**urls .py**
This file contains information of  all url attached with application.

**manage .py**
A command-line utility that lets you interact with this Django project in various ways . [More details](https://docs.djangoproject.com/en/5.0/ref/django-admin/).

**ASGI and WSGI**
ASGI (Asynchronous Server Gateway Interface) and WSGI (Web Server Gateway Interface) are both specifications that define **how web servers communicate with web applications**, but they serve different purposes and are used in different contexts within the Django framework.

**WSGI (Web Server Gateway Interface):**
- WSGI is a standard interface between web servers and Python web applications or frameworks like Django.
- It's synchronous, meaning that each request is processed one after the other in a blocking manner.
- Handles one request at a time.
- Blocks the server until the processing of one request is completed.
- WSGI is used with traditional synchronous web servers.
- In Django, WSGI is used primarily for **deploying** Django applications on traditional web servers.

**ASGI (Asynchronous Server Gateway Interface):**
- ASGI is an asynchronous version of WSGI, designed to support asynchronous web frameworks and applications.
- It allows for handling long-lived connections, WebSockets, and other asynchronous operations.
- Allows parallel processing of multiple requests at a time.
- Does not block the server
- ASGI is used with asynchronous web servers and frameworks like Django Channels, which enable handling of real-time applications, chat systems, and other asynchronous features.

**When use what?**
In Simple Terms:
- Both ASGI (Asynchronous Server Gateway Interface) and WSGI (Web Server Gateway Interface) are related to deploying web applications in Python, but they serve different purposes and are used in different contexts.
- If your app is like a regular store: Use WSGI. Customers come in, buy things one at a time, and leave.
- If your app is like a bustling marketplace: Use ASGI. Lots of people are doing different things all at once, like browsing, buying, and chatting with vendors.


So, if your application needs to handle real-time interactions or multiple tasks simultaneously, choose ASGI. If it's a more traditional web application where tasks can be handled one at a time, WSGI is sufficient.

When run the project by  python manage.py runserver; StudyHub/__pycache__ : Create the cache files for the project to load the project faster.


**App : Common files**

```
__init__.py
admin.py
apps.py
models.py
tests.py
views.py
urls.py
```

## 2. view and urls

```
App/views > all logic/function
App/urls < import views
Root Directory/urls < include('App.urls')
```

## 3. Templates

- templates inheritance
- Variables : surrounded by {{ and }}
- Dictionary lookup :
  - {{ my_dict.key }}
  - {{ my_object.attribute }}
  - {{ my_list.0 }}
- Tags : Tags are surrounded by {% csrf_token %} \
   _provide arbitrary logic in the rendering process.This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags._

## 4. Admin

#### Create Super User

```
python manage.py createsuperuser
```

## 5. Database

**Initial Migration:** When you first create a Django app or define models within an existing app, you need to create an initial migration. This is done using the makemigrations command: python manage.py makemigrations . This command generates migration files in your app's migrations directory, which describe the changes to your models.

`python manage.py makemigrations`

**Applying Migrations:** After creating migration files, you can apply them to the database using the migrate command: python manage.py migrate. This command executes the migration files in the order they were created, updating the database schema accordingly.

`python manage.py migrate`

**Database Sync:** migrate not only creates new tables but also updates existing ones to match the current state of your models. It handles tasks such as creating or deleting columns, changing field types, and creating indexes.

**Database Schema Management:** Django tracks which migrations have been applied to the database in a special table called django_migrations. This table keeps a record of the migrations that have been executed, preventing them from being applied more than once.
