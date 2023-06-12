
$(document).ready(function(){

    setInterval(function(){
        $.ajax({
            type: 'GET',
            url: '/getMessages/{{room}}/',
            success: function(res) {
                $('#display').empty();

                for (var key in res.messages) {
                    var temp = `
                        hahaha
                    `;
                    $('#display').append(temp);
                }
            },
            error: function() {
                alert('Error')
            }
        })
    }, 5000)
});



$(document).on('submit', '#panel-submit', function(e) {
    e.preventDefault();
    console.log('gogo')
    $.ajax({
        type: 'POST',
        url: '/send',
        data: {
            username: $('#username').val(),
            room_id: $('#room_id').val(),
            message: $('#message').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function(res) {
            // alert(res)
        },
        error: function() {
            alert("Error")
        }
    });
    document.getElementById('message').value = "";
});