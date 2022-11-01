// document.getElementById("buty").onsubmit = function(){
//     location.reload(true);
// }

$(function () {
    $('#inputform').on('keydown', 'input', function (event) {
      if (event.which == 13) {
        $(this).next('input').focus();
        event.preventDefault();
      }
    });
  });


  