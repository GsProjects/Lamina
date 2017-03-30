function update_details()
{
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals_details",
            data: $('#updateProfileForm').serialize(),
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
                        if (result["status"] == "Updated Successfully") 
                            {
                                bootbox.alert("Animal details updated successfully",function()
                                    {
                                        window.location.replace("home.html");
                                    })
                            } 
                        if (result["status"] == "Wrong gender") 
                            {
                                bootbox.alert("Animal gender must be M or F",function()
                                    {
                                        window.location.replace("update_animal_profile.html");
                                    })
                            } 
                        if (result["status"] == "Empty fields") 
                            {
                                bootbox.alert("Please fill in all the fields",function()
                                    {
                                        window.location.replace("update_animal_profile.html");
                                    })
                            }
                        if (result["status"] == "Tracking number already in use") 
                            {
                                bootbox.alert("Tracking number already in use.",function()
                                    {
                                        window.location.replace("update_animal_profile.html");
                                    })
                            } 
                        if (result["status"] == "Animal ID associated with another animal") 
                            {
                                bootbox.alert("Animal ID associated with another animal",function()
                                    {
                                        window.location.replace("update_animal_profile.html");
                                    })
                            }      
                    }                  
        })
}