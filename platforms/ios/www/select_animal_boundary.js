function get_animal()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals",
            type: 'GET',
            async: false})
            .done(function(response) {
                var result = JSON.parse(response);
                if(result['status'])
                    {
                        if (result["status"] == "Your session has timed out, please log in again") 
                            {
                                bootbox.alert("Your session has timed out, please log in again",function()
                                    {
                                        window.location.replace("index.html");
                                    })
                            } 
                        if(result["status"] == "No animals")
                            {
                                bootbox.alert("No animals associated with your account",function()
                                    {
                                        window.location.replace("addAnimalProfile.html");
                                    })
                            }
                    }
                else
                    {
                        window.localStorage.setItem("boundary_animals", JSON.stringify(result));
                        window.location.replace("create_boundary.html");
                    }    
        })
}