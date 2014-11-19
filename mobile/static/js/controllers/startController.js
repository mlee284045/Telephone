function startController($scope, $http) {
    console.log('start');

    $scope.audio = true;

    $http.get('/api/users/');

    $scope.getSound = function(user) {
        var data = {
            "text": $scope.text,
            "owner": user
        };
        $http.post('/api/telephone/', data).
            success(function(res) {
                console.log('worked');
                console.log(res);
            }).
            error(function(err) {
                console.log('did not work');
                console.log(err);
        });
    }
}