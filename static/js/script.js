 // カードをドラッグ＆ドロップするためのJavaScript

 var cardContainer = document.getElementById('card-container');
 var answerArea = document.getElementById('answer-box');
 
 // カードのドラッグ＆ドロップができるように設定
 var sortableCardContainer = Sortable.create(cardContainer, {
    group: "shared",
    animation: 150,
    sort: false  // 元のカードリストの順序は変更しない
});

var sortableAnswerArea = Sortable.create(answerArea, {
    group: "shared",  // 同じグループ名にすることで、カードをドラッグし合えるようにする
    animation: 150,
    // 解答欄内で順序を入れ替えることができる
});

// フォーム送信時に、解答エリアにあるカードを取得してinputにセット
document.getElementById('submit-button').addEventListener('click', function() {
    var answerCards = document.querySelectorAll('#answer-box .card');
    var answers = [];
    answerCards.forEach(function(card) {
        answers.push(card.innerText);  // カードのテキストを取得
    });
    document.getElementById('answer-input').value = answers.join(', ');  // カードをカンマ区切りで結合
});
