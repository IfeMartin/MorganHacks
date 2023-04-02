import googlemaps
import requests

def find_food_pantries(location):
    # Initialize the geocoding client
  gmaps = googlemaps.Client(api_key='AIzaSyBBYnpAxJcaOLChrnWrsDDM-k3WRtKUEDc')
    
    # Geocode the user's location
  geocode_result = gmaps.geocode(location)
  latitude = geocode_result[0]['geometry']['location']['lat']
  longitude = geocode_result[0]['geometry']['location']['lng']
    
    # Use the food bank locator API to find nearby food pantries
  url = f'https://api.feil.org/foodbanks?lat={latitude}&lon={longitude}&distance=10'
  response = requests.get(url)
  results = response.json()
    
    # Format the results into a response for the user
  output = []
  for result in results:
    name = result['name']
    address = result['address']
    hours = result['hours']
    # Add any other information you want to include
    output.append({'name': name, 'address': address, 'hours': hours})
        
  return output



find_food_pantries(input("Location:"))