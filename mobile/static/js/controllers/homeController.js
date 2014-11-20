function homeController($scope, $location) {
    if (localStorage['Authorization']) {
        console.log('Authorized')
    } else {
        $location.path('/');
    }
    $scope.goCreate = function() {
        $location.path('/start/');
    };
    $scope.goPass = function() {
        $location.path('/pass/');
    };
    $scope.goProfile = function() {
        $location.path('/profile/');
    };
}