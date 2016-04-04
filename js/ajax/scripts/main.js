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
Div.prototype = new Item();

//Instantiate the four objects
upButton = new Button();
downButton = new Button();
titleLabel = new Label();
ratingLabel = new Label();
image = new Image();
div = new Div();

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
upButton.createButton("UP", "upButton");
downButton.createButton("DOWN", "downButton");
image.createImage("image");
div.createDiv("hContainer");

//Add classes
titleLabel.addClass("item");
ratingLabel.addClass("item");
upButton.addClass("item");
downButton.addClass("item");
image.addClass("item");

//Set up buttons handlers
args = [ titleLabel, ratingLabel, image, image_path ];
upButton.addClickEventHandler(rateMovie, args.concat([5]));
downButton.addClickEventHandler(rateMovie, args.concat([1]));

//Add elements to document
titleLabel.addToDocument();
div.addToDocument();
ratingLabel.addToDocument();

upButton.addToNode(div);
image.addToNode(div)
downButton.addToNode(div);

getNewMovie(args);
