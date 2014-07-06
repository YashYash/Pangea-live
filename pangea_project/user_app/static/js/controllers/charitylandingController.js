/**
 * Created by yash on 7/6/2014.
 */
/**
 * Created by yash on 7/6/2014.
 */
user_landing_app.controller('charitylandingController', function($scope, $http, $routeParams, $sce, $location) {

    console.log($routeParams);
    console.log("hello");

    $http.get('/api/v1/charity/' + $routeParams.id + '?format=json').success(function (data) {

        console.log(data);
        $scope.charity = data;


        for (var i = 0; i < data.length; i++) {
            data[i].trusted_url = $sce.trustAsResourceUrl(data.all[i].video_url);
            console.log(data[i].trusted_url);

        }
    });

});
