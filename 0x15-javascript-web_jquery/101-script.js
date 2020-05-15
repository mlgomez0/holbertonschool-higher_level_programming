/* script that adds, removes and clears LI elements
   from a list when the user clicks
 */
document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    $('#add_item').click(function () {
      $('ul.my_list').append('<li>Item</li>');
    });
    $('#remove_item').click(function () {
      $('ul.my_list li:last-child').remove();
    });
    $('#clear_list').click(function () {
      $('ul.my_list').empty();
    });
  });
});
