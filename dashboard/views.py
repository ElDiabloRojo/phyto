from django.shortcuts import render, redirect, get_object_or_404
from .models import Plant

# Create your views here.
def plant_page(request):
    plants = Plant.objects.all()
    return render(request, 'dashboard/plants.html', {
        'plants': plants
    })

def create_plant(request):
    # print(request.POST)
    Plant.objects.create(title=request.POST['title'])
    return redirect('plants')

def complete_plant(request, pk):
    plants = get_object_or_404(Plant, pk=pk)
    plants.is_completed = True
    plants.save()
    return redirect('plants')

def delete_plant(request, pk):
    plants = get_object_or_404(Plant, pk=pk)
    plants.delete()
    return redirect('plants')

def settings_page(request):
    plants = Plant.objects.all()
    return render(request, 'dashboard/settings.html', {
        'plants': plants
    })

def gallery_page(request):
    plants = Plant.objects.all()
    return render(request, 'dashboard/gallery.html', {
        'plants': plants
    })