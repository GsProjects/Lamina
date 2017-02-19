function update_details()
{
    console.log("Update animals details in database");
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals_details",
            data: $('#updateProfileForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log("RESPONSE"+response);

                var result = JSON.parse(response);
                
                if(result['status'])
                    {
                        console.log("IN IF");
                        if (result["status"] == "Your session has timed out, please log in again") 
                            {
                                alert("Your session has timed out, please log in again");
                                 window.location.replace("index.html");

                            }
                        if (result["status"] == "Updated") 
                            {
                                alert("Aniaml details updated successfully");
                                 window.location.replace("home.html");

                            } 
                        if (result["status"] == "Empty fields") 
                            {
                                alert("Please fill in all the fields");
                                 window.location.replace("update_animal_profile.html");
                            } 
                        
                        
                    }    
               
        })
}