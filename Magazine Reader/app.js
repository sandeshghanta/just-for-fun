var app = angular.module('myApp', ['ngRoute']);

app.config(['$routeProvider',
function($routeProvider) {
    $routeProvider.
        when('/dashboard', {
            templateUrl: 'Templates/dashboard.html',
        }).
        when('/reader',{
            templateUrl: 'Templates/reader.html'
        }).
        otherwise({
            redirectTo: '/dashboard'
        });        
}]);

app.controller('MainCtrl', function ($scope, $http,  $location) {
    $scope.books = [];
    $http.get('data.json').then(function (response) {

        $scope.data = response.data;
        for (var key in response.data) {
            $scope.books.push({name: key,data:response.data[key]});
        }

        $scope.currentBook = $scope.books[0];
        $scope.currentPage = 0;

    });

    document.onkeydown = checkKey;
    
    function checkKey(e){
         if(e.keyCode == '37'){
             $scope.previousPage();
         }
         else if(e.keyCode == '39'){    
             $scope.nextPage();
         }

         $scope.$apply();
    }

    $scope.bookChange = function(book){
        $scope.currentBook = book;
        $scope.currentPage = 0;
    };

    $scope.nextPage = function(){
        if($scope.currentPage + 1 < $scope.currentBook.data.length){
            $scope.currentPage++;
            Materialize.fadeInImage('#page')
        }
        else{
            alert('book completed');
        }
    };


    $scope.previousPage = function(){
        if($scope.currentPage - 1 >= 0){
            $scope.currentPage--;
            Materialize.fadeInImage('#page')            
        }
    }

    $scope.read = function(book){
        $scope.currentBook = book;
        $scope.currentPage = 0;
        $location.path('/reader');
    }
   
});