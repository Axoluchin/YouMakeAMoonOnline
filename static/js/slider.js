var slideIndex = 1;
showSlides(slideIndex);
document.getElementById("Fecha").value =
  new Date().getDate() +
  " / " +
  new Date().getMonth() +
  " / " +
  new Date().getFullYear();

function plusSlides(n) {
  showSlides((slideIndex += n));
  document.getElementById("Num").value = slideIndex;
}

function currentSlide(n) {
  showSlides((slideIndex = n));
  document.getElementById("Num").value = slideIndex;
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {
    slideIndex = 1;
    document.getElementById("Num").value = slideIndex;
  }
  if (n < 1) {
    slideIndex = slides.length;
    document.getElementById("Num").value = slideIndex;
  }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}

