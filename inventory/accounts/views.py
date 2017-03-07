from django.shortcuts import render , render_to_response ,redirect , reverse,get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate , logout , login
from django.views.generic import ListView , View ,DeleteView ,CreateView ,RedirectView , DetailView
from .models import User
from .forms import Register_form , Register_formTwo ,LoginForm

# Create your views here.
class Register(View):
    def get(self , request):
        user = request.user
        form = Register_form()
        return render(request ,'index.html',{'form':form})
    def post(self , request):
        form = Register_form(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/accounts/steptwo/%s'%(user.id))
        return render(request , 'index.html' , {"form":form})

def registertwo(request , id= None):
    instance = get_object_or_404(User , id=id)
    user = request.user
    form =Register_formTwo(request.POST or None , request.FILES or None , instance =instance)
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form":form,
    }
    return render(request , "registertwo.html" , context)

class RegisterTwo(LoginRequiredMixin , View):
    def get(self , request):
        user = request.user
        form = Register_formTwo(request.POST or None)
        context = {
    "form":form
        }
        return render(request , 'registertwo.html', context)
    def post(self,request):
        user = request.user

class Login(View):

    def get(self, request):
        user = request.user
        if user.is_authenticated():
            return redirect('/accounts/steptwo/%s'%(user.id))
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('/accounts/steptwo/%s'%(user.id)))

            else:
                return redirect('/accounts/login')

        return render(request, 'login.html', {'form': form})

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/accounts/login/')