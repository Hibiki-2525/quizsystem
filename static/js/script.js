 // カードをドラッグ＆ドロップするためのJavaScript
 const cards = document.querySelectorAll('.card');
 const dropArea = document.getElementById('drop-area');
 const answerInput = document.getElementById('answer-input');
 let answerSequence = []; 

 cards.forEach(card => {
     card.addEventListener('dragstart', (e) => {
         e.dataTransfer.setData('text/plain', e.target.id);
     });
 });

 dropArea.addEventListener('dragover', (e) => {
     e.preventDefault();  // ドロップを許可するため
 });

 dropArea.addEventListener('drop', (e) => {
     e.preventDefault();
     const cardId = e.dataTransfer.getData('text');
     const card = document.getElementById(cardId);
     dropArea.appendChild(card);  // ドロップエリアにカードを追加
     answerSequence.push(card.textContent);  // ドロップされたカードを順序に追加
     answerInput.value = answerSequence.join(', ');  // 隠しフィールドに順序を保存
 });

