from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Django's ORM simplifies the process of interacting with databases in web applications by providing a high-level abstraction layer that allows developers to work with Python objects instead of dealing with raw SQL querie.

# - Allow us to access the database in a Object oriented way
# - Represent the database structure as classes  and those classes called method
# - Each class represent a table in the database
# - Each attribute of the class represent a field in the table
# - Each instance of the class represent a row in the table
# - make migrations after modify models.py
# - have a look on SQL code that will be migrate => python manage.py sqlmigrate BlogApp 0001 

# - query database on shell => python manage.py shell
# - from BlogApp.models import Post
# -  from django.contrib.auth.models import User
# - User.objects.all()
# - User.objects.first()
# - User.objects.filter(username='Username')

# - Dunder __str__ method
# - special query set of user model
# - from view import the Post model
# - Register the Post model in the admin panel
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

"""
load data by using the shell
python manage.py shell
from BlogApp.models import Post

with open('posts.json') as f:
    posts_json = json.load(f)

for post in posts:
    Post.objects.create(title=post['title'], content=post['content'], author_id=post['user_id'])

Post pagination
from django.core.paginator import Paginator
posts = ['1', '2', '3', '4', '5']
p = Paginator(posts, 5)
p.num_pages

"""