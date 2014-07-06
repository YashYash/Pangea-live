charity_dashboard_app.controller('charityfullController', function($scope, $http) {

    console.log("charityfullController is working");
    $http.get('/api/v1/giver_full?format=json').success(function (data) {
        console.log(data);
        console.log(data.objects);
        $scope.givers = data.objects;
        $scope.charities = $scope.givers.charities;
        console.log($scope.charities);
        console.log($scope.givers);



    });


});

