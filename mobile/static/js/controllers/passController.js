function passController($scope, $http) {
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
}