import React from "react";

import Container from '@material-ui/core/Container';

function About() {
  return (
    <Container maxWidth="sm">
        <meta charSet="utf-8" />
        <meta name="viewport" content="width-device-width, initial-scale=1" />
        <meta content="ie=edge" http-equiv="X-UA-Compatible"/>
        <iframe id="iframe" allow="microphone;" width="350" height="430" src="https://console.dialogflow.com/api-client/demo/embedded/cecffa92-4622-4969-b78f-a45134699444"></iframe>
    </Container>
  );
}

export default About;