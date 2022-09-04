from django.urls import path
from .views import product_list, ProductListView

urlpatterns = [
    path("list/",ProductListView.as_view())
]