// Script that toggles the class of the header element when the user clicks on the tag id toggle_header
document.addEventListener('DOMContentLoaded', function () {
  const toggleHeader = document.getElementById('toggle_header');
  toggleHeader.addEventListener('click', function () {
    const header = document.querySelector('header');
    if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
    } else {
      header.classList.remove('green');
      header.classList.add('red');
    }
  });
});



