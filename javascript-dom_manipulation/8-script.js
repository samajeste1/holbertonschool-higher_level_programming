// Task 8: Say Hello!
// Fetch translation of "hello" in French and display in #hello
// Script works when imported from <head> tag
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    });
});
