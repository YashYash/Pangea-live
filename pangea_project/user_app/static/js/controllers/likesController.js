/**
 * Created by yash on 7/6/2014.
 */

user_landing_app.controller('likesController', function($scope, $http, $routeParams, $sce, $location) {
    console.log("likes controller");
    console.log($routeParams.id);
        $http.get('/api/v1/charity').success(function (data) {});
    $scope.close_window = function(){
        window.close();
    }
});
