import googlemaps
import json

GMAPS_API_KEY = "AIzaSyB82T513Cr6TiZN4EPdzYnCYx5Ak1FIcfU"

class ResturantInfo:
    def __init__(self, query, key, userlocation):
        self.query = query
        self.gmaps = googlemaps.Client(key=key)
        self.lbias = self.getLocationBias(userlocation)
        
    def getLocationBias(self, userlocation):
        geocode_result = self.gmaps.geocode(userlocation)
        lat = geocode_result[0]['geometry']['location']['lat']
        lng = geocode_result[0]['geometry']['location']['lng']
        return f'point:{lat},{lng}'

    def placeInfo(self):
        findplace_result = self.gmaps.find_place(self.query, input_type='textquery', location_bias=self.lbias)
        placeid = findplace_result['candidates'][0]['place_id']
        place_result = self.gmaps.place(place_id=placeid)
        try:
            rating = place_result['result']['rating']
            rating = float(rating)
        except Exception as e:
            rating = 0
        try:
            price = place_result['result']['price_level']
            price = int(price)*"$"
        except Exception as e:
            price = "NA"
        return {
                'address': place_result['result']['formatted_address'],
                'phonenumber': place_result['result']['international_phone_number'],
                'rating': rating,
                'price': price,
                'name': place_result['result']['name'],
                'id': place_result['result']['place_id'],
                'website': place_result['result']['website']
                }


# userlocation = 'New York, NY'
# query = 'citizens of bleecker'
# TestResturant = ResturantInfo(query, GMAPS_API_KEY, userlocation)
# info = TestResturant.placeInfo()
# print(info)

# gmaps = googlemaps.Client(key=GMAPS_API_KEY)
# findplace_result = gmaps.find_place(query, input_type='textquery')
# placeid = findplace_result['candidates'][0]['place_id']
# place_result = gmaps.place(place_id=placeid)
# print(json.dumps(place_result, indent=2))