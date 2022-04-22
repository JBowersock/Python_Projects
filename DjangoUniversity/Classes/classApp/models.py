from django.db import models

class djangoClasses(models.Model): #created a new class
    title = models.CharField(max_length=60, default="", null=False) #title w/charecter field, null means cant be empty.
    courseNumber = models.IntegerField() #integer field.
    instructorName = models.CharField(max_length=60, default="", null=False) #title w/charecter field, null means cant be empty.
    duration = models.FloatField() #float field.
    objects = models.Manager() #model manager.