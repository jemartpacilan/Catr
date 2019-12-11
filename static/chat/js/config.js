/* eslint-disable no-unused-vars */

// Make a copy of this file and save it as config.js (in the js directory).

// Set this to the base URL of your sample server, such as 'https://your-app-name.herokuapp.com'.
// Do not include the trailing slash. See the README for more information:

var SAMPLE_SERVER_BASE_URL = 'https://catr-opentok-server.herokuapp.com';

// OR, if you have not set up a web server that runs the learning-opentok-php code,
// set these values to OpenTok API key, a valid session ID, and a token for the session.
// For test purposes, you can obtain these from https://tokbox.com/account.

var API_KEY;
var SESSION_ID;
var TOKEN;
var catererId;
var consumerId;

if(window.location.pathname.match(/\/chat\/conchat\//)){	
	catererId =	window.location.pathname.replace(/\/chat\/conchat\//, '');
	consumerId = $("input#hidden_catruser_id")[0].value
} else {
	catererId = window.location
	                      .pathname
	                      .replace(/\/chat\/catchat\//, '')
	                      .replace(/\/\d+$/, '');
	consumerId = window.location
	                   .pathname
	                   .replace(/\/chat\/catchat\/\d+\//, '');
}

console.log(catererId);
console.log(consumerId);