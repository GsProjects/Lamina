function animal_paths()
{
    event.preventDefault();    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/analyse_paths",
            type: 'POST',
            data: $('#select_form').serialize(),
            async: true})
            .done(function(response) {
                var result = JSON.parse(response);
                console.log(result);
                if(result['status'])
                    {
                        if (result['status'] == 'No Animal Selected')
                            {
                                bootbox.alert("Please Select An Animal", function()
                                    {
                                        window.location.replace("select_animal.html");
                                    })
                            }
                        if (result['status'] == 'Your session has timed out, please log in again')
                            {
                                bootbox.alert("Your session has timed out, please log in again", function()
                                    {
                                        window.location.replace("index.html");
                                    })
                            }
                        if (result['status'] == 'No Date Selected')
                            {
                                bootbox.alert("No Date Selected. Please select a date.",function()
                                    {
                                        window.location.replace("select_animal.html");
                                    })
                            }  
                    }
                else
                {
                    process_path_data(response);
                    window.location.replace ("analyseLocation.html");
                }
    
        })        
};
function back()
{
    window.location.replace ("home.html");
};
function process_path_data(location_paths)
{
    window.localStorage.setItem("analyse_coordinates", location_paths);
}
