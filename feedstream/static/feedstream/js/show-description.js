let card  = document.getElementById("card")
let cardClose  = document.getElementById("cardClose")


card.addEventListener("click", () => {
  card.style.transform = "rotateY(180deg)"
})

cardClose.addEventListener("click", (event) => {
  card.style.transform = "rotateY(0deg)";
  event.stopPropagation();
})
