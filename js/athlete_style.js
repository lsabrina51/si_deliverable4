function openNav() {
    document.getElementById("nav").style.width = "20vw";
    document.getElementById("nav").style.width = "20vw";
    document.querySelector("main").style.marginLeft= "20vw";
    document.querySelector("footer").style.marginLeft= "20vw";
    document.querySelector("header").style.marginLeft= "20vw";
    document.getElementById("skip").style.marginLeft= "20vw";
    
    //adjusts width
     document.querySelector("main").style.width= "80vw";
     document.querySelector("footer").style.width= "80vw";
     document.querySelector("header").style.width= "80vw";
     document.getElementById("skip").style.width= "80vw";

    document.getElementById("menubtn").style.display= "none";
  }
  
  //main, header, #skip, footer
  function closeNav() {
    document.getElementById("nav").style.width = "0";
    document.querySelector("main").style.marginLeft= "0";
    document.querySelector("footer").style.marginLeft= "0";
    document.querySelector("header").style.marginLeft= "0";
    document.getElementById("skip").style.marginLeft= "0";

    //makes width regular 
    document.querySelector("main").style.width= "100vw";
    document.querySelector("footer").style.width= "100vw";
    document.querySelector("header").style.width= "100vw";
    document.getElementById("skip").style.width= "100vw";

    document.getElementById("menubtn").style.display= "block";
  }

 //loads default image for images that do not load
 document.querySelectorAll('img').forEach(img => {
  img.onerror = function() {
     this.onerror = null; // Prevents infinite loop if default image missing
     this.src = '../images/default_image.jpg';
     this.alt = ""
  };
  });