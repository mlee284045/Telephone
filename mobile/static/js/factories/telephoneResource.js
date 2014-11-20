telephone.factory('TelephoneApi', function($resource) {
    function send_auth_header(data, headersGetter) {
        var headers = headersGetter();
        headers['Authorization'] = localStorage['Authorization'];
        console.log(data);
    }
    return $resource('/api/telephones/', {}, {
        create: {method: 'POST', transformRequest: send_auth_header}
    });
});