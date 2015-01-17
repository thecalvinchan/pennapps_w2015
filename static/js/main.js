require.config({
    paths: {
        //tries to load jQuery from Google's CDN first and falls back
        //to load locally
        "jquery": ["http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min",
                    "../bower_components/jquery/src/jquery"],
        "underscore": "../bower_components/underscore/underscore-min",
        "backbone": "../bower_components/backbone/backbone",
        "mustache-source": "../bower_components/mustache/mustache.min.js",
        "mustache": "../bower_components/mustache/wrappers/jquery/mustache.js.post"
    },
    shim: {
        "backbone": {
                        //loads dependencies first
            deps: ["jquery", "underscore"],
                        //custom export name, this would be lowercase otherwise
            exports: "Backbone"
        },
        "mustache": {
            deps: ["jquery", "mustache-source"]
        }
    },
        //how long the it tries to load a script before giving up, the default is 7
    waitSeconds: 10,
    catchError: true
});


var route = window.location.pathname;
var queryParams = route.indexOf('?') === -1 ? null : route.indexOf('?');
if (queryParams) {
    route = route.substring(1,queryParams);
} else {
    route = route.substring(1);
}
route = route.split('/');
if (route[0] == '') {
    route = [];
}
var controller = route.length > 0 ? route[0] : 'home';
    action = route.length > 1 ? route[1] : 'index';

var routeView = ['views',controller,action].join('/');

var dependencies = [
    'jquery',
    'underscore',
    'backbone',
    'views/common/index'
];

function init($, _, Backbone, Common) {
    //Common.initialize();
}

require(dependencies.concat(routeView), function() {
    init.apply(this, arguments);
    new (Array.prototype.pop.call(arguments));
}, function(err) {
    var failedId = err.requireModules && err.requireModules[0];
    if (failedId === routeView) {
        requirejs.undef(failedId);
        require(dependencies, function() {
            init.apply(this, arguments);
        });
    }
});
