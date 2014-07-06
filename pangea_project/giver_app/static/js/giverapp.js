var giver_dashboard_app = angular.module('giver_dashboard_app', ['ngRoute']);

giver_dashboard_app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/views/templates/giver_partners.html',
        controller: 'giverfullController'
    });
    $routeProvider.when('/giver/:id', {
        templateUrl: '/static/views/templates/giver_details.html',
        controller: 'giverController'
    });
    $routeProvider.when('/giver/analytics/:id', {
        templateUrl: '/static/views/templates/giver_analytics.html',
        controller: 'giverController'
    });

}]);
