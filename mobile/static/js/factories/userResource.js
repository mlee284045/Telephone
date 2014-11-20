telephone.factory('UserApi', function($resource) {
    function add_auth_header(data, headersGetter){
        var headers = headersGetter();
        headers['Authorization'] = ('Basic ' + btoa(data.username + ':' + data.password));
        localStorage['Authorization'] = headers['Authorization'];
    }
    return {
        auth: $resource('/api/auth/', {}, {
            login: {method: 'POST', transformRequest: add_auth_header},
            logout: {method: 'DELETE'}
        }),
        users: $resource('/api/register/', {}, {
            create: {method: 'POST'}
        })
    };
});