import React from 'react';
import ReactDOM from "react-dom";
import { render } from 'react-dom';
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';

import CreateResturant from "./components/Resturants/CreateResturant"
import ResturantList from "./components/Resturants/ResturantList"
import ChatBot from "./pages/ChatBot"

import "./style.css";
import Chat from "./pages/Chat"

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache()
});

function App() {
  return (
    <ApolloProvider client={client}>
      <div className="mainSection">
        <div className="heading">
        </div>  
        <ChatBot />
      </div>
    </ApolloProvider>
  );
}

render(<App />, document.getElementById('root'));