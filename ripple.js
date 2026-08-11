// ★ ページのどこをクリック/タップしても、その位置から波紋（cursor ripple）を出す。
//    見た目(色・アニメ)は style.css の .click-ripple 側。ここは「押した点に円を1枚挿して、
//    終わったら消す」だけ。位置は clientX/Y（固定表示なのでスクロール中でも点に出る）。
document.addEventListener('pointerdown', function (e) {
  var s = document.createElement('span');
  s.className = 'click-ripple';
  s.style.left = e.clientX + 'px';
  s.style.top = e.clientY + 'px';
  document.body.appendChild(s);
  s.addEventListener('animationend', function () { s.remove(); });
});
