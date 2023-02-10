from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Liquor
from .forms import SpiritForm

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
  spirit_form = SpiritForm()
  return render(request, 'liquors/detail.html', {
      'liquor': liquor,
       'spirit_form': spirit_form 
       })

def add_spirit(request, liquor_id):
  form = SpiritForm(request.POST)
  if form.is_valid():
    new_spirit = form.save(commit=False)
    new_spirit.liquor_id = liquor_id
    new_spirit.save()
  return redirect('detail', liquor_id=liquor_id)

class LiquorCreate(CreateView):
  model = Liquor
  fields = '__all__'

class LiquorUpdate(UpdateView):
  model = Liquor
  fields = ['description', 'ABV']

class LiquorDelete(DeleteView):
  model = Liquor
  success_url = '/liquors'