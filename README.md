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

**Project : Common files**

```
__init__.py
asgi.py
wsgi.py
setting.py
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
