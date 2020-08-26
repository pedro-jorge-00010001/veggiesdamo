"use strict";
var btn = document.getElementById("nav-l");
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