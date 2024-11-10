//Collapsibles 
var coll = document.getElementsByClassName("collapsible");
console.log(coll)
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    console.log(content)
    
    if (content) {
        if (content.style.display === "grid") {
          content.style.display = "none";
        } else {
          content.style.display = "grid";
        }
      } else {
        console.warn("No next sibling found for this element.");
      }
    });
}

