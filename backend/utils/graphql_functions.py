import requests
from requests.exceptions import HTTPError
import json
from string import Template

# query_term = "4.5"  

def GQL_SEARCH(query_term):
    SEARCH = Template("""{
    resturants(search: "$search") {
        name
        address
        rating
        price
        phoneNumber
        website
        }
    }
    """
    )

    SS = SEARCH.substitute({'search': query_term})

    try:
        resp = requests.post("http://localhost:8000/graphql/", params={'query': SS })
        resp.raise_for_status()
        resp_dict = resp.json()
        # resp_dict = json.loads(resp.text)
        return resp_dict['data']['resturants']
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


# ans = GQL_SEARCH(query_term)
# print(ans)
