# Create your views here.
from zimity.models import *
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext

def home(request):
    return render_to_response('pages/home.html')
    
def imprint_index(request):
    imprints = Imprint.objects.all().order_by('-created')[:5]
    return render_to_response('imprints/index.html', {'imprints': imprints})
    
def imprint_view(request, slug):
    imprint = get_object_or_404(Imprint, slug=slug)
    return render_to_response('imprints/view.html', {'imprint': imprint})
    
def imprint_add(request):
    return render_to_response('imprints/add.html')
    
def imprint_edit(request):
    return render_to_response('imprints/edit.html')
    
def user_index(request):
    users = User.objects.all()
    return render_to_response('users/index.html', {'users': users})
    
def user_view(request, id):
    user = get_object_or_404(User, pk=id)
    return render_to_response('users/view.html', {'user': user}, context_instance=RequestContext(request))
    
def user_add(request):
    return render_to_response('users/add.html')
    
def user_edit(request):
    return render_to_response('users/edit.html')
    
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