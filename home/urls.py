from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('logout', do_logout),
    path('signup', signup),
    path('signin', do_login)
]
