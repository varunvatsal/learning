from django.urls import path
from . import views
app_name = 'first_app'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/first_year/', views.first_year, name='first_year'),
    path('home/second_year/', views.second_year, name='second_year'),
    path('home/third_year/', views.third_year, name='third_year'),
    path('home/fourth_year/', views.fourth_year, name='fourth_year'),
    path('home/teach/', views.teach, name='teach' ),
    path('home/about/', views.about, name='about'),
]