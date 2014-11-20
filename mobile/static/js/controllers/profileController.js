function profileController($scope, $http) {
    var num = localStorage['id'];
    $scope.editMode = true;
    $http.get('api/users/'+ num + '/').
        success(function(res) {
            console.log(res);
            $scope.user = res;
        }).
        error(function(err) {
            console.log(err);
    });
    $http.get('api/profile/'+ num + '/').
        success(function(res) {
            console.log(res);
            $scope.profile = res;
        }).
        error(function(err) {
            console.log(err);
    });



    $scope.toggleEdit = function() {
        var data = {
            user: $scope.profile.user,
            description: $scope.profile.description
        };
        $scope.editMode = !$scope.editMode;
        if ($scope.editMode) {
            $http.put('api/users/'+ num + '/', $scope.user).
                success(function(res) {
                    console.log(res);
                }).
                error(function(err) {
                    console.log(err);
            });
            $http.patch('api/profile/'+ num + '/', data).
                success(function(res) {
                    console.log(res);
                }).
                error(function(err) {
                    console.log(err);
            });
        }
    }
}