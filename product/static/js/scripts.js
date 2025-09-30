$(document).ready(function(){

    function addOpions(){
        var select = $('#pr-amount').text()
        var x = $('#pr-amount').val()
        for(var i=1; i<select; i+=1){
            $('select').append(`<option value="${i}">${i}</option>`);
        };
        $('select').append(`<option value="${x}">${x}</option>`);
    };

    addOpions();

    $('#add-button').click(function(e){
        e.preventDefault();

        $.ajax({
            type: 'POST',
            url: $('.detail').data('url'),
            data: {
                product_id: $(this).val(),
                product_qty: $('#select option:selected').text(),
                'csrfmiddlewaretoken': $("[name=csrfmiddlewaretoken]").val(),
                action: 'post'
            },
            success: function (response) {
                addOpions();
                window.location.href = $('.text-end').data('redirect')
            },
            error: function (error) {
                console.log(error)
            }
        })
    });
});