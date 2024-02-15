from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('upload_file/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='files'),
    path('delete-file/<id>/', views.delete_file, name='delete-file'),
    path('searchuser/',views.searchuser, name='searchuser'),
    path('sharefile/',views.sharefile, name ='sharefile'),
    #path('sharedfile/',views.sharedfile, name = 'sharedfile'),

]

if settings.DEBUG:
    
    urlpatterns += static(settings.MEDIA_URL,
                            document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()