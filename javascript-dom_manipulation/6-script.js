// Script that fetches the character name from the Star Wars API and displays it in the HTML tag with id character
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  })
  .catch(error => {
    console.error('Error:', error);
  });



