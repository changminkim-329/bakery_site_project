from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('login/',LoginView.as_view()),
    path('logout',logout),
    path('useredit',useredit)
]