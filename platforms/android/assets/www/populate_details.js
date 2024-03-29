function populate_animals()
{   
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/get_animal_data",
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
                                bootbox.alert("No animals associated with your account",function()
                                    {
                                        window.location.replace("addAnimalProfile.html");
                                    })
                            }
                    }
                else
                    {
                        window.localStorage.setItem("animals", JSON.stringify(result));
                        window.location.replace("myprofile.html");
                    }  
        })
}