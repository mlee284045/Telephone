function loginController($scope, UserApi, $location) {
    if (localStorage['Authorization']) {
        $location.path('/home/')
    }
    $scope.loginUser = function() {
        console.log('Logging in');
        UserApi.auth.login($scope.user).
            $promise.
            then(function(res) {
                localStorage['id'] = res.id;
            });
        $location.path('/home/')
    }
}