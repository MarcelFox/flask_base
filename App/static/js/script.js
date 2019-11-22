$(document).ready(function () {
    $("#addTip").click(function () {

        let test = ('PRAISE THE SUN')
        let oldValue = $('#tip').text()

        $.ajax({
            url: "/getTip",
            method: 'GET',
            success: function (result) {
                console.log(test)
                console.log(oldValue)
                console.log(result)
                $("#tip").html(result);
            }
        });


    });
});