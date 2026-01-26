// Task 3: Toggle classes
// Toggle between 'red' and 'green' class on header when clicking #toggle_header
document.getElementById('toggle_header').addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.toggle('red');
  header.classList.toggle('green');
});
