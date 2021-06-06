"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse,HttpRequest

def dev(request):
    HTML = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>1.Dasturlash tillari quyidagilardir.</h1>
        <ol type="1" start="10">
        <li>C++</li> 
        <li>Paskal</li> 
        <li>Java</li>    
        <li>Python</li>  
        </ol>
        <h2>2.Matn muharrirlari quyidagilardir.</h2>
        <ol type="I" start="15">
            <li>MS Word</li>
            <li>WordAD</li>
            <li>Notepad</li>
            <li>Sublime</li>
        </ol>
    </body>
    </html>
    '''
    return HttpResponse(HTML)

def home(request):
    home_page = '<h1 align="center">HOME PAGE</h1>'
    return HttpResponse(home_page)

def sum(request):
    print(request.GET.get('a'))
    return HttpResponse('<h1 align="center">SUM</h1>')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/',dev),
    path('',home),
    path('sum/',sum)
]
