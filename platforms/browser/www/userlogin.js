function userlogFunction()
{
    event.preventDefault();
    console.log("In login");
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
                    alert("Login successful");
                     window.location.replace("home.html");
                   
                } 
                else if(result["status"] == wrongPass) 
                {
                    alert("The password is incorrect");
                    window.location.replace ("Login.html");
                   
                }
                else if(result["status"] == empty)
                {
                    alert("Please fill in all the fields");
                    window.location.replace ("Login.html");
                
                }
                else if(result["status"] == wrongUserName)
                {
                    alert("The user name is incorrect");
                    window.location.replace ("Login.html");
                
                }
                
        })
        
};

function back()
{
    window.location.replace ("index.html");
};