function update_gps()
{
        event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_gps",
            type: 'GET',
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
                        if(result["status"] == "No animals")
                            {
                                bootbox.alert("You need to add an animal to your account to configure the gps",function()
                                    {
                                        window.location.replace("addAnimalProfile.html");
                                    })
                            }
                    }
                else
                    {
                        window.localStorage.setItem("associated_animals", JSON.stringify(result));
                        window.location.replace("gpsConfiguration.html");
                    }
            
                
               
        })
}
