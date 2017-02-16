function changePass()
{
    event.preventDefault();
    console.log("In changePass");
        $.ajax({
            url: "http://gProject.pythonanywhere.com/changePassword",
            data: $('#changePasswordForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
                var updated = "updated";
                var noExistance = "Username does not exist";
                var empty = "Empty fields";
                var oldPassCorrect = "Old password is incorrect";
                var newPassMatch = "The new passwords do not match";

            
                if (result["status"] == updated) 
                {
                    alert("Your details have been updated");
                     window.location.replace("home.html");
                   
                } 
                else if(result["status"] == noExistance) 
                {
                    alert("The user name does not exist");
                    window.location.replace ("changePassword.html");
                   
                }
                else if(result["status"] == empty)
                {
                    alert("Please fill in all the fields");
                    window.location.replace ("changePassword.html");
                
                }
                else if(result["status"] == oldPassCorrect)
                {
                    alert("The current password is incorrect");
                    window.location.replace ("changePassword.html");
                
                }
                else if(result["status"] == newPassMatch)
                {
                    alert("The new passwords do not match");
                    window.location.replace ("changePassword.html");
                
                }
        })
        
};

function back()
{
    window.location.replace ("index.html");
};

