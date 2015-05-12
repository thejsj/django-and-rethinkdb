/*global angular:true, moment:true, _:true */
(function () {
  'use strict';

  angular.module('rethinkDBWorkshop.services', [])
    .factory('MessageFactory', MessageFactory);

  MessageFactory.$inject = ['$http', '$state', '$q', '$rootScope'];

  function MessageFactory ($http, $state, $q, $rootScope) {

    var ws = new WebSocket('ws://' + window.config.url + ':' + window.config.ports.http + '/new-messages/');
    var messageCollection = [];

    ws.onopen = function () {
      console.log('Socket Connection Open');
    };

    ws.onmessage = function (evt) {
      var message = JSON.parse(evt.data).new_val;
      console.log('message', message);
      $rootScope.$apply(function () {
        messageCollection.push(message);
      });
    };

    var factory = {
      getMessageCollection: getMessageCollection,
      addMessage: addMessage,
    };

    return factory;

    function getMessageCollection() {
      return $http.get('/messages/')
        .then(function (res) {
          console.log(res);
          res.data.forEach(function (row) {
            messageCollection.push(row);
          });
          return messageCollection;
        });
    }

    function addMessage(text) {
      ws.send(JSON.stringify({
        text: text,
        email: window.config.email,
        created: (new Date()).getTime()
      }));
    }

  }

})();
