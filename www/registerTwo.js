
function register()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/register",
            data: $('#registerForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);
                //alert("RESPONSE: " + response);
                //console.log("THE ORIGINAL RESPONSE" + response);
                var result = JSON.parse(response);
                //var ok = "ok";
                //var exists = "Username already exists";
                //var emptyFields = "Empty fields";
                
                //console.log("The response from api was: "+result["status"]);
            
                if (result["status"] == "ok") 
                {
                    console.log("yurt 1");
                    alert("Registration successful");
                     window.location.replace("home.html");
                   
                } 
                else if(result["status"] == "Username already exists") 
                {
                    console.log("yurt 2" + result["status"]);
                    alert("The user name already exists please try again");
                    window.location.replace ("register.html");
                   
                }
                else if(result["status"] == "Empty fields")
                {
                    console.log("yurt 3");
                    alert("Please fill in all the fields");
                    window.location.replace ("register.html");
                
            }
        })
        
};
function back()
{
    window.location.replace ("index.html");
};

