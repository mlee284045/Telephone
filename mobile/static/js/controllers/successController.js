function successController($scope, $location) {
    $scope.goHome = function() {
        $location.path('/home/');
    }
}