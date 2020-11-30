from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# import csrf fro CSRF protection
from django.views.decorators.csrf import csrf_exempt
# import df_library 
from library.df_response_lib import *
# import json to get json request
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
    address = parameters['location']['street-address']
    rating = get_rating(parameters)
    sortparams = parameters['sort']
    spec = f'{address}, {rating}, {sortparams}'
    out = json.dumps(spec, indent=4)  
    # return a fulfillment message 
    fulfillmentText = {'fulfillmentText': out} 
    # return response 
    return JsonResponse(fulfillmentText, safe=False)