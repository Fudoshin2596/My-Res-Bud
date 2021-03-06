import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import { Link } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
  offset: theme.mixins.toolbar,
}));

const NavBar = () => {
  const classes = useStyles();

  return (
    <React.Fragment>
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            My Res Bud App
          </Typography>
          <Button color="inherit"><Link to="/Home">Home</Link></Button>
          <Button color="inherit"><Link to="/ChatBox">ChatBox</Link></Button>
        </Toolbar>
      </AppBar>
    </div>
    </React.Fragment>
  );
}

export default NavBar;