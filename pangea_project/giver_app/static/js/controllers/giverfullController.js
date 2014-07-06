/**
 * Created by yash on 7/6/2014.
 */
giver_dashboard_app.controller('giverfullController', function($scope, $http) {

    console.log("giverfullController is working");
    $http.get('/api/v1/charity_full?format=json').success(function (data) {
        console.log(data);
        console.log(data.objects);
        $scope.charities = data.objects;
        $scope.giver_info = data.objects.charity.givers;
        console.log($scope.giver_info);
    });

});

