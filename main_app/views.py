from django.shortcuts import render

liquors = [
    {'name': 'Leyenda', 'spirit': 'Rum', 'description': '', 'ABV': '38%'},
    {'name': 'Los Vecinos', 'spirit': 'Mezcal', 'description': '', 'ABV': '45%'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def liquors_index(request):
    return render(request, 'liquors/index.html', {
        'liquors': liquors
    })