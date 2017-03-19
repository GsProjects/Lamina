function animal_location()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/currentLocation",
            type: 'POST',
            data: $('#select_form').serialize(),
            async: true})
            .done(function(response) {
                console.log(response);
                var result = JSON.parse(response);
                process_data(result)
                window.location.replace ("currentLocation.html");
        })        
};
function back()
{
    window.location.replace ("home.html");
};
function process_data(location_data)
{ 
    window.localStorage.setItem("coordinates", JSON.stringify(location_data));
}
