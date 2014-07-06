/**
 * Created by yash on 7/6/2014.
 */


user_landing_app.controller('landingController', function($scope, $http, $routeParams, $sce, $location) {

    console.log("landingController is working");
    console.log($routeParams.id);
    $http.get('/api/v1/charity_full').success(function (data) {
        console.log("DATA");
        console.log(data);
        $scope.all = data.objects;
        console.log($scope.all);

        for (var i = 0; i < $scope.all.length; i++) {
            $scope.all[i].trusted_url = $sce.trustAsResourceUrl($scope.all[i].video_embed);
            console.log($scope.all[i].trusted_url);
            $scope.random = function () {
                return Math.random();
            };
            $scope.all[i].random_giver = $scope.all[i].charity.givers[Math.floor(Math.random() * $scope.all[i].charity.givers.length)];
        }


    });

});
