function populate()
{
    var animal_data = JSON.parse(window.localStorage.getItem("boundary_animals"));
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
    var option = document.createElement("option");
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
    var animal_data = JSON.parse(window.localStorage.getItem("boundary_animals"));    
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
                            console.log(temp_array[5]);
                            
                        }
                }
        }
    
}
function sendSMS()
{
    var animal = document.getElementById("animal").value;
    if(animal == "--Select an Animal--")
        {
            bootbox.alert("Please select an animal",function()
                {
                    window.location.replace("create_boundary.html");
                })
        }
    var distance = document.getElementById("distance").value;
    var phone_number = document.getElementById("trackingNum").value;
    if(distance == "")
        {
            bootbox.alert("Please select a distance",function()
                {
                    window.location.replace("create_boundary.html");
                })
        }
    
    var longitude = document.getElementById("longitude").value;
    var latitude = document.getElementById("latitude").value;
   
    if(longitude =="" || latitude == "")
        {
            bootbox.alert("Please select a point on the map",function()
                {
                    window.location.replace("create_boundary.html");
                })
        }

    var message ="distance:";
    message = message + distance.toString() + " " + longitude.toString() + " " + latitude.toString() + ",";
    
    https://github.com/cordova-sms/cordova-sms-plugin

    var success = function () { alert('Message sent successfully'); };
    var error = function (e) { alert('Message Failed:' + e); };       
    SMS.sendSMS(phone_number, message, success, error);
    window.localStorage.clear();
    window.location.replace("home.html");
}
    
function back()
{
    window.location.replace("home.html");
}