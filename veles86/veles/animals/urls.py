from django.urls import path
from animals import views
#from django.contrib.auth import views as auth_views
from .views import (DogCreateView, DogDetailView, DogListView, DogTableView,
                    DogUpdateView, HealthUpdateView, DiseaseCreateView,
                    Adress_FindCreateView, Adress_OwnerCreateView, DogImageUpdateView,
                    PostCreateView, MessageCreateView, MessageView, MessageDeleteView,
                    PostListView )


urlpatterns = [
    path('', views.index, name = 'index'),
    path('animals/', views.animals, name = 'animals'),
    path('dog_read/<int:pk>', views.DogReadView.as_view(), name='read_dog'),
    path('dogs_create/', DogCreateView.as_view(), name='dog_create'),#ссылка на создание новости
    path('dog_list/<int:pk>', DogDetailView.as_view(), name='dog_list'),#ссылка на создание новости
    path("admin_panel/", DogListView.as_view(), name='admin_panel'),
    path("admin_panel2/", DogTableView.as_view(), name='admin_panel2'),
    path('dog_update/<int:pk>', DogUpdateView.as_view(), name='dog_update'),
    path('health_update/<int:pk>', HealthUpdateView.as_view(), name='health_update'),
    path('disease_create/<int:pk>', DiseaseCreateView.as_view(), name='disease_create'),
    path('adress_find_create/<int:pk>', Adress_FindCreateView.as_view(), name='adress_f_create'),
    path('adress_owner_create/<int:pk>', Adress_OwnerCreateView.as_view(), name='adress_o_create'),
    path('foto_dog_update/<int:pk>', DogImageUpdateView.as_view(), name='foto_dog_update'),
    path('post_create/', PostCreateView.as_view(), name='post_create'),
    path('message_create/', MessageCreateView.as_view(), name='message_create'),
    path('message_view/', MessageView.as_view(), name='message_view'),
    path('message_delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('post_list/', PostListView.as_view(), name='post_list'),

]