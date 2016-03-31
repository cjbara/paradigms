//Name: Cory Jbara

//Create the movie_id
var movie_id = 32;
var user_id = 4;

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
	req.open("GET", "http://student02.cse.nd.edu:40001/movies/"+movie_id, true);
	req.onload = function() {
		args[0].setText(req.response);
	}
	req.send();
};

//Function to handle voteButton click
function voteHandler(dropdown) {
	console.log("Rating movie "+movie_id+" with a rating of "+dropdown.getSelected());
	var req = new XMLHttpRequest();
	req.open("PUT", "http://student02.cse.nd.edu:40001/recommendations/"+user_id, true);
	req.onload = function() {
		console.log("Added rating to db");
	}
	var data = { "movie_id": movie_id, "rating": dropdown.getSelected(), "apikey": "AaD72Feb3" };
	//req.setRequestHeader("Content-Type", "application/json");
	req.send(JSON.stringify(data));
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
voteButton.addClickEventHandler(voteHandler, dropdown);

//Add label and button to document
label.addToDocument();
button.addToDocument();
rating.addToDocument();
dropdown.addToDocument();
voteButton.addToDocument();
