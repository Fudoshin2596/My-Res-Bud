import React from 'react';
import { useQuery, gql } from '@apollo/client';
import withTheme from "./withTheme";

import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';

const RESTURANT_QUERY = gql`
  query {
  resturants{
    id
    name
    address
    rating
    price
    phoneNumber
    website
  }
}`;

function ResturantQuery() {
  const { loading, error, data } = useQuery(RESTURANT_QUERY);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return data.resturants.map(({ id, name, address, rating, phoneNumber, price, website }) => (
    <Container maxWidth="sm">
    <Box my={1}>
    <Typography variant="h6" component="h1" gutterBottom>
    <div key={id}>
      <ul>
      <li>{"id"}: {id}</li>
      <li>{"name"}: {name}</li>
      <li>{"address"}: {address}</li>
      <li>{"rating"}: {rating}</li>
      <li>{"price"}: {price}</li>
      <li>{"phone number"}: {phoneNumber}</li>
      <li>{"website"}: {website}</li>
      </ul>
    </div>
    </Typography>
    </Box>
    </Container>
  ));
}

export default withTheme(ResturantQuery);