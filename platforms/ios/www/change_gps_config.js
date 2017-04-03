function load_data()
{    
    var animal_data = JSON.parse(window.localStorage.getItem("associated_animals"));
    
    var animal_array = Object.values(animal_data);
    var parsed_array =[]
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
        
            if(temp_array.length == 2)
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
function change_gps()
{
    var animal = document.getElementById("animal").value;
    if(animal == "--Select an Animal--")
        {
            bootbox.alert("Please select an animal",function()
                {
                    window.location.replace("gpsConfiguration.html");
                })
        }
    var metric = document.getElementById("metric").value;
    var time = parseInt(document.getElementById("time").value);
    var phone_number;
    
    if(typeof(time) != "number" & Number.isInteger(time) == false)
        {
            bootbox.alert("You must enter an integer value",function()
                {
                    window.location.replace("gpsConfiguration.html");
                })
        }
    
    if(metric != "seconds")
        {
            time = time * 60;
        }
    
    
    var animal_data = JSON.parse(window.localStorage.getItem("associated_animals"));
    
    var animal_array = Object.values(animal_data);
    var parsed_array =[]
    for(var i =0; i < animal_array.length;i++)
        {
            var temp_array = Object.values(animal_array[i]);
        
            if(temp_array.length == 2)
                {
                    if(temp_array[0] == animal)
                        {
                             phone_number = temp_array[1];
                        }

                }
        }
    var message ="interval:"
    message = message + time + ','
    
    //https://github.com/cordova-sms/cordova-sms-plugin

    var success = function () { alert('Message sent successfully'); };
    
    var error = function (e) { alert('Message Failed:' + e); };       
    SMS.sendSMS(phone_number, message, success, error);
    window.location.replace("home.html");
}
    

