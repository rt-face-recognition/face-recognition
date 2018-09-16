
// Import the messaging module
import * as messaging from "messaging";

var API_KEY = "your-key-goes-here";
var ENDPOINT = "https://api.openweathermap.org/data/2.5/weather" +
                  "?q=San%20Francisco,USA&units=imperial";


// Fetch the weather from OpenWeather
function queryFaceData() {
  var weather = {
          name: "Bob" 
        }
        // Send the weather data to the device
        sendToFitbit(weather);
  // sendToFitbit(ENDPOINT 
}


// Send the weather data to the device
function sendToFitbit(data) {
  if (messaging.peerSocket.readyState === messaging.peerSocket.OPEN) {
    // In seconds
    var DELAY = 2*60;
    var current_time = Math.round((new Date()).getTime() / 1000);

    // Send a command to the device if it's over the delay time
    if (5>3) {
      messaging.peerSocket.send(data);
    } else {
		console.log("Data found, but not sent due to time limits");
	         }
  }
    else {
    console.log("Error: Connection is not open");
  }
}


// Listen for messages from the device
messaging.peerSocket.onmessage = function(evt) {
  if (evt.data) {
	  if (evt.data.command == "face-recognition") {
    	// The device requested face data
    	queryFaceData();
    } else {
      console.log("Error: data was received on the companion, but incorrect command");
    }
  }
}



// Listen for the onerror event
messaging.peerSocket.onerror = function(err) {
  // Handle any errors
  console.log("Connection error: " + err.code + " - " + err.message);
}

