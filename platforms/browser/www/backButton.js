//Following code got from http://docs.phonegap.com/en/4.0.0/cordova_events_events.md.html#backbutton
function onLoad() {
        document.addEventListener("deviceready", onDeviceReady, false);
    }

    // device APIs are available
    //
    function onDeviceReady() {
        // Register the event listener
        document.addEventListener("backbutton", onBackKeyDown, false);
    }

    // Handle the back button
    //
    function onBackKeyDown() 
    {

        window.location.replace("home.html");
    }