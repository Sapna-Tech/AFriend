exports.handler = function(context, event, callback) {
    let twiml = new Twilio.twiml.MessagingResponse();
    let message = twiml.message();

    if (event.NumMedia !== "0") {

        message.body("Thanks for sending me this image. \r\nI think that you will find this image informative.");
        message.media("https://covid-19-imageforafriend.s3.jp-tok.cloud-object-storage.appdomain.cloud/covid-19.png");
        console.log(event.MediaUrl0);
        callback(null, twiml);


    } else {

        var mob_number = event.From;
        var actual_number = mob_number.substring(12);
        console.log("Mobile number is " + actual_number);
        if (event.hasOwnProperty('Body')) {

            var request = require("request");

            var options = {
                method: 'GET',

                url: '####Python API - coronavirus bot####',

                headers: {
                    'Authorization': '####Auth - coronavirus bot####'
                },

                qs: {
                    text: event.Body,
                    ani: actual_number
                }
            };

            request(options, function(error, response, body) {
                if (response.statusCode === 200) {
                    console.log("Response id " + response);
                    var response_body = response.body;
                    var response_bot = JSON.parse(response_body);

                    var predicted_message = "";
                    var image_url = "";

                    try {
                        if (response_bot.url.length > 0) {
                            message.media(response_bot.url[0]);
                        }
                    } catch (error) {
                        console.log("Catch " + predicted_message);
                    }

                } else {
                    message.body("Sorry...We are facing some technical issue.Please try again.");
                }
                message.body(response_bot.response[0]);
                callback(null, twiml);
            });
        }

    }

};