/*global angular:true */
(function () {
  'use strict';
  angular.module('rethinkDBWorkshop', [
      'ui.router',
      'rethinkDBWorkshop.services',
      'rethinkDBWorkshop.messages'
    ])
    .config(function ($stateProvider, $urlRouterProvider) {
      $urlRouterProvider.otherwise('/');
      $stateProvider
        .state('main', {
          templateUrl: '/static/app/main/main.html',
          url: '/'
        });
      });
})();
