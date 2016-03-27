//Name: Cory Jbara

//Set up the inheritance
Button.prototype = new Item();
Label.prototype = new Item();

//Instantiate the two objects
button = new Button();
label = new Label();

//Function makes async call to change text
function changeText(args) {
	console.log("Changing text");
	var req = new XMLHttpRequest();
	req.open("GET", "http://student02.cse.nd.edu:40001/movies/32", true);
	req.onload = function() {
		args[0].setText(req.response);
	}
	req.send();
};

//Create label and button
label.createLabel("Guess Who!", "theLabel");
button.createButton("Click Here", "theButton");

//Set up button to accept changeText
args = [ label ];
button.addClickEventHandler(changeText, args);

//Add label and button to document
button.addToDocument();
label.addToDocument();
