//$("#profileForm").submit(function() {//.submit allows required and pattern attributes work as .submit does not ignore the required or pattern attributes like onclick
function add_animal()
{
    event.preventDefault()
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
                        alert("Animal profile added successfully");
                        window.location.replace("home.html");

                    } 
                if(result["status"] == "Animal id already exists") 
                    {
                        alert("The animal id already exists please try again");
                        window.location.replace ("addAnimalProfile.html");

                    }
                if(result["status"] == "Empty fields")
                    {
                        alert("Please fill in all the fields");
                        window.location.replace ("addAnimalProfile.html");
                    }
                if(result["status"] == "logged out")
                    {
                        alert("You need to login");
                        window.location.replace ("index.html");

                    }
                if(result["status"] == "Session timed out, please log in again")
                    {
                        alert("You need to login");
                        window.location.replace ("index.html");

                    }
            
        })
}
function back()
{
    window.location.replace ("home.html");
};