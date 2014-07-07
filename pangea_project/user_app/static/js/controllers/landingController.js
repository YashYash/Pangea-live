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
        for (var x = 0; x < $scope.all.length; x++) {
            $scope.all[x].charity.trusted_id = $sce.trustAsResourceUrl($scope.all[x].charity.id);
            console.log($scope.all[i].trusted_id);
        }

    });

    $scope.fliersOnly = function () {
        $scope.searchText = "flying";
    };

    $scope.charityLike = function(charity_id){
        console.log(charity_id);
        $http.get('/api/v1/charity/' + charity_id + "/?format=json").success(function (data) {
            console.log(data);
            var current_likes = data.total_likes;
            var incremented_likes = current_likes + 1;
            $scope.likes = incremented_likes;
            console.log($scope.likes);
            $http.post('/api/v1/charity/' + charity_id + "/?format=json",{"total_likes":1});
            $http.get('/api/v1/charity/' + charity_id + "/?format=json").success(function (data) {
               console.log(data.total_likes);

            });
        });

    };

    $scope.like_popup = function(charity_id){
        window.open("#/charity/likes/"+ charity_id,'targetWindow','toolbar=no,location=no, directories=no, titlebar=no, status=no,menubar=no,scrollbars=on,resizable=no,width=500,height=500');
    }


});
