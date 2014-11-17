function startController($scope, $http) {
    console.log('start');
    $scope.getSound = function() {
        $http.jsonp('http://tts-api.com/tts.mp3?q=' + $scope.text + '&return_url=1', {'Content-Type': 'text/plain', 'responseType': 'text'}).
            success(function(res) {
                console.log('worked');
//                console.log(res);
            }).
            then(function(err) {
//                console.log(err.data);
                console.log(err.status);
                console.log(err.headers);
                console.log(err.config);
                console.log(err.statusText);
            });
    }
}