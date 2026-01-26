// Task 7: Star Wars movies
// Fetch all movie titles from SWAPI and list them in #list_movies
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const listMovies = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      listMovies.appendChild(li);
    });
  });
