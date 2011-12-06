# Create your views here.
from zimity.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth import logout


def home(request):
    return render_to_response('pages/home.html', context_instance=RequestContext(request))
    
def imprint_index(request):
    imprints = Imprint.objects.all().order_by('-created')[:5]
    return render_to_response('imprints/index.html', {'imprints': imprints})
    
def imprint_view(request, year, month, day, slug):
    imprint = get_object_or_404(Imprint, created__year=year, created__month=month, created__day=day, slug=slug)
    return render_to_response('imprints/view.html', {'imprint': imprint}, context_instance=RequestContext(request))
    
def imprint_add(request):
    return render_to_response('imprints/add.html')
    
def imprint_edit(request):
    return render_to_response('imprints/edit.html')
    
def user_index(request):
    users = User.objects.all()
    return render_to_response('users/index.html', {'users': users})
    
def user_view(request, username):
    user = get_object_or_404(User, username=username)
    return render_to_response('users/view.html', {'user': user}, context_instance=RequestContext(request))
    
def user_add(request):
    return render_to_response('users/add.html')
    
def user_edit(request):
    return render_to_response('users/edit.html')
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(user.get_absolute_url(), context_instance=RequestContext(request))
            else:
                # Return a 'disabled account' error message
                return HttpResponse("disabled", context_instance=RequestContext(request))
        else:
            return HttpResponse("invalid", context_instance=RequestContext(request))
            # Return an 'invalid login' error message.
    else:
        return HttpResponse("blah", context_instance=RequestContext(request))
        
def user_profile(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(request.user.get_absolute_url())
    else:
        return HttpResponseRedirect(reverse('home'))
    
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