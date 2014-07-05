var charity_dashboard_app = angular.module('charity_dashboard_app', ['ngRoute']);

charity_dashboard_app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/views/templates/charity_analytics.html',
        controller: 'charityController'
    });


}]);

