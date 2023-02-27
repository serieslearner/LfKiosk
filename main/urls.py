from django.urls import include, path
from .views import *
from . import views


app_name = 'LfKiosk'

urlpatterns = [

    path('process_photo', views.process_photo, name='process_photo'),
    path('male_30/', views.male_30_view, name='male_30_view'),
    path('male_40/', views.male_40_view, name='male_40_view'),
    path('female_30/', views.female_30_view, name='female_30_view'),
    path('female_40/', views.female_40_view, name='female_40_view'),
        path('', views.index, name='index'),
]
