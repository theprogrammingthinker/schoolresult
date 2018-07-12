"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from results.views import Homepage
#from django.contrib.auth import views as auth_views

from django.contrib.auth import authenticate, login as LoginView
from django.contrib.auth import authenticate, login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Homepage.as_view(), name=''),
    path('results/', include('results.urls')),
    path('login/', login, name='login'),
    
]


school_name = 'Fulhata Secondary School'

# default: "Django Administration"
admin.site.site_header = school_name+' Admin Panel'
# default: "Site administration"
admin.site.index_title = school_name+' Administration '
admin.site.site_title = school_name+' adminsitration'
