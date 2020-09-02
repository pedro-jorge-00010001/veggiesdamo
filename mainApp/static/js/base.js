"use strict";
var btn = document.getElementById("nav-l");
var lastScrollTop = 0;
var	navbar = document.getElementById("navbar");

window.addEventListener("scroll", function(){
	var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
	if (scrollTop > lastScrollTop){
		navbar.style.top = "-80px";
	}else{
		navbar.style.top="0";	
	}
	lastScrollTop = scrollTop;
})
/* yt Online Tutorials*/

function navAppear() { 
  if (btn.style.display === "none") {
    btn.style.display = "flex";
  } else {
    btn.style.display = "none";
  }
}

window.addEventListener("resize", () => {
	btn.style.display = "flex";
});