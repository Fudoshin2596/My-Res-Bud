from fuzzywuzzy import fuzz, process

import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()


class Zomato:
    def __init__(self):
        self.user_key = os.getenv("ZOMATO_API_KEY")
        self._base_url = "https://developers.zomato.com/api/v2.1/"
        self._entity_type = 'city'
        self._entity_id = '280'

    def restaurant_query_search(self, query="", limit=5):
        """
        Takes query as string
        Returns a list of Restaurant dict.
        """
        headers = {'Accept': 'application/json', 'user-key': self.user_key}
        r = (requests.get(f"{self._base_url}search?entity_id={self._entity_id}&entity_type={self._entity_type}&q={str(query)}&count={str(limit)}",
                          headers=headers).content).decode("utf-8")
        a = json.loads(r)
        restaurants = []
        res_dict = {}

        if a['results_found'] == 0:
            return []
        else:
            for restaurant in a['restaurants']:
                restaurants.append(restaurant['restaurant'])

        for item in restaurants:
            name = item['name']
            res_dict[f'{name}'] = {}
            res_dict[f'{name}']['id'] = item['id']
            res_dict[f'{name}']['cuisines'] = item['cuisines']
            res_dict[f'{name}']['cost4two'] = item['average_cost_for_two']

        return res_dict

    def match(self, query=""):
        ResturantsInfo = self.restaurant_query_search(query=query)
        passers = []
        for item in ResturantsInfo.items():
            # print(item)
            # print(item[0])
            if fuzz.ratio(query.lower(), item[0].lower()) > 90:
                passers.append(item)

        return process.extractOne(query, passers)

# ZomatoObj = Zomato()
# query = 'Le Coucou' 


# passers = ZomatoObj.match(query)
# print(passers[0][1]['cuisines'])
