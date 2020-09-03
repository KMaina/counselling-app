// (function($) {
//     "use strict";

//     // manual carousel controls
//     $('.next').click(function(){ $('.carousel').carousel('next');return false; });
//     $('.prev').click(function(){ $('.carousel').carousel('prev');return false; });
    
// })(jQuery);
$('.design').click(function () {
    $(this).children('.hide').slideToggle(1300);
    $(this).children('.show').slidetoggle(1400);
  });
  $(".card").hover(function () {
    $(this).children(".card-1").fadeToggle(500);
  });

$(document).ready(function(){
  $("#form").submit(function(event){
    event.preventDefault();
    var name = $("input#b_name").val();
    var email = $("input#b_email").val();
    var message = $("textarea#b_comment").val();
    if ($("input#b_name").val() && $("input#b_email").val()){
      alert (name + ", we have received your message. Thank you for reaching out to us.");
    }
    else {
      alert("Please enter your name and email!");
    }
    
  });

});