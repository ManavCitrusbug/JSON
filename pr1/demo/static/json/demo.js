$(document).ready(function () {
    $.ajax({
        url: '/countries/',
        type: 'GET',
        success: function (data) {

            $('#countries').html("");
            data.forEach(element => {

                $('#countries').append(`<option >${element.name}</option>`);
            });
        }

    });

})

function get_country() {
    var country = $('#countries').val();

    $.ajax({
        url: '/states/',
        type: 'GET',
        data: { 'country': country },
        success: function (response) {

            var val;
            var i;
            console.log(response);
       

                $('#states').html("");
                $('#city').html("");
                for (var key in response) {
                    val = response[key];
                    for (i = 0; i < val.length; i++) {
                        $('#states').append(`<option >${val[i]}</option>`);
                    }
                }
            // }
            // else {
            //     $('#states').append("<option >" + 'No states are available' + "</option>");

            // }
        },

    });

}

function get_city() {
    var states = $('#states').val();

    $.ajax({
        url: '/city/',
        type: 'GET',
        data: { 'states': states },
        success: function (response) {
            // if (response.length > 0) {
                var val;
                var i;
                $('#city').html("");
                for (var key in response) {
                    val = response[key];
                    for (i = 0; i < val.length; i++) {

                        $('#city').append(`<option >${val[i]}</option>`);
                    }
                }
      
            // else {
            //     $('#city').append("<option >" + "No city are available" + "</option>");
            // }
        },

    });
}

function show_data() {
    var country = $('#countries').val();
    var state = $('#states').val();
    var city = $('#city').val();


    if (state == 'No states are available' || city == 'No city are available') {
        $("#div1").css({
            "border-color": "red",
            "border-weight": "4px",
            "border-style": "solid"
        });
        $('#countrydata').html(country);
        $('#statedata').html("Empty");
        $('#citydata').html("Empty");
        $('#statedata').css("color", "red");
        $('#citydata').css("color", 'red');

    }
    else {
        $('h5').show();
        $("#div1").css({
            "border-color": "green",
            "border-weight": "4px",
            "border-style": "solid"
        });
        $('#countrydata').html(country);
        $('#statedata').html(state);
        $('#citydata').html(city);


    }




}






