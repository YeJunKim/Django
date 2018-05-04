from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})
    
def submit(request):
    return render(request, 'blog/submit.html', {})

    
    