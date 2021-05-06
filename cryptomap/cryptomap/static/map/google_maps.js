$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&callback=initMap&libraries=&v=weekly")
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)
})

function initMap() {
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById("map-route"), {
      center: { lat: 51.513416, lng: -0.129761 },
      zoom: 11,
    });
    directionsDisplay.setMap(map);
    var marker = new google.maps.Marker({
      position: { lat: 51.513416, lng: -0.129761 },
      map: map,
      title: "Hello World!",
    });

    var info = new google.maps.InfoWindow({
      content: '<h3>Твое место</h3>'
    });

    marker.addListener("click", function() {
      info.open(map, marker);
    });
}
