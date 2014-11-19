function profileController($scope, $http) {
    var num = 2;
    $scope.editMode = true;
    $http.get('api/users/'+ num + '/').
        success(function(res) {
            console.log(res);
            $scope.user = res;
            $scope.user.email = 'testing@test.com';
        }).
        error(function(err) {
            console.log(err);
    });


    $scope.toggleEdit = function() {
        $scope.editMode = !$scope.editMode;
    }
}