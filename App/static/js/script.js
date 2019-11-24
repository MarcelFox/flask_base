$(document).ready(function () {
    $("#addHit").click(function () {

        let playerOldValue = $('#hit').text()

        if ($('#tbCard1').text() == '?') {
            $.get('/gethit', e => {
                $("#tbCard1").html(e.name)
                    (e.value)
            })

        } else {
            let tbOldValue = $('#game').text()
            $.get('/gethit', e => { $("#game").html(tbOldValue + e.name) })
        }

        $.get('/getCardValue', { 'value': $('#hit').text().slice(-2, -1) }).done(e => {
            scndLastValue = parseInt(e)
            $.get('/getCardValue', { 'value': $('#hit').text().slice(-1) }).done(e => {
                lastValue = parseInt(e)

                $.get('/getCardValue', { 'value': $('#hit').text().slice(-1) }).done(e => {
                    let plScore = $("#plScore").text()

                    let value = (parseInt(plScore) + parseInt(e))
                    $("#plScore").html(value)

                })
            })


        })


        $.ajax({
            url: "/gethit",
            method: 'GET',
            success: function (card) {
                let hit = (playerOldValue + card.name)
                // if (hit == 21){
                //     let 
                //     $("#hit").html(card);
                // }
                $("#hit").html(hit);
            }
        });


    });
});

