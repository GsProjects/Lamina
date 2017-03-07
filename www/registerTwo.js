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

                var result = JSON.parse(response);
            
                if (result["status"] == "ok") 
                {
                    alert("Registration successful");
                     window.location.replace("home.html");
                   
                } 
                else if(result["status"] == "Username already exists") 
                {
                    alert("The user name already exists please try again");
                    window.location.replace ("register.html");
                   
                }
                else if(result["status"] == "Empty fields")
                {
                    alert("Please fill in all the fields");
                    window.location.replace ("register.html");
                
            }
            else if(result["status"] == "You are already logged in as another user")
                {
                    alert("You are already logged in as another user");
                    window.location.replace ("index.html");      
            }
        })
        
};
function back()
{
    window.location.replace ("index.html");
};

