from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from utils.df_response_lib import *
from utils.graphql_functions import GQL_SEARCH
import json
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
    # get all params
    parameters = req.get('queryResult').get('parameters')
    try:
        address = parameters['location']['street-address']
    except Exception as e:
        address = "New York"
    try:
        rating = get_rating(parameters)
    except Exception as e:
        rating = 0
    # sortparams = parameters['sort']
    spec = GQL_SEARCH(str(rating))
    ans = spec
    out = json.dumps(ans, indent=4)  
    # return a fulfillment message 
    fulfillmentText = {'fulfillmentText': out} 
    # return response 
    return JsonResponse(fulfillmentText, safe=False)
