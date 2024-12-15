$(document).ready(function () {
    // グーがクリックされた時の処理
    $('#hand-rock').click(function () {
        clickHand("rock");
        $.ajax({
            url: '/game',
            type: 'POST',
            data: {
                "hand": "ROCK"
            },
            success: function (data) {
                iconShow(data)
                console.log(data)
            }
        });
    });
    // パーがクリックされた時の処理
    $('#hand-paper').click(function () {
        clickHand("paper");
        $.ajax({
            url: '/game',
            type: 'POST',
            data: {
                "hand": "PAPER"
            },
            success: function (data) {
                iconShow(data)      
                console.log(data)
            }
        });
    });
    // チョキがクリックされた時の処理
    $('#hand-sissors').click(function () {
        clickHand("sissors");
    
        $.ajax({
            url: '/game',
            type: 'POST',
            data: {
                "hand": "SISSORS"
            },
            success: function (data) {
                iconShow(data)
                console.log(data)
            }
        });
    });
    function iconShow(result) {
        if (result == "勝ち") {
            // 勝利　アイコン　表示
            $('#win').css('display', 'block')
            // 残念　アイコン　消す
            $('#fail').css('display', 'none')
            // あいこ　アイコン　消す
            $('#aiko').css('display', 'none')
        } else if (result == "負け") {
            // 勝利　アイコン　消す
            $('#win').css('display', 'none')
            // 残念　アイコン　表示
            $('#fail').css('display', 'block')
            // あいこ　アイコン　消す
            $('#aiko').css('display', 'none')
        } else {
            // 勝利　アイコン　消す
            $('#win').css('display', 'none')
            // 残念　アイコン　消す
            $('#fail').css('display', 'none')
            // あいこ　アイコン　表示
            $('#aiko').css('display', 'block')
        }
        backDisplay()
    }
    function clickHand(hand) {
        ["rock", "paper", "sissors"].forEach(element => {
         if (element == hand) {
            $('#hand-' + element).css('display','block')    
         } else {
            $('#hand-' + element).css('display','none')
         }  
        })   
    }
    async function backDisplay() {
        await sleep(1000);
        ["rock", "paper", "sissors"].forEach(element => {
            $('#hand-' + element).css('display','block')
         });
        ["#win", "#fail", "#aiko"].forEach(element => {
            $(element).css('display','none')
         });       
    }
    // wait関数
    function sleep(milliseconds) {
      return new Promise(function(resolv) {
        setTimeout(function() {
            resolv()
         }, milliseconds)
        })
    }
});