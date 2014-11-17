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
//            This will be shifted into the home page controller
        }).
        when('/login/', {
            templateUrl: '/static/js/views/login.html',
            controller: loginController
        }).
        when('/register/', {
            templateUrl: '/static/js/views/register.html',
            controller: registerController
        }).
        when('/profile/', {
            templateUrl: '/static/js/views/profile.html',
            controller: profileController
        }).
        otherwise({redirectTo: '/'});
}]);