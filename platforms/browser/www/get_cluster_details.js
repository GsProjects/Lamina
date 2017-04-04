function get_cluster_data()
{
    event.preventDefault();

    $.ajax({
            url: "http://gProject.pythonanywhere.com/get_cluster_data",
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
                                bootbox.alert("Your session has timed out, please log in again",function()
                                    {
                                        window.location.replace("index.html");
                                    })
                            }
                       
                        if (result["status"] == "Empty Fields") 
                            {
                                bootbox.alert("Please select an animal",function()
                                    { 
                                        window.location.replace("cluster.html");
                                    })
                            }
                        if (result['status'] == 'Date order')
                            {
                                bootbox.alert("The end date cannot be before the start date",function()
                                    {
                                        window.location.replace("cluster.html");
                                    })
                            }
                        if (result['status'] == 'Same Dates')
                            {
                                bootbox.alert("The dates cannot be the same",function()
                                    {
                                        window.location.replace("cluster.html");
                                    })
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
    event.preventDefault();
    window.location.replace("home.html");
}