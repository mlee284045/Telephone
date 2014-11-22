function profileController($scope, $http) {
    $scope.profile = {};
    var num = localStorage['id'];
    $scope.editMode = true;
    // You did a good job putting some api calls into services/factories, these could also be in one too
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
            if (!$scope.profile.picture) {
                $scope.path = 'media';
            } else {
                $scope.path = 'img';
                $scope.profile.picture = 'default-profile-photo.png';
            }
        }).
        error(function(err) {
            console.log(err);
            $scope.path = 'img';
            $scope.profile.picture = 'default-profile-photo.png';
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
