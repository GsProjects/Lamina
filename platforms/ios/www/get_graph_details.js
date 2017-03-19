function get_graph_data()
{
    event.preventDefault();

    $.ajax({
            url: "http://gProject.pythonanywhere.com/get_graph_data",
            data: $('#graph_form').serialize(),
            type: 'POST',
            async: false})
            .done(function(response) {
                console.log(response);

                var result = JSON.parse(response);
                
                if(result['status'])
                    {
                        
                        if (result["status"] == "Your session has timed out, please log in again") 
                            {
                                alert("Your session has timed out, please log in again");
                                 window.location.replace("index.html");

                            }
                       
                        if (result["status"] == "Empty fields") 
                            {
                                alert("Please select an animal"); window.location.replace("myprofile.html");
                            }
                       
                    }
                else
                {
                    window.localStorage.setItem('graph_Data',JSON.stringify(result));
                    window.location.replace("movement_graph.html");
                }
               
        })
}
function back()
{
    console.log("Back");
    event.preventDefault();
    window.location.replace("home.html");
}