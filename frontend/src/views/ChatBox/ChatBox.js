import React, { Component } from 'react';
import Container from '@material-ui/core/Container';

// GoogelDialogFlow Basic ChatBox Utility
function ChatBox() {
  return (
    <Container >
        <meta name="viewport" content="width-device-width, initial-scale=1" />
        <meta content="ie=edge" http-equiv="X-UA-Compatible"/>
        <iframe id="iframe" allow="microphone;" width="875" height="800" src="https://console.dialogflow.com/api-client/demo/embedded/cecffa92-4622-4969-b78f-a45134699444"></iframe>
    </Container>
  );
}

// Kommunicate ChatBox Utility
class XChatBox extends Component {
  constructor(props) {
    super(props);
  }
  componentDidMount(){
    (function(d, m){
      var kommunicateSettings = {"appId":"352375d75eb6b49a95122bd66f9eddcef","popupWidget":true,"automaticChatOpenOnNavigation":true};
      var s = document.createElement("script"); s.type = "text/javascript"; s.async = true;
      s.src = "https://widget.kommunicate.io/v2/kommunicate.app";
      var h = document.getElementsByTagName("head")[0]; h.appendChild(s);
      window.kommunicate = m; m._globals = kommunicateSettings;
    })(document, window.kommunicate || {});
  }
render() {
    return (
      <div></div>
    )
  }

}

export default ChatBox;