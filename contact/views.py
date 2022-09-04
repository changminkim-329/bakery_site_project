from urllib import request
from django.shortcuts import render,redirect
from django.views import View
from user.models import User
from .models import Receipt
# Create your views here.

class Contact(View):
    def get(self, request):
        try:
            print(request.session['id'])
            user_object = User.objects.get(email=request.session['id'])
            username = user_object.username
            email = user_object.email
            contact_number = user_object.contact_number

            context = {}
            context["username"] = username
            context["email"] = email
            context["contact_number"] = contact_number

            return render(request, "contact.html",context)

        except Exception as e:
            print("오류:",e)
            return redirect("/login")


    def post(self, request):
        try:
            post_data = request.POST
            email = post_data['email']
            contact_number = post_data['contact-number']
            message = post_data['message']

            receipt_object = Receipt(
                user = User.objects.get(email=request.session['id']),
                email = email,
                contact_number = contact_number,
                message = message,
            )
            receipt_object.save()

            return redirect("/")

        except Exception as e:
            print("오류: ",e)
            return redirect("/contact")
