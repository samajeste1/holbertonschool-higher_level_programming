// Script that updates the text of the header element to New Header!!! when the user clicks on the element with id update_header
document.addEventListener('DOMContentLoaded', function () {
  const updateHeader = document.getElementById('update_header');
  updateHeader.addEventListener('click', function () {
    document.querySelector('header').textContent = 'New Header!!!';
  });
});



