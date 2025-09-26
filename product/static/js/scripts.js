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
});