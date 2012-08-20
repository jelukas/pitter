from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import  RequestContext
from django.contrib.auth.decorators import login_required
from pitapp.decorators import ajax_required
from pitapp.models import Pit, Profile, Follow
from pitapp.forms import PitForm


@login_required
def profile_test(request):
    profile = request.user.get_profile()
    return render_to_response('pitapp/profile_test.html',{'profile':profile},context_instance = RequestContext(request))

#@ajax_required
@login_required
def new(request):
    if request.method == 'POST': # If the form has been submitted...
        pit_form = PitForm(request.POST) # A form bound to the POST data
        if pit_form.is_valid(): # All validation rules pass
            pit = pit_form.save(commit=False)
            pit.user = request.user
            pit.save()
            return HttpResponseRedirect('/pitter/test/') # Redirect after POST
    else:
        pit_form = PitForm() # An unbound form
    return render_to_response('pitapp/new_ajax_form.html',{'message':'Hola mundo cruel','pit_form':pit_form},context_instance = RequestContext(request))