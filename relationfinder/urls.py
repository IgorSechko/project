from django.urls import path, include

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('create/', views.create, name='create'),
    path('profile/', views.profile, name='profile'),
    path('savedata/', views.save_form_data, name='savedata'),
    path('', include("django.contrib.auth.urls")),
    path('', include("frontend.urls")),
    # path('formcreation', views.create_form),
]