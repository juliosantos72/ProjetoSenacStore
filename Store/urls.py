
from django.urls import path
from Store import views
urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.teste, name='teste')
]
