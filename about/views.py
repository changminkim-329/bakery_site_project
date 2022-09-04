from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Staff
# Create your views here.

def about_staff(request):
    return render(request,"about_staff.html")

class AboutStaffView(ListView):
    template_name = "about_staff.html"
    model = Staff
    context_object_name = "staffs"


def about_bakery(request):
    return render(request, "about_bakery.html")