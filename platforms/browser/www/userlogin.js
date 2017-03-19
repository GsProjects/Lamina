function userlogFunction()
{
    event.preventDefault();
        $.ajax({
            url: "http://gProject.pythonanywhere.com/userlogin",
            data: $('#loginForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
                var loggedIn = "successful";
                var wrongPass = "Incorrect Password";
                var empty = "Empty fields";
                var wrongUserName = "Incorrect user name";
                var newPassMatch = "The new passwords do not match";

            
                if (result["status"] == loggedIn) 
                {
                    bootbox.alert("Login successful", function()
                        {
                            window.location.replace("home.html");
                        })
                   
                } 
                else if(result["status"] == wrongPass) 
                {
                    bootbox.alert("The password is incorrect", function()
                        {
                            window.location.replace ("Login.html");
                        })
                   
                }
                else if(result["status"] == empty)
                {
                    
                    bootbox.alert("Please fill in all the fields", function()
                        {
                            window.location.replace ("Login.html");
                        })
                
                }
                else if(result["status"] == wrongUserName)
                {
                    bootbox.alert("The user name is incorrect", function()
                        {                       
                            window.location.replace ("Login.html");
                        })
                
                }       
        })
        
};

function back()
{
    window.location.replace ("index.html");
};