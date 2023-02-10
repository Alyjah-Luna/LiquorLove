from django.forms import ModelForm
from .models import Spirit

class SpiritForm(ModelForm):
  class Meta:
    model = Spirit
    fields = ['name']

