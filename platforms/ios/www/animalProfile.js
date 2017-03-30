function add_animal()
{
    event.preventDefault()
        $.ajax({
            url: "http://gProject.pythonanywhere.com/animalProfile",
            data: $('#profileForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                var result = JSON.parse(response);
                if (result["status"] == "ok") 
                    {
                        bootbox.alert("Animal profile added successfully",function()
                            {
                                window.location.replace("home.html");
                            })
                    } 
                if(result["status"] == "Animal id already exists") 
                    {
                        bootbox.alert("The animal id already exists please try again",function()
                            {
                                window.location.replace ("addAnimalProfile.html");
                            })
                    }
                if(result["status"] == "Wrong gender") 
                    {
                        bootbox.alert("The animal gender can only be M or F",function()
                            {
                                window.location.replace ("addAnimalProfile.html");
                            })
                    }
                if(result["status"] == "Empty fields")
                    {
                        bootbox.alert("Please fill in all the fields",function()
                            {
                                window.location.replace ("addAnimalProfile.html");
                            })
                    }
                if(result["status"] == "logged out")
                    {
                        bootbox.alert("You need to login",function()
                            {
                                window.location.replace ("index.html");
                            })
                    }
                if(result["status"] == "Session timed out, please log in again")
                    {
                        bootbox.alert("You need to login",function()
                            {
                                window.location.replace ("index.html");
                            })
                    }          
        })
}
function back()
{
    window.location.replace ("home.html");
};