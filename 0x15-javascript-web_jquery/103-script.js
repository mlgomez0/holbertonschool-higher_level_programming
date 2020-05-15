/* script that fetches and prints how to say
   “Hello” depending of the language supports click and enter
 */
document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    function translate () {
      const languaje = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + languaje;
      $.get(url, function (data) {
        $('#hello').text(data.hello);
      });
    }
    $('#btn_translate').click(function () {
      translate();
    });
    $('#language_code').keypress(function (event) {
      const keycode = (event.keyCode ? event.keyCode : event.which);
      if (keycode == '13') {
        translate();
      }
    });
  });
});
