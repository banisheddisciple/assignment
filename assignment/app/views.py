from django.shortcuts import render, redirect
from app.forms import UploadForm

def home(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = UploadForm()

    context = {'form': UploadForm()}
    return render(request, 'app/home.html',context)
