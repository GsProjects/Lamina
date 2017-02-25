function process_animal()
{
    var animal_data = JSON.parse(window.localStorage.getItem("select_animals"));

    var animal_array = Object.values(animal_data);
    var parsed_array =[];
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);  
            console.log(temp_array.length);
            if(temp_array.length == 6)
                {
                    if(parsed_array.indexOf(temp_array[0] == -1 | parsed_array.length ==0))
                        {
                             parsed_array.push(temp_array[0]);
                        }

                }
        }
    console.log("Parsed array: " + parsed_array);
    
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
    
    
    var select_tag = document.getElementById("animalTwo");
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
function populate_select()
{
    var animal_data = JSON.parse(window.localStorage.getItem("select_animals"));
    console.log(animal_data);
    
    var animal_array = Object.values(animal_data);
    var choice = document.getElementById("animal").value;
    
    var parsed_array =[]
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
            console.log("TEMP ARRAY: " + temp_array);
        
            console.log("Temp array 7 " + temp_array[7]);
            console.log("Temp array 1 " + temp_array[1]);
            console.log("Temp array 0 " + temp_array[0]);
            
            if(temp_array.length == 6)
                {
                    if(temp_array[0] == choice)
                        {
                            console.log(temp_array[5]);  
                            $("#trackingNum").val(temp_array[5]);   
                        }

                }
        }
    
    
    var choice = document.getElementById("animalTwo").value;
    
    var parsed_array =[]
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
            console.log("TEMP ARRAY: " + temp_array);
        
            console.log("Temp array 7 " + temp_array[7]);
            console.log("Temp array 1 " + temp_array[1]);
            console.log("Temp array 0 " + temp_array[0]);
            
            if(temp_array.length == 6)
                {
                    if(temp_array[0] == choice)
                        {
                            console.log(temp_array[5]);  
                            $("#trackingNumTwo").val(temp_array[5]);   
                        }

                }
        }
    
   
}
function back()
{
    window.location.replace("home.html");
}