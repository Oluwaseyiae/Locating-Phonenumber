import folium
import phonenumbers
from Text import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode

#Opencage account key
key = "2901ffbf36e34abf9fe759ef52215366"

#Location
ch_nmber = phonenumbers.parse(number, "CH")
your_location = geocoder.description_for_number(ch_nmber, "en")
print("You're in", your_location)

#Carrier
service_nmber = phonenumbers.parse(number, "RO")
your_carrier = carrier.name_for_number(service_nmber, "en")
print("You're using", your_carrier)

#Getting Longitude and Latitude of the Location
geocoder = OpenCageGeocode(key)
query = str(your_location)
result = geocoder.geocode(query)

#Using the Longitude and Latitude of the Location
latitude = result[0]["geometry"]["lat"]
longitude = result[0]["geometry"]["lng"]
print(latitude, longitude)
my_map = folium.Map(location=[latitude, longitude], zoom_start= 9)

folium.Marker([latitude, longitude], popup=your_location).add_to(my_map)

#Save file as HTML
my_map.save("Location.html")