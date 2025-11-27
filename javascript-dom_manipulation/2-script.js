// Script that adds the class red to the header element when the user clicks on the tag with id red_header
document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');
  redHeader.addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
  });
});



