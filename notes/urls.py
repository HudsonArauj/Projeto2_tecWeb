from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='destroy'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),
    path('tags', views.tags, name='tags'),
    path('tagSelect/<str:tag>', views.tagSelect, name='tagSelect'),

    path('home', views.index, name='home'),



]