//Name: Cory Jbara

//Item Object
function Item() {
	this.addToDocument = function() {
		document.body.appendChild(this.item);
	}
}

//Label object (inherits from Item)
function Label() {
	this.createLabel = function(text, id) {
		this.item = document.createElement("p");
		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	}

	this.setText = function(text) {
		this.item.innerHTML = text;
	}
}

//Button object (inherits from Item)
function Button() {
	this.createButton = function(text, id) {
		this.item = document.createElement("button");
		this.item.setAttribute("id", id);
		this.item.innerHTML = text;
	}

	this.addClickEventHandler = function(handler, args) {
		this.item.onmouseup = function () { handler(args); };
	}
}

//Dropdown object
function Dropdown() {
	this.createDropdown = function(dict, id, selected) {
		this.item = document.createElement("select");
		this.item.setAttribute("id", id);

		for(r in dict) {
			var option = document.createElement("option"); 
			option.text = dict[r];
			option.value = r;
			if( r == selected ) {
				option.selected = true;
			}
			this.item.options.add(option);
		}
	}

	this.getSelected = function() {
		var options = this.item.options.length;
		for( var i = 0; i < options; i++ ) {
			if( this.item.options[i].selected == true ) {
				console.log( i + 1 );
			}
		}
	}
}
