from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import PhotoModel
from .models import CommentModel
from .forms import PhotoForm

# Create your views here.
def index(request):
    if 'id' in request.session:
        upload = PhotoModel.objects.all()
        comment = CommentModel.objects.all()
        return render(request,'photo_app/index.html',{'upload':upload,'comment':comment})
    else:
        return redirect('user:login')    
        

def add(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not valid')    
    else:    
        form = PhotoForm
        return render(request,'photo_app/addphoto.html',{'form':form})

def edit(request,id):
    photo = PhotoModel.objects.get(id=id)
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES,instance=photo)
             
        if form.is_valid():
            try:
                form.save()
                return redirect('photo_app:index')
            except:
                return HttpResponse('Failed')
        else:
            print(form.errors)
            return HttpResponse('Form not valid')    
    else:    
        # form = PhotoForm
        return render(request,'photo_app/edit_photo.html',{'photo':photo})
    

