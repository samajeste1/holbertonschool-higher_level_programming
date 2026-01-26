// Task 2: Add .red class
// Add class 'red' to header when clicking on #red_header
document.getElementById('red_header').addEventListener('click', function () {
  document.querySelector('header').classList.add('red');
});
