from django.contrib import admin
# here we need to register our model to admin 

# Register your models here.
from .models import Article

admin.site.register(Article)