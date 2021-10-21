from django.contrib import admin
from TFS.models import customerdetail, transectiondetail

# Register your models here.
admin.site.register((customerdetail, transectiondetail))