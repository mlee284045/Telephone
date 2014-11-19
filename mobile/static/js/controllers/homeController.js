function homeController($scope, $location, $rootScope) {
    $rootScope.cornerText = 'Login';
    $rootScope.cornerUrl = '/#/Login/';

    console.log('home');
    $scope.login = function() {
        $location.path('/login/');
    };

    $scope.register = function() {
        $location.path('/register/');
    };

}