$(document).ready(function () {
    $("#addHit").click(function () {

        let playerOldValue = $('#hit').text()

        if ($('#game').text() == '?') {
            $.get('/gethit', e => {$("#game").html(e.name)})
        } else {
            let tableOldValue = $('#game').text()
            $.get('/gethit', e => {$("#game").html(tableOldValue + e.name)})
        }

        $.ajax({
            url: "/gethit",
            method: 'GET',
            success: function (card) {
                let hit = (playerOldValue + card.name)
                // if (hit == 21){
                //     let 
                //     $("#hit").html(card);
                // }
                console.log(card.value)
                $("#hit").html(hit);
            }
        });


    });
});

