import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router } from 'react-router-dom';
import { Routes } from './routes'; 
import { ApolloProvider, ApolloClient, InMemoryCache } from '@apollo/client';
import * as serviceWorker from './serviceWorker';

const client = new ApolloClient({
  uri: "http://localhost:8000/graphql/",
  cache: new InMemoryCache()
});

function App() {
  return (
    <ApolloProvider client={client}>
      <Router>
        <Routes />
      </Router>
    </ApolloProvider>
  );
}

render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();

// Random Old imports
// import ReactDOM from "react-dom";
// import ApolloClient from "apollo-boost";
// import { ApolloProvider } from "@apollo/react-hooks";
// import CreateResturant from "./components/Resturants/CreateResturant"
// import ResturantList from "./components/Resturants/ResturantList"
// import ChatBot from "./pages/ChatBot"
// import Profile from "./pages/Profile"
// import Chat from "./pages/Chat"
// import ResturantQuery from './Root';
