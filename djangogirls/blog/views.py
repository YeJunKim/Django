from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def register(request):
    return render(request, 'blog/register.html', {})

def Login(request):
    return render(request, 'blog/Login.html', {})

def analysis(request):
    return render(request, 'blog/analysis.html', {})

def api(request):
    return render(request, 'blog/api.html', {})


        
def submit(request):
    return render(request, 'blog/submit.html', {})
    