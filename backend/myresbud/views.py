from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.df_response_lib import *
from utils.ql_functions import GQL_SEARCH, GQL_SEARCHR
import json
import random
from itertools import islice, count


def iter_range(start, stop, step):
    if step == 0:
        raise ValueError("Step could not be NULL")
    length = int(abs(stop - start) / step)
    return islice(count(start, step), length)

def get_rating(parameters):
    rating_condition = parameters['rating'].split(" ")[0]
    rating_scale = float(parameters['rating'].split(" ")[1])
    if rating_condition == '>':
        rating = [ float("{0:.1f}".format(x)) for x in iter_range(rating_scale, 5.11, 0.1)]
    else:
        rating = [ float("{0:.1f}".format(x)) for x in iter_range(0, rating_scale, 0.1)]
    return rating

# define home function 
def home(request): 
    return HttpResponse('Hello World!') 

@csrf_exempt 
def webhook(request): 
    # build a request object 
    req = json.loads(request.body) 
    
    # get action from json 
    action = req.get('queryResult').get('action')
    
    # get intent from json
    intent = req.get('queryResult').get('intent').get('displayName')
    
    # get all params
    parameters = req.get('queryResult').get('parameters')
    
    try:
        address = parameters['location']['street-address']
    except Exception as e:
        address = "New York"

    if intent == 'venues.eating_out.search.pricelevel':
        if parameters['pricelevel'] == "very cheap":
            pricelevel = '$'
        elif parameters['pricelevel'] == "cheap":
            pricelevel = '$$'
        elif parameters['pricelevel'] == "moderate":
            pricelevel='$$$'
        elif parameters['pricelevel'] == "any":
            pricelevel = '$'*random.choice(range(1,5))
        else:
            pricelevel='$$$$'
        
        spec=GQL_SEARCH(pricelevel)

    if intent == 'venues.eating_out.search.rating':
        try:
            rating = get_rating(parameters)
        except Exception as e:
            rating = 0
        
        spec = GQL_SEARCHR(rating)

    if intent == 'venues.eating_out.search.cuisine':
        if len(parameters['cuisine']) > 1:
            cuisine = ''.join(parameters['cuisine'][0])
        else:
            cuisine = ''.join(parameters['cuisine'])

        spec = GQL_SEARCH(cuisine)
    
    out = json.dumps(spec, indent=4)
    # return a fulfillment message 
    fulfillmentText = {'fulfillmentText': out} 
    # return response 
    return JsonResponse(fulfillmentText, safe=False)
