from django.urls import path
from users.views import get_user, inicio

urlpatterns = [
    path('usuario/', get_user, name='user'),
    path('cliente/', inicio, name='inicio'),
]