/* script that fetches and prints how to say
   “Hello” depending of the language
 */

$(document).ready(function () {
  const languaje = $('#language_code').val();
  const url = 'https://fourtonfish.com/hellosalut/?lang=' + languaje;
  $.get(url, function (data) {
    $('#btn_translate').click(function () {
      $('#hello').text(data.hello);
    });
  });
});
