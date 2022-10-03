from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Event
from .forms import EventForm
import folium
import geocoder
import creds
# def index(request):
#     event_list = Event.objects.all()
#     return render(request, 'index.html',
#         {'event_list': event_list})

def index(request):   ########################## Need to loop through all events and add to map
    #for event in Event:
        event = Event.objects.all()
        event_address = '25 E Cedar st 97355' #########Event.address/ This is a placeholder because I couldn't get the address to work from the database
        location = geocoder.google(event_address, key= creds.key)
        location = location.latlng
        lat = location[0]
        lng = location[1]

        # if lat == None or lng == None:
        #     address.delete()
        #     return HttpResponse('Please enter a valid address. Refresh the page to try again.')
        # Create Map Object
        m = folium.Map(location=[45.5236, -122.6750], zoom_start=1.5) #works
        folium.Marker(
            location=[lat, lng],
            popup='WHAT IS THIS',
            tooltip='View Event',
        ).add_to(m)

        m = m._repr_html_()
            #Add Marker
    

        context = {
            'event': event,
            'm': m,
            'address': event_address,
            'lat': lat,
            'lng': lng,
        }
        return render(request, 'index.html', context)
    #folium.Marker([45.3288, -121.6625], popup= title, tooltip=tooltip).add_to(m) #change tooltip to event title
    # folium.Marker([45.3311, -121.7113], popup="<i>Timberline Lodge</i>", tooltip=tooltip).add_to(m)
    # folium.Marker([33.41063301181929, -82.13471009798371], popup="<i>Annex</i>", tooltip=tooltip).add_to(m)

    # folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    # # Get HTML Representation of Map Object
    # m = m._repr_html_()
    # context = {
    #     'm': m,
    #     'form': form,
    #     'address': address,
    # }
    # #m.save("index.html")
    # return render(request, 'index.html', context)
            

def post_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form,}
    return render(request, 'post_event.html', context)




