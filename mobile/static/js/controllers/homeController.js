function homeController($scope, $location) {
    console.log('home');
    $scope.message = 'Home Controller Works';

    $scope.login = function() {
        $location.path('/login/');
    };

    $scope.register = function() {
        $location.path('/register/');
    };

}