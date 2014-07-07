/**
 * Created by yash on 7/6/2014.
 */



$(document).ready(function() {
  console.log("this is working");
  $("#show-form").click(function () {
      $("#overlay-black").fadeIn();
      $(".signin-form").fadeIn();
  });

  $("#overlay-black").click(function () {
      $("#overlay-black").fadeOut();
      $(".signin-form").fadeOut();
      window.location.href = '/';
  });

    $(".hide-overlay").click(function () {
        $("#overlay-black").fadeOut();
        $(".signin-form").fadeOut();

    })
});

