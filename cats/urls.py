from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "cats"
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),

    path('main/create_breed/', views.BreedCreate.as_view(), name='breed_create'),
    path('main/view_breeds', views.BreedList.as_view(), name='all_breeds'),
    path('main/<int:pk>/update_breed/', views.BreedUpdate.as_view(), name='breed_update'),
    path('main/<int:pk>/delete_breed/', views.BreedDelete.as_view(), name='breed_delete'),
]
