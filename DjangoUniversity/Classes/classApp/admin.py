from django.contrib import admin

from .models import djangoClasses #importing the newly created class.

admin.site.register(djangoClasses) #registering the new class.