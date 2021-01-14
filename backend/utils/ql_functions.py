from gql.transport.requests import RequestsHTTPTransport
from gql import Client, gql
import json
from string import Template


def GQL_SEARCH(query_term):
  """
  Search string based feilds
  """
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
  """
  Search float based feilds
  """
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