function animalProfile()
{
    event.preventDefault();
    
        $.ajax({
            url: "http://gProject.pythonanywhere.com/animalProfile",
            data: $('#profileForm').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
            
                if (result["status"] == "ok") 
                {
                    console.log("yurt 1");
                    alert("Animal profile updated");
                     window.location.replace("home.html");
                   
                } 
                else if(result["status"] == "Animal id already exists") 
                {
                    console.log("yurt 2" + result["status"]);
                    alert("The animal id already exists please try again");
                    window.location.replace ("addAnimalProfile.html");
                   
                }
                else if(result["status"] == "Empty fields")
                {
                    console.log("yurt 3");
                    alert("Please fill in all the fields");
                    window.location.replace ("addAnimalProfile.html");
                
            }
        })
        
};
function back()
{
    window.location.replace ("home.html");
};