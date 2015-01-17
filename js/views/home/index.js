define([
'jquery',
'underscore',
'backbone',
'mustache'
], function($,_,Backbone) {
    var exports = Backbone.View.extend({
        el: '.kimono-home',
        events: {
            'submit .kimono-query': 'queryAPI'
        },
        initialize: function() {
            console.log("HELLO WORLD");
        },
        queryAPI: function(e) {
        },
        render: function(e) {
        }
    });
    return exports;
});
