function animal_location()
{
    //event.preventDefault();
    console.log("In currentLocation.js");
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/currentLocation",
            type: 'GET',
            async: true})
            .done(function(response) {
                console.log("YURT");
                console.log(response);

                var result = JSON.parse(response);
                console.log(result);
            
                
        })
        
};
function back()
{
    window.location.replace ("home.html");
};