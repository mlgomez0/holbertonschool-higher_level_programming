/* script that updates the text color of the HTML
   tag HEADER to red (#FF0000) when user click on "Red header" */

$('#red_header').click(function () {
  $('header').css({ color: '#FF0000' });
});
