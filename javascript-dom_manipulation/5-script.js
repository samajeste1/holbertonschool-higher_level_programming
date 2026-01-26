// Task 5: Change the text
// Update header text to "New Header!!!" when clicking #update_header
document.getElementById('update_header').addEventListener('click', function () {
  document.querySelector('header').textContent = 'New Header!!!';
});
