const message = new SpeechSynthesisUtterance();

// set the text to be spoken
message.text = "Hello World!";

// create an instance of the speech synthesis object
const speechSynthesis = window.speechSynthesis;

// start speaking
speechSynthesis.speak(message);