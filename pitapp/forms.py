from django.forms import ModelForm
from pitapp.models import Pit

class PitForm(ModelForm):
    class Meta:
        exclude = ('deleted','user')
        model = Pit
