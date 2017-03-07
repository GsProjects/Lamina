function get_animals()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals",
            type: 'GET',
            async: false})
            .done(function(response) {
                console.log("RESPONSE"+response);

                var result = JSON.parse(response);
                
                if(result['status'])
                    {
                        if (result["status"] == "Your session has timed out, please log in again") 
                            {
                                alert("Your session has timed out, please log in again");
                                 window.location.replace("index.html");

                            } 
                        if(result["status"] == "No animals")
                            {
                                alert("You need to add an animal to your account to configure the gps");
                                window.location.replace("addAnimalProfile.html");
                            }
                    }
                else
                    {
                        window.localStorage.setItem("associated_animals_update", JSON.stringify(result));
                        window.location.replace("update_animal_profile.html");
                    }
            
                
               
        })
}