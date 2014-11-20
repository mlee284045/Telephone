function startController($scope, $http, $location) {
    console.log('start');

    $scope.audio = true;

    $http.get('/api/users/');

    $scope.createSound = function() {
        console.log('creating sound');
        var data = {
            "text": $scope.text,
            "owner": 1
        };
//        var auth['Authorization'] = localStorage['Authorization'];
        console.log(data);
        $http.post('/api/telephones/', data, {headers: localStorage}).
            success(function(res) {
                console.log('worked');
                console.log(res);
                $location.path('/success/');
            }).
            error(function(err) {
                console.log('did not work');
                console.log(err);
        });
    }
}