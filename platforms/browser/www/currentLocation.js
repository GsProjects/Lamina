function animal_location()
{
    //event.preventDefault();
    console.log("In currentLocation.js");
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/currentLocation",
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
                console.log("result")
            
                
        })
        
};
function back()
{
    window.location.replace ("home.html");
};