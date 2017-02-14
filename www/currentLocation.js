function animal_location()
{
    //event.preventDefault();
    console.log("In currentLocation.js");
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/currentLocation",
            type: 'GET',
            async: true})
            .done(function(response) {
                console.log(response);
                process_data(response)
                window.location.replace ("currentLocation.html");
            
                
        })
        
};
function back()
{
    window.location.replace ("home.html");
};
function process_data(location_data)
{
    var result = JSON.parse(location_data);
    console.log(result);
    //var coordinates_to_string = result[0].toString();
    var coordinates_to_string = result.toString();
    var coordinate_array = coordinates_to_string.split(",");
    window.localStorage.setItem("coordinates", JSON.stringify(coordinate_array));
  }
