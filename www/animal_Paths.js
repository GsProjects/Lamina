function animal_paths()
{
    event.preventDefault();    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/analyse_paths",
            type: 'POST',
            data: $('#select_form').serialize(),
            async: true})
            .done(function(response) {
                console.log(response);
                var result = JSON.parse(response);
            
                if(result['status'])
                    {
                        if (result['status'] == 'No Animal Selected')
                            {
                                alert("Please Select An Animal")
                                window.location.replace("select_animal.html");
                            }
                        if (result['status'] == 'Your session has timed out, please log in again')
                            {
                                alert("Your session has timed out, please log in again")
                                window.location.replace("index.html");
                            }
                        
                    }
                else
                {
                    process_path_data(result)
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
    window.localStorage.setItem("analyse_coordinates", JSON.stringify(location_paths));
}
