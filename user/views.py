from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from .models import User

# Create your views here.
from .forms import LoginForm, UserEditForm
def index(request):
    return render(request, "index.html")


# def login(request):
#     print(request.session["id"])
#     return render(request,"login.html")


class LoginView(FormView):
    success_url = "/"
    template_name = "login.html"
    form_class = LoginForm

    def get(self, request):
        try:
            self.request.session["id"] != None
            return redirect("/")

        except Exception as e:
            return super().get(self, request)

    def form_valid(self, form):
        print("세션",form.data.get('email'))
        self.request.session['id'] = form.data.get('email')
        return super().form_valid(form)


def logout(request):
    try:
        request.session['id']
        request.session.flush()
        return render(request,"logout.html")

    except:
        return redirect("/")


def useredit(request):
    if(request.method == "GET"):
        context = {}
        try:
            user_object = User.objects.get(email = request.session['id'])

            context['username'] = user_object.username
            context['gender'] = user_object.gender
            print(user_object.gender)
            context['contact_number'] = user_object.contact_number
            context['address'] = user_object.address
            return render(request, "useredit.html",context)

        except Exception as e:
            return redirect("/login") 

    if(request.method == "POST"):
        print(request.POST)
        username = request.POST.get('username')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact-number')
        address = request.POST.get('address')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        
        user_object = User.objects.get(email = request.session['id'])

        if(password == re_password):

            try:
                user_object.username = username
                user_object.gender = gender
                user_object.contact_contact_number =contact_number
                user_object.address = address
                user_object.password = password

                user_object.save()

                return redirect("/")

            except Exception as e:
                print("오류:",e)
                return redirect("/useredit")

        else:
            return redirect("/useredit")

# class UserEditView(FormView):
#     form_class = UserEditForm
#     success_url = "/"
#     template_name = "useredit.html"

#     def form_valid(self, form):
#         try:
#             user_object = User.objects.get(email = self.request.session.get('email'))

#             print(user_object.username)
#             print(user_object.password)
#             print(user_object.contact_number)
#             print(user_object.gender)
#             print(user_object.address)

#             return super().form_valid(form)
            

#         except Exception as e:
#             print("오류",e)
#             return super().form_valid(form)


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['user_model'] = User.objects.get(email=self.request.session.get('id'))
#         print("컨텍스트:",context)

#         return context 



    