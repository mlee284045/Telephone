telephone.factory('telephoneFactory', function($http, User) {
    return {
        startMessage: function(callback) {
            $http.post('/api/telephones/', data).
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
});