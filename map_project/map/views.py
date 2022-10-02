from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event
from .forms import EventForm
import folium
import geocoder

def index(request):
    if request.method == 'POST':
        form = EventForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('/')        ####################Original code
    else:
        form = EventForm()
    address = Event.objects.all().last()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country
    # if lat == None or lng == None:
    #     address.delete()
    #     return HttpResponse('Please enter a valid address. Refresh the page to try again.')

    # Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=1.5) #works
    tooltip = "View Event!"

    #folium.Marker([45.3288, -121.6625], popup= title, tooltip=tooltip).add_to(m) #change tooltip to event title
    # folium.Marker([45.3311, -121.7113], popup="<i>Timberline Lodge</i>", tooltip=tooltip).add_to(m)
    # folium.Marker([33.41063301181929, -82.13471009798371], popup="<i>Annex</i>", tooltip=tooltip).add_to(m)

    folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        'form': form,
        #'address': address,
    }
    
    return render(request, 'index.html', context)
            

def post_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form,}
    return render(request, 'post_event.html', context)
