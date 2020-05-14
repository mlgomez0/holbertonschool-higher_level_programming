/*   script that fetches and lists all movies title by using
     this URL: https://swapi-api.hbtn.io/api/films/?format=json
 */

$(document).ready(function () {
  $(function () {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json',
      function (data) {
        $.each(data.results, function (i, movie) {
          $('#list_movies').append($('<li></li>').text(movie.title));
        });
      });
  });
});
