from django.contrib import admin
from .models import UploadedFile, SharedFile
# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(SharedFile)