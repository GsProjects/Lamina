function remove_animal()
{
    event.preventDefault();

    $.ajax({
            url: "http://gProject.pythonanywhere.com/delete_details",
            data: $('#delete_form').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log("RESPONSE: "+response);

                var result = JSON.parse(response);
                
                if(result['status'])
                    {
                        
                        if (result["status"] == "Your session has timed out, please log in again") 
                            {
                                console.log("session");
                                alert("Your session has timed out, please log in again");
                                 window.location.replace("index.html");

                            }
                        if (result["status"] == "Animal profile deleted successfully") 
                            {
                                console.log("success");
                                alert("Animal profile deleted successfully");
                                 window.location.replace("home.html");

                            } 
                        if (result["status"] == "Empty fields") 
                            {
                                console.log("empty");
                                alert("Please fill in all the fields");
                                 window.location.replace("delete_animal.html");
                            }
 
                    }    
               
        })
}