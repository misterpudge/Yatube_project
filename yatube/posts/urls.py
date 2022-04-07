from django.urls import path

from . import views

app_name = 'publications'

urlpatterns = [
    path('', views.index, name='main'),
    path('group/<slug:pk>/', views.group_posts, name='groups')
]
