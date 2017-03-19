function remove_animal()
{
    event.preventDefault();

    $.ajax({
            url: "http://gProject.pythonanywhere.com/delete_details",
            data: $('#delete_form').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);
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
                        if (result["status"] == "Animal profile deleted successfully") 
                            {
                                bootbox.alert("Animal profile deleted successfully",function()
                                    {
                                        window.location.replace("home.html");
                                    })
                            } 
                        if (result["status"] == "Empty fields") 
                            {
                                bootbox.alert("Please select an animal",function()
                                    {
                                        window.location.replace("delete_animal.html");
                                    })
                            }
 
                    }                  
        })
}