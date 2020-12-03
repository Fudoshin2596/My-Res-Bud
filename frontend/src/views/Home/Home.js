import React from 'react';
import './Root.css';
import { useQuery, useMutation } from '@apollo/react-hooks';
import gql from "graphql-tag";
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import DeleteIcon from '@material-ui/icons/Delete';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';

const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
  table: {
    minWidth: 650,
  },
  button: {
    margin: theme.spacing(1),
  },
}));


const READ_RESTURANTS = gql`
  query {
    resturants{
      id
      name
      address
      rating
      price
      phoneNumber
    }
}`;

const CREATE_RESTURANT = gql`
mutation createResturant($name: String!) {
  createResturant(name: $name){
    resturant{
      id
    }
  }
}
`;

const REMOVE_RESTURANT = gql`
  mutation deleteResturant($id: ID!) {
  deleteResturant(id: $id) {
    id
  }
}
`;

function Home() {
  let input;
  const { data, loading, error } = useQuery(READ_RESTURANTS);
  const [createResturant] = useMutation(CREATE_RESTURANT);
  const [deleteResturant] = useMutation(REMOVE_RESTURANT);
  const classes = useStyles();

  if (loading) return <p>loading...</p>;
  if (error) return <p>ERROR</p>;
  if (!data) return <p>Not found</p>;

  return (
  <div className={classes.root}>
  <h3>Create New Restruant</h3>
  <form className={classes.root} onSubmit={e => {
    e.preventDefault();
    createResturant({ variables: { name: input.value } });
    input.value = '';
    window.location.reload();
    }}>
    <input className={classes.root} type="text" placeholder="Enter resturant name" ref={node => { input = node; }}></input>
    <Button variant="contained" color="primary" type="submit">Add</Button>
  </form>
  <TableContainer component={Paper}>
    <Table className={classes.table} aria-label="simple table">
      <TableHead>
        <TableRow>
          <TableCell>Name</TableCell>
          <TableCell align="left">Address</TableCell>
          <TableCell align="left">Rating</TableCell>
          <TableCell align="left">Price</TableCell>
          <TableCell align="left">Phone Number</TableCell>
          {/* <TableCell align="left">Website</TableCell>  */}
          <TableCell align="left">Delete</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {data.resturants.map((resturants) => (
          <TableRow key={resturants.id}>
            <TableCell component="th" scope="row">
              {resturants.name}
            </TableCell>
            <TableCell align="left">{resturants.address}</TableCell>
            <TableCell align="left">{resturants.rating}</TableCell>
            <TableCell align="left">{resturants.price}</TableCell>
            <TableCell align="left">{resturants.phoneNumber}</TableCell>
            {/* <TableCell align="left">{resturants.website}</TableCell> */}
            <TableCell align="left">
            <Button
              variant="contained"
              color="secondary"
              className={classes.button}
              startIcon={<DeleteIcon />}
              onClick={() => {
              deleteResturant({ variables: { id: resturants.id } });
              window.location.reload();
            }}>Delete</Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  </TableContainer>
  </div>
);
}

export default Home;