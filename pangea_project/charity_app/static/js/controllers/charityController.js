charity_dashboard_app.controller('charityController', function($scope, $http, $routeParams) {

    console.log("charityController is working");
    console.log($routeParams.id);
    $http.get('/api/v1/charity/' + $routeParams.id + '?format=json').success(function (data) {
        console.log("DATA");
        console.log(data);
        $scope.charity = data;
        console.log("GIVERS");
        console.log(data.givers);
        $scope.givers = data.givers;
        $scope.videos = data.videos;
        console.log("VIDEOS");
        console.log($scope.videos);
    });

    $http.get('/api/v1/videos?format=json').success(function (data) {
        all_data = data.objects;
        var videos = [];
        for (i=0; i < all_data.length; i++) {
            if (all_data[i].charity.id == $routeParams.id) {
                videos.push({
                    url: all_data[i].video_url,
                    title: all_data[i].title,
                    posted: all_data[i].posted,
                    sortable:true,
                    resizeable:true,
                    charity_name: all_data[i].charity.name
                });

            }
        }
        console.log(videos);
        $scope.videos = videos;
    });

});

