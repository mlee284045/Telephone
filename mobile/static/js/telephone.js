var telephone = angular.module('telephone', ['ngRoute', 'ngResource']);

telephone.config(['$routeProvider', function($routeProvider) {
    // Route code will go here
    $routeProvider.
        when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        }).
        when('/start/', {
            templateUrl: '/static/js/views/start.html',
            controller: startController
        }).
        otherwise({redirectTo: '/'});
}]);