var charity_dashboard_app = angular.module('charity_dashboard_app', ['ngRoute']);

charity_dashboard_app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/views/templates/charity_partners.html',
        controller: 'charityfullController'
    });
    $routeProvider.when('/charity/:id', {
        templateUrl: '/static/views/templates/charity_details.html',
        controller: 'charityController'
    });
    $routeProvider.when('/charity/analytics/:id', {
        templateUrl: '/static/views/templates/charity_analytics.html',
        controller: 'charityController'
    });
    $routeProvider.when('/charity/account/:id', {
        templateUrl: '/static/views/templates/charity_account.html',
        controller: 'charityaccountController'
    });

}]);

