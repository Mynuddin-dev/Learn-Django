<p align="center">
  <h2 align="center"> Learn-Django <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28"></h2> 
</p>


## 1. Setting Environment
- Create Virtual Environment : ```python3 -m venv environment_name```
- Activate The Environmet : ``` source environment_name/bin/activate```
- Install Django : ```pip install django```
- Check version: ```django-admin --version ```
- Create Project : ``` django-admin startproject project_name```
- Check the tree structure and run the server : ```python manage.py runserver```
- Create App : ```python manage.py startapp app_name```
#### Project vs App
What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

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
## 2. Routes
```
App/views > all logic/function
App/urls < import views
Project/urls < include('App.urls')
```
## 3. Templates
- templates inheritance
- Variables : surrounded by {{ and }} 
- Dictionary lookup : 
    - {{ my_dict.key }}
    - {{ my_object.attribute }}
    - {{ my_list.0 }}
    
- Tags : Tags are surrounded by {% and %} \
    *provide arbitrary logic in the rendering process.This definition is deliberately vague. For example, a tag can output content, serve as a control structure e.g. an “if” statement or a “for” loop, grab content from a database, or even enable access to other template tags.*
