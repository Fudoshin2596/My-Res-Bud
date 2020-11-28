import React from 'react';
import { render } from 'react-dom';
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

import Root from "./Root";


const client = new ApolloClient({
  uri: 'http://localhost:8000/graphql/',
  cache: new InMemoryCache()
});

export default function App() {
  return (
      <ApolloProvider client={client}>
          <Root />
      </ApolloProvider>
  );
}

render(<App />, document.getElementById('root'));
