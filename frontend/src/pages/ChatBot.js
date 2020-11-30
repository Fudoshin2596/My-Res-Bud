import React from 'react';
import withTheme from "../withTheme";

import Container from '@material-ui/core/Container';

function GoogleWebDemo() {
  return (
    <Container maxWidth="sm">
            <meta charSet="utf-8" />
            <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
            <meta content="ie=edge" http-equiv="X-UA-Compatible"/>
        <iframe id="iframe" height="1024px" width="1000px" src="https://bot.dialogflow.com/cecffa92-4622-4969-b78f-a45134699444"> </iframe>
    </Container>
  );
}

export default withTheme(GoogleWebDemo);
  
