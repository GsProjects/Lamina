function display_coordinates()
{
    var gps =[];
    var coordinate_array = JSON.parse(window.localStorage.getItem("coordinates"));

    mapboxgl.accessToken = 'pk.eyJ1IjoiZ2FybDk0IiwiYSI6ImNpeTVucXc5YzAwNG0ycW82MTFqeWl5bmQifQ.L3m2Ue3OOucOI3XrhwjUIQ';
                    var map = new mapboxgl.Map({
                        container: 'map', // container id
                        style: 'mapbox://styles/mapbox/satellite-v9', //stylesheet location
                        center: [-6.934135900000001,52.8365072], // starting position longitude followed by latitude
                        zoom: 5 // starting zoom
                    });


    

        map.addLayer({
            "id": "points",
            "type": "symbol",
            "source": {
                "type": "geojson",
                "data": {
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": {
                            "type": "Point",
                            "coordinates": [parseFloat(coordinate_array[1]),parseFloat(coordinate_array[2])]
                        },
                        "properties": {
                            "title": coordinate_array[3],
                            "icon": "dog-park"

                        }
                    }]
                }
            },
            "layout": {
                "icon-image": "{icon}-15",
                "text-field": "{title}",
                "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
                "text-offset": [0, 0.6],
                "text-anchor": "top"
            }
        });
   
    
    
}