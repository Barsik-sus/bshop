from django.urls import path

from .views import *

urlpatterns = [
    path('login/', loginView, name='login'),
    path('sign-up/', sign_upView, name='sign_up'),
    path('loguot/', logoutView, name='logout'),
]