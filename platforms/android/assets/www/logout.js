function logout_user()
{
    //event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/logout",
            type: 'GET',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
            
                if (result["status"] == "You have logged out successfully") 
                {
                    alert("You have logged out successfully");
                     window.location.replace("index.html");
                   
                } 
                else if(result["status"] == "Logout failed") 
                {
                    alert("Logout failed please try again");
                    window.location.replace ("home.html");
                   
                }
        
         
        })
        
};