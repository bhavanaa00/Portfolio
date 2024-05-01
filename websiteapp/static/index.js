let mobmenu = document.querySelector(".mobmenu");
let cross = document.querySelector(".cross");
let ham = document.querySelector(".ham");
let listItems = document.querySelectorAll(".mobmenu li");

// cross.addEventListener("click", function () {
//   mobmenu.style.display = "block";
//   cross.style.display = "none";
//   ham.style.display = "block";
// });

ham.addEventListener("click", () => {
  mobmenu.style.display = "block";
  // cross.style.display = "block";
  // ham.style.display = "none";
});

listItems.forEach((item) => {
  item.addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent event propagation to the parent elements
    mobmenu.style.display = "none";
    // cross.style.display = "none";
    // ham.style.display = "block";
  });
});
