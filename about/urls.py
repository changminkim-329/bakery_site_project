from django.urls import path
from .views import about_staff, about_bakery, AboutStaffView

urlpatterns = [
    path('staff/', AboutStaffView.as_view()),
    path('bakery/', about_bakery)
]