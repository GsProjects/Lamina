function logout_user()
{    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/logout",
            type: 'GET',
            async: false})
            .done(function(response) {
                console.log(response);
                var result = JSON.parse(response);
                if (result["status"] == "You have logged out successfully") 
                {
                    bootbox.alert("You have logged out successfully",function()
                        {
                            window.location.replace("index.html");
                        })
                   
                } 
                else if(result["status"] == "Logout failed") 
                {
                    bootbox.alert("Logout failed please try again",function()
                        {
                            window.location.replace ("home.html");
                        })
                }
        })     
};