function get_animal_data()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/update_animals",
            type: 'GET',
            async: false})
            .done(function(response) {
                console.log("Select_animals.js: " + response);

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
                                alert("No animals associated with your account");
                                window.location.replace("addAnimalProfile.html");
                            }
                    }
                else
                    {
                        window.localStorage.setItem("select_animals", JSON.stringify(result));
                        window.location.replace("select_animal.html");
                    }
            
                
               
        })
}