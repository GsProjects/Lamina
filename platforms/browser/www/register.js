function registerFunction(){
	/*var registrationObj={}

	registrationObj.userName = document.getElementById('registerUserName').value;
	registrationObj.userPassword = document.getElementById('registerUserPassword').value;
	registrationObj.confirmPassword = document.getElementById('confirmRegisterUserPassword').value;

	/*$.ajax({
                    url:"https://www.pythonanywhere.com/user/gProject/files/home/gProject/Lamina/sampleCGI.py", 
                    type:"POST", 
                    dataType:"json", 
                    data:{type:"registrationObj",registerUserName:registrationObj.userName, registerUserPassword:registrationObj.userPassword, confirmRegisterUserPassword:registrationObj.confirmPassword},
                    ContentType:"application/json";
                })*/

	//$("#registerForm").submit(function(){
	//var landmarkID = $(this).parent().attr('data-landmark-id');
	//var postData = $(this).serialize();
	//var registrationObj={}

	/*registrationObj.userName = document.getElementById('registerUserName').value;
	registrationObj.userPassword = document.getElementById('registerUserPassword').value;
	registrationObj.confirmPassword = document.getElementById('confirmRegisterUserPassword').value;*/
	var userName = document.getElementById('registerUserName').value;
	var userPassword = document.getElementById('registerUserPassword').value;
	var confirmPassword = document.getElementById('confirmRegisterUserPassword').value;
	
	//alert(registrationObj.userName);
	/*$.ajax({
		type: 'POST',
		//data:{registerUserName:registrationObj.userName, registerUserPassword:registrationObj.userPassword, confirmRegisterUserPassword:registrationObj.confirmPassword},
		data:{userName:userName, userPassword:userPassword ,confirmPassword:confirmPassword},
		url: 'https://www.pythonanywhere.com/user/gProject/files/home/gProject/Lamina/register.php',
		 headers: {
        //'X-CSRF-Token': $('meta[name="_token"]').attr('content')
    	}
		success: function(data){
			console.log(data);
			alert('Your comment was successfully added');
		},
		error: function(data){
			console.log(data);
			alert('There was an error adding your comment');
		}
	});
	
	return false;*/
	$.ajax({
            url: "sampleCGI.py",
            type: "POST",
            data: {foo: 'bar', bar: 'foo'},
            success: function(response){
                    //$("#div").html(response);
                    console.log(userName);
                    alert("yay it worked");
                }
       });
}
