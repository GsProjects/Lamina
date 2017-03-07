function process_animal()
{
    var animal_data = JSON.parse(window.localStorage.getItem("associated_animals_update"));
    var animal_array = Object.values(animal_data);
    var parsed_array =[]
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
   
   // document.getElementById("animalID") = animal_array[1] ;
}
function populate_fields()
{
    var animal_data = JSON.parse(window.localStorage.getItem("associated_animals_update"));    
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
                            $("#animalID").val(temp_array[0]);
                            $("#animalType").val(temp_array[1]);
                            $("#animalBreed").val(temp_array[2]);
                            $("#animalWeight").val(temp_array[3]);
                            $("#animalGender").val(temp_array[4]);
                            $("#trackingNum").val(temp_array[5]);
                            $("#oldTrackingId").val(temp_array[5]);
                            $("#oldanimalIdentifier").val(temp_array[0]);
                        }

                }
        }

}
function back()
{
    window.location.replace("home.html");
}