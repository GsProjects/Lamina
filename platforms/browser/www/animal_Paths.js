function animal_paths()
{
    //event.preventDefault();
    console.log("In animal_paths.js");
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/analyse_paths",
            type: 'GET',
            async: true})
            .done(function(response) {
                console.log("THE RESPONSE: " + response);
                var result = JSON.parse(response);
                process_path_data(result)
                window.location.replace ("analyseLocation.html");
            
                
        })
        
};
function back()
{
    window.location.replace ("home.html");
};
function process_path_data(location_paths)
{
    window.localStorage.setItem("analyse_coordinates", JSON.stringify(location_paths));
  }
