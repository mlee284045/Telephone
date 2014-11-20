function registerController($scope, $http, UserApi, $location) {
    $scope.registerUser = function() {

        console.log('registered');
        UserApi.users.create($scope.user).
            $promise.
            then(function(res) {
                localStorage['id'] = res.id;
                localStorage['Authorization'] = ('Basic ' + btoa($scope.user.username + ':' + $scope.user.password));
                $http.put('api/profile/'+localStorage['id'] + '/', {user:res.id}, {headers: localStorage}).
                    success(function(res) {
                        console.log(res);
                        $location.path('/home/');
                    }).
                    error(function(err) {
                        console.log(err);
                });
            });

    }
}