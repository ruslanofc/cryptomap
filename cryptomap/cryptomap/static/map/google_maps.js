$.getScript( "https://maps.googleapis.com/maps/api/js?key=" + google_api_key + "&callback=initMap&libraries=&v=weekly")
.done(function( script, textStatus ) {
    google.maps.event.addDomListener(window, "load", initMap)
})

function initMap() {
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById("map-route"), {
      center: { lat: 55.7887, lng: 49.1221 },
      zoom: 11,
    });

    directionsDisplay.setMap(map);

    for (i=0; i<markers.length; i++){
        var marker = new google.maps.Marker({
          position: { lat: markers[i][0], lng: markers[i][1] },
          map: map,
          content: '<a href="/shop/'+markers[i][2]+'/">'+ markers[i][3]+'</a>'
        });

        var infowindow = new google.maps.InfoWindow();

        google.maps.event.addListener(marker, 'click', function(){
            infowindow.setContent(this.content;
            infowindow.open(map,this);
        });
    }
}
