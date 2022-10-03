from .models import Event



def index():
    location = Event.objects.all()
    print(location)

index()











#import geocoder

# def index():
#     #API_KEY = 'AIzaSyAbef5FgmAxnSP54OKvj_TWXMBYRqdNbAk'
#     address = "25 E Cedar st 97355"
#     location = geocoder.google(address, key='AIzaSyAbef5FgmAxnSP54OKvj_TWXMBYRqdNbAk')
#     location = location.latlng
#     lat = location[0]
#     lng = location[1]
#     print(lat, lng)
    

# index()

# def index():
#     #API_KEY = 'AIzaSyAbef5FgmAxnSP54OKvj_TWXMBYRqdNbAk'
#     location = Event.objects.all()

#     print(location)
    

# index()