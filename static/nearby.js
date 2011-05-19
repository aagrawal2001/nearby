$(document).ready(function() { 
  if (geo_position_js.init()) {
    $('#globe').html('Your browser supports geolocation.<br><a href="">Click here to find stuff near you!</a>');
    $('a').click(function(e) {
      e.preventDefault();
      $("#toplist").text("Trying to find your location...");
      geo_position_js.getCurrentPosition(geo_success, geo_error, {enableHighAccuracy:true});
    });
  } else {
    $('#globe').html('Your browser does not support geolocation.');
  }
});

function geo_success(p) {
    /*
    var center = new google.maps.LatLng(p.coords.latitude, p.coords.longitude);
    var mapOptions = {
      zoom: 14,
      center: center,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("globe"), mapOptions);
    var marker = new google.maps.Marker({
      position: center,
      title: "You are here"
    });
    marker.setMap(map);
    */
    $("#toplist").text("Searching for cool stuff near you...");
    var url = '/search/' + p.coords.latitude + '/' + p.coords.longitude;
    $.getJSON(url, function(data) {
	    var items = [];

	    $("#toplist").text("");
	    $("<p>Top 10 businesses near you</p>").appendTo("#toplist");
	    $.each(data.businesses, function(i, b) {
		    $('<ul>' + '<img src="' + b.rating_img_url + '"></img>' + '<a href="' + b.url + '">' + b.name + '</a></ul>').appendTo("#toplist");
		});
    });

    //    alert("Found you at latitude " + p.coords.latitude +
    //    ", longitude " + p.coords.longitude);
}


function geo_error() {
  alert("Could not find you!");
}



