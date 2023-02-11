from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Liquor, Cocktail
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
  id_list = liquor.cocktails.all().values_list('id')
  cocktails_liquor_doesnt_have = Cocktail.objects.exclude(id__in=id_list)
  spirit_form = SpiritForm()
  return render(request, 'liquors/detail.html', {
      'liquor': liquor,
       'spirit_form': spirit_form,
       'cocktails': cocktails_liquor_doesnt_have
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
  fields = ['name', 'description', 'ABV']

class LiquorUpdate(UpdateView):
  model = Liquor
  fields = ['description', 'ABV']

class LiquorDelete(DeleteView):
  model = Liquor
  success_url = '/liquors'

def assoc_cocktail(request, liquor_id, cocktail_id):
  Liquor.objects.get(id=liquor_id).cocktails.add(cocktail_id)
  return redirect('detail', liquor_id=liquor_id)

def unassoc_cocktail(request, liquor_id, cocktail_id):
  Liquor.objects.get(id=liquor_id).cocktails.add(cocktail_id)
  return redirect('detail', liquor_id=liquor_id)
