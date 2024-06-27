from django.contrib import admin
from .models import Userdetails, User
# Register your models here.
class userdetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'email', 'contact', 'quotes')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 1
    list_editable = ("contact",)

admin.site.register(Userdetails, userdetailsAdmin)
admin.site.register(User)