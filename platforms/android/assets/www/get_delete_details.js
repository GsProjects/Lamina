function delete_details()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals",
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
                        window.localStorage.setItem("delete_animals", JSON.stringify(result));
                        window.location.replace("delete_animal.html");
                    }   
        })
}