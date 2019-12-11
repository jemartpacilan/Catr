/* global API_KEY TOKEN SESSION_ID SAMPLE_SERVER_BASE_URL OT */
/* eslint-disable no-alert */

var apiKey;
var session;
var sessionId;
var token;

function initializeSession() {
  alert('session initialized')
  session = OT.initSession(apiKey, sessionId);

  // Subscribe to a newly created stream
  session.on('streamCreated', function streamCreated(event) {
    var subscriberOptions = {
      subscribeToVideo: false,
      subscribeToAudio: false,
      insertMode: 'none',
      width: '0',
      height: '0'
    };
    session.subscribe(event.stream, 'subscriber', subscriberOptions, function callback(error) {
      if (error) {
        console.error('There was an error publishing: ', error.name, error.message);
      }
    });
  });

  session.on('sessionDisconnected', function sessionDisconnected(event) {
    console.error('You were disconnected from the session.', event.reason);
  });

  // Initialize the publisher
  var publisherOptions = {
    audioSource: null,
    videoSource: null,
    publishVideo: false,
    publishAudio: false,
    insertMode: 'none',
    width: '0',
    height: '0'
  };
  var publisher = OT.initPublisher('publisher', publisherOptions, function initCallback(initErr) {
    if (initErr) {
      console.error('There was an error initializing the publisher: ', initErr.name, initErr.message);
      return;
    }
  });

  // Connect to the session
  session.connect(token, function callback(error) {
    // If the connection is successful, initialize a publisher and publish to the session
    if (!error) {
      // If the connection is successful, publish the publisher to the session
      session.publish(publisher, function publishCallback(publishErr) {
        if (publishErr) {
          console.error('There was an error publishing: ', publishErr.name, publishErr.message);
        }
      });
    } else {
      console.error('There was an error connecting to the session: ', error.name, error.message);
    }
  });

  // Receive a message and append it to the history
  var msgHistory = document.querySelector('.chatbox-spacer');
  session.on('signal:msg', function signalCallback(event) {        
    var textContent = event.data;
    var className = event.from.connectionId === session.connection.connectionId ? 'me' : 'caterer';

    var appendedBubbleInText = '<div class="row">' + ((className === 'caterer') ? 
                                 ('<div class="chatbox-div-image col-sm-1 m-auto">' +
                                   '<img class="chatbox-image" src="https://image.ibb.co/c6JYXT/1499344631_malecostume.png">' +
                                 '</div>' +
                                 '<div class="chathistory-div col-sm-11">' + 
                                   '<div class="' + className + ' chatbubble">' +
                                     textContent + ' <turpis class=""></turpis>' +
                                   '</div>' +
                                 '</div>') :
                                 ('<div class="chathistory-div col-sm-11">' + 
                                    '<div class="' + className + ' chatbubble">' +
                                      textContent + ' <turpis class=""></turpis>' +
                                    '</div>' +
                                  '</div>' +
                                  '<div class="chatbox-div-image col-sm-1 m-auto">' +
                                    '<img class="chatbox-image" src="https://image.ibb.co/c6JYXT/1499344631_malecostume.png">' +
                                  '</div>')) +
                               '</div>'

    var msg = new DOMParser().parseFromString(appendedBubbleInText, 'text/html');    
    msgHistory.appendChild(msg.body.firstChild);    
  });
}

// Text chat
var form = document.querySelector('form#chat-form');
var msgTxt = document.querySelector('#msgTxt');

// Send a signal once the user enters data in the form
form.addEventListener('submit', function submit(event) {
  session.signal({
    type: 'msg',
    data: msgTxt.value
  }, function signalCallback(error) {
    if (error) {
      console.error('Error sending signal:', error.name, error.message);
    } else {
      msgTxt.value = '';
    }
  });
});

// See the config.js file.
if (API_KEY && TOKEN && SESSION_ID) {
  apiKey = API_KEY;
  sessionId = SESSION_ID;
  token = TOKEN;
  initializeSession();
} else if (SAMPLE_SERVER_BASE_URL) {
  // Make an Ajax request to get the OpenTok API key, session ID, and token from the server
  fetch(SAMPLE_SERVER_BASE_URL + '/room/' +catererId + ':' + consumerId).then(function fetch(res) {
    session_request = res.json();
    return session_request;
  }).then(function fetchJson(json) {
    console.log(json);
    apiKey = json.apiKey;
    sessionId = json.sessionId;
    token = json.token;

    initializeSession();
  }).catch(function catchErr(error) {
    console.error('There was an error fetching the session information', error.name, error.message);
    alert('Failed to get opentok sessionId and token. Make sure you have updated the config.js file.');
  });
}