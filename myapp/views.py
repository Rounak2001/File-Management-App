from django.shortcuts import render, redirect
# from .forms import FileUploadForm
from .models import UploadedFile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import SharedFile

@login_required
def upload_file(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        Upload_file = request.FILES.get('upload_file')

        UploadedFile.objects.create(
                user=request.user,
                Upload_file = Upload_file,
                title = title
        )

        return redirect("files")
    


    return render(request, 'myapp/upload.html')

@login_required
def file_list(request):
    user_files = UploadedFile.objects.filter(user=request.user)
    shared_files = SharedFile.objects.filter(recipients=request.user)
    return render(request, 'myapp/files.html', {'files': user_files,'shared_files': shared_files})

@login_required
def delete_file(request,id):
    file = UploadedFile.objects.get(id = id)
    file.delete()
    return redirect("/files/")

@login_required
def searchuser(request):
    if request.method=="POST":
        search = request.POST['search']
        searched = User.objects.filter(username__icontains = search)
        user_files = UploadedFile.objects.filter(user=request.user)
        return render(request,'myapp/search.html',{'search':search, 'searched':searched, 'files':user_files})
    else:
        return render(request,'myapp/search.html',{})
    



def sharefile(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        file = request.FILES.get('file')
        recipients_ids = request.POST.getlist('recipients')
        uploader = request.user

        shared_file = SharedFile.objects.create(
            title=title,
            file=file,
            uploader=uploader
        )
        shared_file.recipients.add(*recipients_ids)
        shared_file.save()

        

    users = User.objects.exclude(pk=request.user.id)  # Exclude the current user
    return render(request, 'myapp/sharefile.html', {'users': users})

# def sharedfile(request):
#     shared_files = SharedFile.objects.filter(recipients=request.user)
#     return render(request, 'myapp/sharedfile.html', {'shared_files': shared_files})
