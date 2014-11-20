var telephone = angular.module('telephone', ['ngRoute', 'ngResource']);

telephone.config(['$routeProvider', function($routeProvider) {
    // Route code will go here
    $routeProvider.
        when('/', {
            templateUrl: '/static/js/views/landing.html',
            controller: landingController
        }).
        when('/start/', {
            templateUrl: '/static/js/views/start.html',
            controller: startController
        }).
        when('/pass/', {
            templateUrl: '/static/js/views/pass.html',
            controller: passController
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
        when('/home/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        }).
        when('/success/', {
            templateUrl: '/static/js/views/success.html',
            controller: successController
        }).
        otherwise({redirectTo: '/home/'});
}]);

telephone.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);