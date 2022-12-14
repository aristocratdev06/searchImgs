from django.shortcuts import render, reverse, redirect
from .models import *
from .form import *
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.views import get_user_model


def home(request):
    imges = Post.objects.all()
    context ={
        "imgpost": imges
        }
    return render(request, 'home.html',context)

def results(request):
    serfun = request.GET.get("search", "")
    if serfun and serfun != "":
        img = Post.objects.filter(img_title__contains=serfun).all()
    else:
        img = ''

    context = {
        "video": img,
        "value": serfun
    }

    return render(request, "results.html", context)


class Signup(generic.CreateView):
    template_name = 'registration/signup.html'
    form_class = SignUp

    def get_success_url(self):
        return reverse("login")


class Profile(generic.TemplateView):
    template_name = "profile/profile.html"


class Edit_profile(generic.UpdateView):
    form_class = User_change
    template_name = "profile/edit_profile.html"
    success_url = reverse_lazy('app:profile')
    def get_object(self):
        return self.request.user


class NewPostView(generic.CreateView):
    template_name = "newpost.html"
    form_class = NewPostForm
    def get_success_url(self):
        return reverse("app:home")



def public_profile(request, pk):
    user = MyUser.objects.get(username=pk)
    context = {
        'user': user
    }
    return render(request, 'profile/public.html', context)


def handler400(request, exception):
    return render(request, 'helpers/404.html',  status=404)

def handler500(request, *args, **argv):
    return render(request, 'pages/helpers/500tml')

User = get_user_model()

def users(request):
    usersnum = User.objects.count()
    users = User.objects.all()
    context = {
        "usersnum":usersnum,
        "users":users
    }

    return render(request, "user.html", context)
