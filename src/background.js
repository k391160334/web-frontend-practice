const body = document.querySelector("body");
const IMG_NUMBER = 4;

function init() {
  paintImage(generateRand());
}

function paintImage(num) {
  const img = new Image();
  img.src = `images/${num}.jpg`;
  img.classList.add("bgImage");
  body.prepend(img);
}
function generateRand() {
  const rand = Math.ceil(Math.random() * IMG_NUMBER);
  return rand;
}

init();
