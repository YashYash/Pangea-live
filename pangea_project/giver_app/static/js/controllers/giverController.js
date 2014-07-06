giver_dashboard_app.controller('giverController', function($scope, $http, $routeParams) {

    console.log("giverController is working");
    console.log($routeParams.id);
    $http.get('/api/v1/giver/' + $routeParams.id + '?format=json').success(function (data) {
        console.log("DATA");
        console.log(data);
        $scope.giver = data;

    });

});

