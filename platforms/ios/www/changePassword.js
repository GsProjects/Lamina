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
                    bootbox.alert("Your details have been updated",function()
                        {
                            window.location.replace("home.html");
                        })
                   
                } 
                else if(result["status"] == noExistance) 
                {
                    bootbox.alert("The user name does not exist",function()
                        {
                            window.location.replace ("changePassword.html");
                        })
                }
                else if(result["status"] == empty)
                {
                    bootbox.alert("Please fill in all the fields",function()
                        {
                            window.location.replace ("changePassword.html");
                        })
                }
                else if(result["status"] == oldPassCorrect)
                {
                    bootbox.alert("The current password is incorrect",function()
                        {
                            window.location.replace ("changePassword.html");
                        })
                }
                else if(result["status"] == newPassMatch)
                {
                    bootbox.alert("The new passwords do not match",function()
                        {
                            window.location.replace ("changePassword.html");
                        })
                }
        })
        
};

function back()
{
    window.location.replace ("index.html");
};

