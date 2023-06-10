from django.contrib import admin
from . import models

# Register your models here.
admin.site.register([
    models.Project, # adding Project table to the DB
    models.Review,  # adding Review table to the DB
    models.Tag,     # adding Tag table to the DB
])
