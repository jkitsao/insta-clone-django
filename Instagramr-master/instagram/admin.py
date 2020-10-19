from .models import Profile, Image, Followers, Like
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Followers)
admin.site.register(Like)
