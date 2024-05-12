from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('my_works/', views.my_works_view, name='my_works'),
    path('hire_me/', views.hire_me_view, name='hire_me'),
    path('about/', views.about_view, name='about'),
    path('web_development/', views.web_development_view, name='web_development'),
    path('web_design/', views.web_design_view, name='web_design'),
    path('python_programming/', views.python_programming_view, name='python_programming'),
]
