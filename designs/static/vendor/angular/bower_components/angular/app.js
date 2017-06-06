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
        document.getElementById('submitIcon').classList.add("fa-spinner fa-pulse fa-3x fa-fw");
        document.getElementById('submit').innerHTML = "&nbsp;&nbsp;Sending...";
    }

    $scope.check = function(value) {
        
        if (value) {
            $scope.disableButton();
        }
    }
});

})(window.angular);