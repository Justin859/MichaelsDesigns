(function(angular) {
    'use strict';

var app = angular.module('MyApp', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('MyAppController', function($scope){
    $scope.isDisabled = false;

    $scope.disableButton = function() {
        $scope.isDisabled = true;
        document.getElementById('submit').innerHTML = "Sending...  Please Wait."
    }

    $scope.check = function(value) {
        
        if (value) {
            $scope.disableButton();
        }
    }
});

})(window.angular);