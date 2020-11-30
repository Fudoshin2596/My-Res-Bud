import json

from itertools import islice, count

def iter_range(start, stop, step):
    if step == 0:
        raise ValueError("Step could not be NULL")
    length = int(abs(stop - start) / step)
    return islice(count(start, step), length)

parameters = {
    "location": {
    "country": "",
    "city": "",
    "admin-area": "",
    "business-name": "",
    "street-address": "midtown",
    "zip-code": "",
    "shortcut": "",
    "island": "",
    "subadmin-area": ""
    },
    "venue-type": [
    "restaurant"
    ],
    "sort": [
    "expensive",
    "best"
    ],
    "rating": "> 4.5",
    "pricelevel": "",
    "dish": [],
    "beverage": [],
    "cuisine": [],
    "venue-title": "",
    "venue-chain": "",
    "venue-facility": "",
    "meal": "",
    "open": "",
    "stars": "",
    "map-sort": ""
},


conditional_operators = '>'

def get_rating(parameters):
    rating_condition = parameters[0]['rating'].split(" ")[0]
    rating_scale = float(parameters[0]['rating'].split(" ")[1])
    if rating_condition == '>':
        rating = [ float("{0:.1f}".format(x)) for x in iter_range(rating_scale, 5.11, 0.1)]
    else:
        rating = [ float("{0:.1f}".format(x)) for x in iter_range(0, rating_scale, 0.1)]
    return rating

address = parameters[0]['location']['street-address']
rating = get_rating(parameters)
sortparams = parameters[0]['sort']
spec = f'{address}, {rating}, {sortparams}'
out = json.dumps(spec, indent=4)  
# return a fulfillment message 
fulfillmentText = {'fulfillmentText': out} 
print(fulfillmentText)