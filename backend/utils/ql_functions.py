from gql.transport.requests import RequestsHTTPTransport
from gql import Client, gql
# import requests
# from requests.exceptions import HTTPError
import json
from string import Template

# query_term = "French"

def GQL_SEARCH(query_term):
  transport = RequestsHTTPTransport(url="http://localhost:8000/graphql/", verify=True, retries=3)

  client = Client(transport=transport, fetch_schema_from_transport=True)

  query = gql(
      """
      query SearchResturants($search: String) {
        resturants(search: $search) {
          name
          address
          rating
          price
          phoneNumber
          website
          cuisines
        }
      }
  """
  )

  params = {
      "search": query_term
    }

  result = client.execute(query, variable_values=params)

  return result['resturants']


def GQL_SEARCHR(query_term):
  transport = RequestsHTTPTransport(
      url="http://localhost:8000/graphql/", verify=True, retries=3)

  client = Client(transport=transport, fetch_schema_from_transport=True)

  query = gql(
      """
      query SearchResturants($rating_Gte: Float) {
        allResturants(rating_Gte: $rating_Gte) {
          edges {
            node {
              name
              address
              cuisines
              rating
              price
            }
          }
        }
      }
  """
  )

  params = {
      "rating_Gte": query_term
  }

  result = client.execute(query, variable_values=params)

  return result['allResturants']['edges']
  
    # SEARCH = Template("""{
    #         resturants(search: $search) {
    #             name
    #             address
    #             rating
    #             price
    #             phoneNumber
    #             website
    #             cuisines
    #             }
    #         }
    #     """
    #     )

    # SS = SEARCH.substitute({'search': query_term})
    # print(SS)

    # try:
    #     resp = requests.post("http://localhost:8000/graphql/", params={'query': SS })
    #     resp.raise_for_status()
    #     resp_dict = resp.json()
    #     # resp_dict = json.loads(resp.text)
    #     return resp_dict['data']['resturants']
    # except HTTPError as http_err:
    #     print(f'HTTP error occurred: {http_err}')
    # except Exception as err:
    #     print(f'Other error occurred: {err}')


# ans = GQL_SEARCH(query_term)
# print(ans)
