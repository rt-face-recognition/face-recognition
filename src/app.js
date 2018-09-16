// Import the messaging module
import * as messaging from "messaging";
import { vibration } from "haptics";



// Listen for the onopen event
messaging.peerSocket.onopen = function() {
  // Fetch faces when the connection opens
	fetchPeople();
	console.log("Opening connection... I think");
}


// Listen for messages from the companion
messaging.peerSocket.onmessage = function(evt) {
	if (evt.data) {
		console.log("received something!");
		let demotext = document.getElementById("demotext");
		demotext.text = "This worked :)";
		vibration.start("ring");
		console.log(data.name)
	}
}


// Request face data from the companion
function fetchPeople() {
  if (messaging.peerSocket.readyState === messaging.peerSocket.OPEN) {
    // Send a command to the companion
  	messaging.peerSocket.send({command: "face-recognition"});
  }
}


// Listen for the onerror event
messaging.peerSocket.onerror = function(err) {
  // Handle any errors
  console.log("Connection error: " + err.code + " - " + err.message);
}


// Fetch the weather every 10 seconds
setInterval(fetchPeople, 10 * 1000);
