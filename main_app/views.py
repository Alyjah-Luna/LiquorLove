from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Liquor

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def liquors_index(request):
    liquors = Liquor.objects.all()
    return render(request, 'liquors/index.html', {
        'liquors': liquors
    })

def liquors_detail(request, liquor_id):
  liquor = Liquor.objects.get(id=liquor_id)
  return render(request, 'liquors/detail.html', { 'liquor': liquor })

class LiquorCreate(CreateView):
  model = Liquor
  fields = '__all__'

class LiquorUpdate(UpdateView):
  model = Liquor
  fields = ['spirit', 'description', 'ABV']

class LiquorDelete(DeleteView):
  model = Liquor
  success_url = '/liquors'