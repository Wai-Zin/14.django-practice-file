"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include

from sample_app import views

from sample_app import views_calendar


from sample_app import views_404

from template_app import views_template

from template_app import views_tvariable

from template_app import views_ttagsif

from template_app import views_ttagsfor

from template_app import views_ttable

from template_app import views_ttagsblock

from template_app import views_ttagsextends

from template_app import views_ttagsinclude




urlpatterns = [
    path('admin/', admin.site.urls),

    path('helloworld/', views.helloworld),
    path('calendar/', views_calendar.index),
    path('404/', views_404.index),
    path('1_index_template/', views_template.index),
    path('2_index_tvariable/', views_tvariable.index),
    path('3_index_ttagsif/', views_ttagsif.index),
    path('4_index_ttagsfor/', views_ttagsfor.index),
    path('5_index_ttable/', views_ttable.index),
    path('6_index_ttagsblock/', views_ttagsblock.index),
    path('7_index_ttagsextends/', views_ttagsextends.index),
    path('8_index_ttagsinclude/',views_ttagsinclude.index),

    path('url_app/', include('url_app.urls')),
    path('html_form_app/', include('html_form_app.urls')),
    path('model_form_app/', include('model_form_app.urls'))



    #path(domain/ , file_name.function_name)
]
