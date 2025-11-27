// Script that fetches from https://hellosalut.stefanbohacek.com/?lang=fr and displays the value of hello
// This script must work when imported from the <head> tag
document.addEventListener('DOMContentLoaded', function () {
  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});



