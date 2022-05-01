var map;
// var src = 'https://drive.google.com/uc?export=download&id=1z5e5V5X5belJhYl05Z9GmPG4-lriB3T2';
// var src = 'https://siata.gov.co/kml/Gestion%20Riesgo/Deslizamiento_Copacabana.kml';
// var src = 'https://dl.dropbox.com/s/zdda1v9wdril1fb/025_OlayaHerrera.kml?dl=0';
var src = document.getElementById('kml').innerHTML;
console.log(src);
// https://siata.gov.co/kml/ preguntar por que no estan los kml


var longitud = document.getElementById('longitud').innerHTML;
var latitud = document.getElementById('latitud').innerHTML;
// console.log(longitud);
// console.log(latitud);
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(longitud, latitud),
        zoom: 18,
        mapTypeId: 'satellite'
    });

    var kmlLayer = new google.maps.KmlLayer(src, {
        suppressInfoWindows: true,
        preserveViewport: false,
        map: map
    });

    kmlLayer.addListener('click', function (event) {
        var content = event.featureData.infoWindowHtml;
        var testimonial = document.getElementById('capture');
        testimonial.innerHTML = content;
    });
}