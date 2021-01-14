![MRB Logo](assets/logo.png)
# My Res Bud App

Favorite restaurant database and restaurant recommendation chatbot

Deployment Link: TBU

## Summary

- Full stack web application that leverages Django for the backend with a PostgreSQL database and ReactJS for the frontend. The database is interfaced through GraphQL API using both Python and React libraries for schema creation and access. On the frontend the user can perform CRUD operations on their restaurant database through a Material UI table using the GraphQL API layer. On another tab users can interact with a Google DialogFlow chat bot using Google's API and a GraphQL webhook to place queries on the user's database.

- In order to get all the info for the restaurants I use both Google and Zomato APIs. When gathering the right cuisine type for a specific restaurant I use Levenshtein Distance to decide which item from a list of queriers is the correct restaurant if any.

- The chat bot leverages 3 key intents: Query by price, Query by rating, or Query by cuisine. These intents are accessed through a welcome context/conversation flow which encodes query entities based on user’s response and sends those entities to a webhook which performs a GraphQL query with search and filter functionality. GraphQL then returns a list or dictionary with the specified meta data on 5 or less matching entries.

## Technologies

### Tech Stack

#### Backend

- Python
- Django
- PostgreSQL
- GraphQL (Graphene)
- Google Maps API
- Google DialogFlow Webhook (Ngrok in development)
- Zomato API
- FuzzyWuzzy (Levenshtein Distance)

#### Frontend

- ReactJS
- Material UI
- GraphQL (Apollo)
- Google DialogFlow (Chatbot)

## Potential Next Steps

- Deploy and host on public url
- Add Update functionality to frontend dashboard, so users can modify database entries using GraphQL mutations
- Add User Authentication, authentication should protect database views so that users can only access entries associated with them whether through the dashboard or chatbot

## Screenshots

#### GraphiQL backend 
![GQL Backend](assets/GraphiQL_BackEnd.png)

#### ChatBot frontend 
![Google DialogFlow Chatbot](assets/Chat_Bot_FrontEnd.png)

#### Dashboard frontend 
![MaterialUI Table](assets/Dashboard_FrontEnd.png)

