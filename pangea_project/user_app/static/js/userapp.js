/**
 * Created by yash on 7/6/2014.
 */
var user_landing_app = angular.module('user_landing_app', ['ngRoute']);

user_landing_app.config(['$routeProvider', function ($routeProvider) {
    $routeProvider.when('/', {
        templateUrl: '/static/views/templates/landing_videos.html',
        controller: 'landingController'
    });

    $routeProvider.when('/charity/details/:id', {
        templateUrl: '/static/views/templates/charity_details.html',
        controller: 'charitylandingController'
    });

    $routeProvider.when('/giver/details/:id', {
        templateUrl: '/static/views/templates/giver_details.html',
        controller: 'giverlandingController'
    });

    $routeProvider.when('/charity/likes/:id', {
        templateUrl: '/static/views/templates/likes.html',
        controller: 'likesController'
    });
}]);

