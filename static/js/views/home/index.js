define([
'jquery',
'underscore',
'backbone',
'hello'
], function($,_,Backbone) {
    var exports = Backbone.View.extend({
        el: '.kimono-home',
        events: {
            'submit .kimono-query': 'queryAPI',
            'mouseenter .kimono-steps .button i': 'showTooltip',
            'mouseleave .kimono-steps .button i': 'hideTooltip'
        },
        initialize: function() {
            hello.init({
                twitter: '3Sk0imwAY6KS5si5T6msfkteK'
            },{
              redirect_uri: '/'
            });
            hello.on('auth.login', function(auth){
    
                // call user information, for the given network
                hello( auth.network ).api( '/me' ).then( function(r){
                    // Inject it into the container
                    var label = document.getElementById( "profile_"+ auth.network );
                    if(!label){
                        label = document.createElement('div');
                        label.id = "profile_"+auth.network;
                        document.getElementById('profile').appendChild(label);
                    }
                    label.innerHTML = '<img src="'+ r.thumbnail +'" /> Hey '+r.name;
                });
            });
        },
        queryAPI: function(e) {
        },
        render: function(e) {
        },
        showTooltip: function(e) {
            this.$('.kimono-content').hide();
            this.$('.kimono-content').hide();
            var id = this.$(e.target).attr('data-target');
            this.$('#'+id).css({
                'display': 'block'
            });
        },
        hideTooltip: function(e) {
            //this.$('.kimono-content').hide();
        }
    });
    return exports;
});
