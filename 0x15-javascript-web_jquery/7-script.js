/*  script that updates the text of the HTML tag HEADER
    to “New Header!!!” when the user clicks on DIV#update_header
 */

$(document).ready(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    $('#character').text(data.name);
  });
});
