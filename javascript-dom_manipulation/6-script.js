// Task 6: Star Wars character
// Fetch character name from SWAPI and display in #character
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(response => response.json())
  .then(data => {
    document.getElementById('character').textContent = data.name;
  });
