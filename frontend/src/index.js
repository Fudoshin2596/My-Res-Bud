import React from 'react';
import { render } from 'react-dom';
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

import CreateResturant from "./components/Resturants/CreateResturant"
import ResturantList from "./components/Resturants/ResturantList"

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache()
});

function App() {
  return (
    <ApolloProvider client={client}>
      <ResturantList />
    </ApolloProvider>
  );
}

render(<App />, document.getElementById('root'));