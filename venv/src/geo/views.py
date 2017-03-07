from django.shortcuts import render , render_to_response
from django.views.generic import VIew , TemplateView
from django.contrib.auth import authenticate, login, logout, get_user_model

class Register(VIew):
    def get(self):

