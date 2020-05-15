/* script that dds the class red to the HTML tag HEADER */

$(document).ready(function () {
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
