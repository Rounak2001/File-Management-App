from django.db import models
from django.contrib.auth.models import User

class UploadedFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Upload_file = models.FileField(upload_to='uploads')
    title = models.CharField(max_length = 100)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class SharedFile(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='shared_files')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UploadedFile')
    recipients = models.ManyToManyField(User, related_name='received_files')
    shared_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    