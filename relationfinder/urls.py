from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.login_or_register, name='login_or_register'),
    path('logout', views.logoutUser, name='logout'),
    path('create', views.create, name='create'),
    path('update_card/<str:pk>', views.update_card, name='update_card'),
    path('delete_card/<str:pk>', views.delete_card, name='delete_card'),
    path('savedata', views.save_form_data, name='savedata'),
    path('similarities', views.similarities, name='similarities'),
    path('mycards', views.mycards, name='mycards'),
    path('messages', views.messages, name='messages'),
    path('user/<str:pk>', views.get_user, name='user'),
    path('viewcard/<str:pk>', views.viewcard, name='viewcard'),
    path('dialogue/<str:pk>', views.dialogue, name='dialogue'),
    path('usersearch', views.usersearch, name='usersearch'),
    path('profile', views.profile, name='profile'),
    path('settings', views.profilesettings, name='profilesettings'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)