var p = document.createElement("p");
p.setAttribute("id", "nameLabel");
var text = document.createTextNode("Who?");
p.appendChild(text);
document.body.appendChild(p);

var button = document.getElementById("theButton");

button.onclick = function changeText() {
  console.log("Clicked");
  document.getElementById("nameLabel").innerHTML = "Cory Jbara";
};
