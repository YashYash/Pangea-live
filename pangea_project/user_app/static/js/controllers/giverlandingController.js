/**
 * Created by yash on 7/6/2014.
 */

user_landing_app.controller('giverlandingController', function($scope, $http, $routeParams, $sce, $location) {
    console.log($routeParams);

    $http.get('/api/v1/giver/' + $routeParams.id + '?format=json').success(function (data) {
        console.log(data);
        $scope.giver = data;
        console.log($scope.giver);
        console.log($scope.giver.video_url);
        $scope.giver.trusted_url = $sce.trustAsResourceUrl($scope.giver.video_url);
        console.log($scope.giver.trusted_url);

    });
});