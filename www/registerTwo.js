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
                    bootbox.alert("Registration successful",function()
                        {
                            window.location.replace("home.html");
                        }) 
                } 
                else if(result["status"] == "Username already exists") 
                {
                    bootbox.alert("The user name already exists please try again",function()
                        {
                            window.location.replace ("register.html");
                        })                  
                }
                else if(result["status"] == "Empty fields")
                {
                    bootbox.alert("Please fill in all the fields",function()
                        {
                            window.location.replace ("register.html");
                        })               
            }
            else if(result["status"] == "You are already logged in as another user")
                {
                    bootbox.alert("You are already logged in as another user",function()
                        {
                            window.location.replace ("index.html");      
                        })
            }
        })
        
};
function back()
{
    window.location.replace ("index.html");
};

