$( document ).ready(function(){
    $( "#getweather" ).validate({
        rules: {
            zipcode: {
                required: true,
                digits: true,
                rangelength: [5, 5]
            }
        },
        messages: {
            zipcode: {
                required: "Please enter a zip code.",
                digits: "Please enter only numbers.",
                rangelength: "Zip code must be 5 digits."
            }
        }
    });
    $( "#getweather" ).submit(function(event){
        var isvalid = $( "#getweather" ).valid();
        var zip = $( "#zipcode" ).val();
        if (isvalid) {
            $.get( "https://trp0hsbhw7.execute-api.us-east-1.amazonaws.com/test/weather/zip", 
                {
                    zipcode: zip,
                },
               function(data, status){
                $( "#response" ).show();
                var response_code = data['cod'];
                if (response_code == 200) {
                    var weather = data.weather[0];
                    $( "#locationinfo" ).append("<h5></h5>").text(data['name'] + ", " + data['sys']['country']);
                    $( "#forecastinfo" ).append("<h5></h5>").text(weather['main'] + " with " + weather['description']);
                    $( "#tempinfo" ).append("<h5></h5>").text(data['main']['temp']);
                    $( "#windinfo" ).append("<h5></h5").text(data['wind']['speed']);
                    $( "#humidityinfo" ).append("<h5></h5").text(data['main']['humidity']);
                        if (data.hasOwnProperty("visibility")){
                            $( "#visibilityinfo" ).append("<h5></h5").text(data['visibility']);
                        }
                        else {
                            $( "#visibilityinfo" ).append("<h5></h5").text("Currently not available");
                        }
                    $( "#sunriseinfo" ).prepend("<h5></h5>").text(data['sys']['sunrise']);
                    $( "#sunsetinfo" ).append("<h5></h5>").text(data['sys']['sunset']);
                }
                else if (response_code == 404) {
                    $( "#responsedata" ).hide();
                    $( "#errorresponse" ).append("<h5></h5>").text("The zip code you entered is not valid. Please try a new one.");
                }
                });
            $( "#request" ).hide();
        }  
         event.preventDefault();
    });
    $( "#clearweather" ).submit(function(event){
        $( "#request" ).show();
        $( "#response" ).hide();
    });
});

/*$( document ).ready(function(){
    $( "#clearweather" ).submit(function(event){
        $( "#request" ).show();
        $( "#response" ).hide();
    });
});*/