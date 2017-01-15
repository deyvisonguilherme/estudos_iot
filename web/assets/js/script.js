$(document).ready(function() {
    $('#form-control-luz').submit(function(event) {
        var opcao = $("#luzarea option:selected").val();

        $.ajax({
                url: 'http://192.168.0.101:5000/luz/' + opcao,
                type: 'GET',
                dataType: 'text',
            })
            .done(function() {
                console.log("success");
            });
	return false;
    });

});
