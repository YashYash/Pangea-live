/**
 * Created by yash on 7/6/2014.
 */
charity_dashboard_app.controller('charityaccountController', function($scope, $http, $routeParams) {

    console.log("charityController is working");
    console.log($routeParams.id);
    $http.get('/api/v1/charity/' + $routeParams.id + '?format=json').success(function (data) {
        console.log("DATA");
        console.log(data);
        $scope.charity = data;


    });



});
