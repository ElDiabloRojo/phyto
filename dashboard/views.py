from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import Plant
from .forms import SettingsForm

# Create your views here.
def plant_page(request):
    plants = Plant.objects.all()
    return render(request, 'dashboard/plants.html', {
        'plants': plants
    })

def create_plant(request):
    # print(request.POST)
    Plant.objects.create(title=request.POST['title'])
    return redirect('settings')

def complete_plant(request, pk):
    plants = get_object_or_404(Plant, pk=pk)
    plants.is_completed = True
    plants.save()
    return redirect('settings')

def delete_plant(request, pk):
    plants = get_object_or_404(Plant, pk=pk)
    plants.delete()
    return redirect('settings')

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

class SettingsView(TemplateView):
    template_name = 'dashboard/settings.html'

    def get(self, request):
        plants = Plant.objects.all()
        form = SettingsForm()

        return render(request, self.template_name, {
            'form': form,
            'plants': plants
        })

    def post(self, request):
        plants = Plant.objects.all()
        form = SettingsForm(request.POST)

        sunrise = []
        sunset = []
        feed = []

        if form.is_valid():
            form.save()
            sunrise = form.cleaned_data['sunrise']
            sunset = form.cleaned_data['sunset']
            feed = form.cleaned_data['feed']
            return redirect('settings')

        args = {
            'form': form,
            'plants': plants,
            'sunrise': sunrise,
            'sunset': sunset,
            'feed': feed
        }

        return render(request, self.template_name, args)