$(document).ready(function () {
    $("#addHit").click(function () {

        let playerOldValue = $('#hit').text()

        $.get('/getCardValue', { 'value': $('#hit').text().slice(-2, -1) }).done(e => {
            scndLastValue = parseInt(e)
            $.get('/getCardValue', { 'value': $('#hit').text().slice(-1) }).done(e => {
                lastValue = parseInt(e)

                $.get('/getCardValue', { 'value': $('#hit').text().slice(-1) }).done(e => {
                    let plScore = $("#plScore").text()

                    let value = (parseInt(plScore) + parseInt(e))
                    if (value > 21) {
                        $("#plStatus").html('YOU LOSE!')
                        $("#tbStatus").html('TABLE WIN!')
                        $("#addHit").prop("disabled", true);
                        $("#stand").prop("disabled", true);
                        if ($('#tbCard1').text() == '?') {
                            $.get('/gethit', e => {
                                $("#tbCard1").html(e.name)
                            })
                        }
                    } else if (value == 21) {
                        $("#plStatus").html('YOU WIN!')
                        $("#tbStatus").html('TABLE LOSE!')
                        $("#addHit").prop("disabled", true);
                        $("#stand").prop("disabled", true);
                        if ($('#tbCard1').text() == '?') {
                            $.get('/gethit', e => {
                                $("#tbCard1").html(e.name)
                            })
                        }
                    }
                    $("#plScore").html(value)
                })
            })
        })


        $.ajax({
            url: "/gethit",
            method: 'GET',
            success: function (card) {
                let hit = (playerOldValue + card.name)
                $("#hit").html(hit);
            }
        });


    });

    $("#stand").click(function () {
        let count = 1
        $("#addHit").prop("disabled", true);
        $("#stand").prop("disabled", true);

        if ($('#tbCard1').text() == '?') {
            $.get('/gethit', e => {
                $("#tbCard1").html(e.name)
            })

        } else {
            let tbOldValue = $('#game').text()
            $.get('/gethit', e => { $("#game").html(tbOldValue + e.name) })
        }
        let joker = $('#tbCard1').text()


        $.get('/getCardValue', { 'value': $('#game').text().slice(-2, -1) }).done(e => {
            $.get('/getCardValue', { 'value': $('#game').text().slice(-2, -1) }).done(e => {

                let scndLastValue = e
                $.get('/getCardValue', { 'value': $('#game').text().slice(-1) }).done(e => {
                    let tbScore = $("#tbScore").text()

                    let value;

                    if (joker == '?') {
                        let value = (parseInt(scndLastValue) + parseInt(e))
                        $("#tbScore").html(value)
                    } else {
                        let value = (parseInt(tbScore) + parseInt(e))
                        $("#tbScore").html(value)
                    }

                    setTimeout(function(){

                    if ($("#tbScore").text() <= 17 && $("#tbScore").text() !== '') {
                        console.log($("#tbScore").text())
                        $("#stand").trigger("click");
                    } else {

                        if ($("#tbScore").text() > 21) {
                            $("#tbStatus").html('TABLE LOSE!')
                            $("#plStatus").html('YOU WIN!')
                        } else if ($("#tbScore").text() == 21) {
                            $("#tbStatus").html('TABLE WIN!')
                            $("#plStatus").html('YOU LOSE!')
                        } else if ($("#tbScore").text() < 21 && ($("#tbScore").text() > $("#plScore").text())) {
                            $("#tbStatus").html('TABLE WIN!')
                            $("#plStatus").html('YOU LOSE!')
                        }  else if ($("#tbScore").text() < 21 && ($("#tbScore").text() < $("#plScore").text())) {
                            $("#tbStatus").html('TABLE LOSE!')
                            $("#plStatus").html('YOU WIN!')
                        }  else if ($("#tbScore").text() == $("#plScore").text()) {
                            $("#tbStatus").html('DRAW!')
                            $("#plStatus").html('DRAW!')
                        }
                    }
                    }, 800);

                })

            })

        })

    })
    
    $('#reload').click(function() {
        location.reload();
    });



})
