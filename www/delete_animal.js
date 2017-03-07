function process_animal_delete()
{
    var animal_data = JSON.parse(window.localStorage.getItem("delete_animals"));
    
    var animal_array = Object.values(animal_data);
    var parsed_array =[];
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
            if(temp_array.length == 6)
                {
                    if(parsed_array.indexOf(temp_array[0] == -1 | parsed_array.length ==0))
                        {
                             parsed_array.push(temp_array[0]);
                        }

                }
        }    
    var select_tag = document.getElementById("animal");
    var option;
    option = document.createElement("option");
    option.text = "--Select an Animal--";
    select_tag.add(option);
    
    for(var i =0; i < parsed_array.length;i++)
        { 
            option = document.createElement("option");
            option.text = parsed_array[i];
            select_tag.add(option);
        }
   
}
function populate_fields()
{
    var animal_data = JSON.parse(window.localStorage.getItem("delete_animals"));
    var animal_array = Object.values(animal_data);
    var choice = document.getElementById("animal").value;
    
    var parsed_array =[]
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
            if(temp_array.length == 6)
                {
                    if(temp_array[0] == choice)
                        {
                            $("#trackingNum").val(temp_array[5]);                   
                        }

                }
        }
    window.localStorage.clear();
}
function back()
{
    window.location.replace("home.html");
}