/**
 * Created by yash on 7/6/2014.
 */
$( document ).ready(function() {
    console.log( "ready!" );

  $('#test').on( "click", function() {
    $('#test').toggleClass("red blue");
  });

});