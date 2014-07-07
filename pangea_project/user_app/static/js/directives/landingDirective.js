/**
 * Created by yash on 7/6/2014.
 */

user_landing_app.directive('myWidget', function(){
	var linkFn;
	linkFn = function(scope,element,attrs) {
		var fadingin, fadingout
		fadingin = function(){
		    $('#overlay-like').fadeIn();
            $(this).next().fadeIn();
		};
		fadingout = function() {
			$('#overlay-like').fadeOut();
            $(".frame-container").fadeOut();
		};
		$(".like").on("click", fadingin);
		$("#overlay-like").on("click", fadingout );
	};

	return {
		restrict:'E',
		 link: linkFn
	}
});
