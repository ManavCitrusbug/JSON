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
            
            if (response.data1.length > 0) {
                console.log("resposne");
                $('#states').html("");
                $('#city').html("");
                for (var key in response) {
                    val = response[key];
                    for (i = 0; i < val.length; i++) {
                        $('#states').append(`<option >${val[i]}</option>`);
                    }
                }
            }
            else {
                console.log("resposne not foun");
                $('#states').html("")
                $('#states').append(`<option >No state</option>`);


            }
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
            
            var val;
            var i;
            if (response.data1.length > 0) {
                $('#city').html("");
                for (var key in response) {
                    val = response[key];
                    for (i = 0; i < val.length; i++) {

                        $('#city').append(`<option >${val[i]}</option>`);
                    }
                }
            }

            else {
                $('#city').append("<option >" + "No city" + "</option>");
            }
        },

    });
}

function show_data() {
    var country = $('#countries').val();
    var state = $('#states').val();
    var city = $('#city').val();


    if (state == 'No state'|| city == 'Select City' || city == null) {
        $("#div1").css({
            "border-color": "red",
            "border-weight": "4px",
            "border-style": "solid"
        });
        $('#countrydata').html("Empty");
        $('#statedata').html("Empty");
        $('#citydata').html("Empty");
        $('#countrydata').css("color", "red");
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
        $('#countrydata').css("color", "black");
        $('#statedata').css("color", "black");
        $('#citydata').css("color", 'black');


    }




}






