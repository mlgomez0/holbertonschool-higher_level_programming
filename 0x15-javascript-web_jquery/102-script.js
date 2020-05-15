/* script that fetches and prints how to say
   “Hello” depending of the language
 */
document.addEventListener('DOMContentLoaded', function () {
  $(document).ready(function () {
    $('#btn_translate').click(function () {
      const languaje = $('#language_code').val();
      const url = 'https://fourtonfish.com/hellosalut/?lang=' + languaje;
      $.get(url, function (data) {
        $('#hello').text(data.hello);
      });
    });
  });
});
