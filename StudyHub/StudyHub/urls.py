"""
URL configuration for StudyHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

When to use include()?
    You should always use include() when you include other URL patterns. admin.site.urls is the only exception to this

    """
from django.contrib import admin
from django.urls import path , include

# if the project is big there are may be lots of views and urls here and they messy up the code. 
# so we can import views from the app and use them here(This is the purpose of apps in django)
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Home Page')

# def rooms(request):
#     return HttpResponse('Rooms Page')

from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    path('api/', include('Base.api.urls')),

]

urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
