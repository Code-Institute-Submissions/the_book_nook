  $(document).ready(function () { 
      $(".like").click(function(){
      $(this).toggleClass("heart");
      });
  });

  $(document).ready(function() {
setTimeout(function() {
    $('.flash').fadeOut('slow');
}, 2000);
});