/* script that toggles the class of the HTML tag HEADER
   The HEADER tag must always have one class: red or green
   never both in the same time, never empty.
 */

$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
