//Name: Cory Jbara

//Set up the inheritance
Button.prototype = new Item();
Label.prototype = new Item();
Dropdown.prototype = new Item();

//Instantiate the two objects
button = new Button();
label = new Label();
rating = new Label();
voteButton = new Button();
dropdown = new Dropdown();

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

//Function to handle voteButton click
function voteHandler(args) {
	
	dropdown.getSelected();
}

//Create elements
label.createLabel("Which Movie?", "theLabel");
rating.createLabel("I thought the movie was...", "ratingLabel");
button.createButton("Click Here", "theButton");
voteButton.createButton("Vote", "voteButton");

var ratings = { 1: "Just Plain Bad", 2: "Not So Good", 3: "Okay I Guess", 4: "Pretty Good", 5: "Awesome!" };
dropdown.createDropdown(ratings, "dropdown", 5);

//Set up buttons handlers
args = [ label ];
button.addClickEventHandler(changeText, args);
voteButton.addClickEventHandler(voteHandler, []);

//Add label and button to document
label.addToDocument();
button.addToDocument();
rating.addToDocument();
dropdown.addToDocument();
voteButton.addToDocument();
