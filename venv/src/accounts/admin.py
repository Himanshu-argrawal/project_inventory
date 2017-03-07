from django.contrib import admin
from .models import User
# Register your models here.


class accountsAdmin(admin.ModelAdmin):
    list_display = ["first_name","username", "email"]
    list_filter = ['username' , 'email']
    search_fields = ['email','username']
    class Meta:
        model = User

admin.site.register(User , accountsAdmin)