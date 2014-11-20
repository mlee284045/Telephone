function passController($scope, $http, $location) {
    var num = 2;
    $scope.onlyOnce = true;
    $http.get('api/telephones/' + num + '/').
        success(function(res) {
            console.log(res);
            $scope.telephone = res;
        }).
        error(function(err) {
            console.log(err);
    });
    $scope.playAudio = function() {
        console.log('clicked play');
        var audio = document.getElementById('telephone');
        audio.play();
        $scope.onlyOnce = false;
    };
    $scope.createSound = function() {
        var data = {
            "text": $scope.text,
            "owner": 1
        };
        $http.post('api/telephones/' + num + '/pass_it_on/', data).
            success(function(res) {
                $location.path('/success/');
            }).
            error(function(err) {
                console.log(err);
            })
        ;
    };
}