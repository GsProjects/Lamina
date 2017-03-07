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
                                alert("Your session has timed out, please log in again");
                                 window.location.replace("index.html");
                            }
                        if (result["status"] == "Updated Successfully") 
                            {
                                alert("Animal details updated successfully");
                                 window.location.replace("home.html");
                            } 
                        if (result["status"] == "Empty fields") 
                            {
                                alert("Please fill in all the fields");
                                 window.location.replace("update_animal_profile.html");
                            }
                        if (result["status"] == "Tracking number already in use") 
                            {
                                alert("Tracking number already in use.");
                                 window.location.replace("update_animal_profile.html");
                            } 
                        if (result["status"] == "Animal ID associated with another animal") 
                            {
                                alert("Animal ID associated with another animal");
                                 window.location.replace("update_animal_profile.html");
                            }      
                    }                  
        })
}