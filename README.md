# My Res Bud App

Favorite resturant database and resturant reccomendation chatbot

Deployment Link: TBU

## Summary

- Full stack web application that leverages Django for the backend and ReactJS for the frontend. The database is interfaced through GraphQL through both Python and React libaries. On the frontend the user can perform CRUD operations on thier resturant database through a Material UI table using GraphQL. On another tab users can interact with a Google DialogFlow chat bot using Google's API and GraphQl webhook to place queries on the user's database.

- In order to get all the info for the resturants i use both Google and Zomato APIs. When gathering the right cuisine type for a specific resturant i utalize Levenshtein Distance to decide which of a item from a list of queriers is the correct resturant if any.

## Technologies

### Tech Stack

#### Backend

- Python
- Django
- PostgreSQL
- GraphQL (Graphene)
- Google Maps API
- Google Dialogflow (Chatbot)
- Zomato API
- FuzzyWuzzy (Levenshtein Distance)

#### Frontend

- ReactJS
- Material UI
- GraphQL (Apollo)
- Google Dialogflow (Chatbot)

## Potential Next Steps

- Deploy and make available through public url
- Add update functionality to frontend dashboard
- Add User Authenticaiton
