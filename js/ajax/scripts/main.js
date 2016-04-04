//Name: Cory Jbara

//Create the variables
var user_id = 4;
var image_path = "http://www.cse.nd.edu/~cmc/teaching/cse30332_sp16/images";
var movie_id = 0;

//Set up the inheritance
Button.prototype = new Item();
Label.prototype = new Item();
Dropdown.prototype = new Item();
Image.prototype = new Item();

//Instantiate the four objects
upButton = new Button();
downButton = new Button();
titleLabel = new Label();
ratingLabel = new Label();
image = new Image();

//Function gets a new movie then fills the appropriate html info
function getNewMovie(args) {
	console.log("Getting new movie");
	var req = new XMLHttpRequest();
	req.open("GET", "http://student02.cse.nd.edu:40001/recommendations/"+user_id, true);
	req.onload = function() {
		var response = JSON.parse(req.response);
		movie_id = response["movie_id"];
		getMovieInfo(args);
	}
	req.send();
}

//Function gets the movie information
function getMovieInfo(args){
	console.log("Getting info for movie "+movie_id);
	var req = new XMLHttpRequest();
	req.open("GET", "http://student02.cse.nd.edu:40001/movies/"+movie_id, true);
	req.onload = function() {
		var response = JSON.parse(req.response);
		args[0].setText(response["title"]);
		args[2].setImage(args[3]+response["img"]);
		getMovieRating(args);
	}
	req.send();
}

//Function gets the movie information
function getMovieRating(args){
	console.log("Getting rating for movie "+movie_id);
	var req = new XMLHttpRequest();
	req.open("GET", "http://student02.cse.nd.edu:40001/ratings/"+movie_id, true);
	req.onload = function() {
		var response = JSON.parse(req.response);
		args[1].setText(Number(response["rating"]).toFixed(3));
	}
	req.send();
}

//Function to vote on a movie, then calls getNewMovie()
function rateMovie(args) {
	console.log("Rating movie "+movie_id+" with a rating of "+args[4]);
	var req = new XMLHttpRequest();
	req.open("PUT", "http://student02.cse.nd.edu:40001/recommendations/"+user_id, true);
	req.onload = function() {
		console.log("Added rating to db");
		getNewMovie(args);
	}
	var data = { "movie_id": movie_id, "rating": args[4], "apikey": "AaD72Feb3" };
	req.send(JSON.stringify(data));
}

//Create elements
titleLabel.createLabel("Title", "titleLabel");
ratingLabel.createLabel("Rating", "ratingLabel");
upButton.createButton("Up", "upButton");
downButton.createButton("Down", "downButton");
image.createImage("image");

//Set up buttons handlers
args = [ titleLabel, ratingLabel, image, image_path ];
upButton.addClickEventHandler(rateMovie, args.concat([5]));
downButton.addClickEventHandler(rateMovie, args.concat([1]));

//Add label and button to document
titleLabel.addToDocument();
upButton.addToDocument();
image.addToDocument()
downButton.addToDocument();
ratingLabel.addToDocument();

getNewMovie(args);
