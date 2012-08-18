from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from pitapp.models import Pit, Profile, Follow

@login_required()
def profile_test(request):
    profile = request.user.get_profile()
    return render_to_response('pitapp/profile_test.html',{'profile':profile})
# Create your views here.
