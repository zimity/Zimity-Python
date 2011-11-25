# Create your views here.
from zimity.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('pages/home.html')
    
def imprint_index(request):
    return render_to_response('pages/about.html')
    
def imprint_view(request, id):
    return render_to_response('pages/about.html')
    
def imprint_add(request):
    return render_to_response('pages/about.html')
    
def imprint_edit(request):
    return render_to_response('pages/about.html')
    
def user_index(request):
    users = User.objects.all()
    return render_to_response('users/index.html', {'users': users})
    
def user_view(request):
    return render_to_response('pages/about.html')
    
def user_add(request):
    return render_to_response('pages/about.html')
    
def user_edit(request):
    return render_to_response('pages/about.html')
    
def about(request):
    return render_to_response('pages/about.html')
                              
def contact(request):
    return render_to_response('pages/contact.html')

def dev(request):
    return render_to_response('pages/dev.html')

def jobs(request):
    return render_to_response('pages/jobs.html')

def terms(request):
    return render_to_response('pages/terms.html')
    
def privacy(request):
    return render_to_response('pages/privacy.html')