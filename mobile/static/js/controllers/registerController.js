function registerController($scope, Api) {
    $scope.register = function() {
        Api.users.create($scope.user)
    }
}