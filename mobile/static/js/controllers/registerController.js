function registerController($scope, UserApi) {
    $scope.registerUser = function() {
        console.log('registered');
        UserApi.users.create($scope.user)
    }
}