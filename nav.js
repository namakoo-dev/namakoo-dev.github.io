// ★ nav のクリック/タップに波紋（Material 風 ripple）を付ける。
//    押下位置から円が広がって消える。見た目(色・アニメ)は style.css の .ripple 側。
//    ここは「押した場所に、その要素を覆う大きさの円を1枚挿して、終わったら消す」だけ。
(function () {
  function ripple(e) {
    var el = e.currentTarget;
    var rect = el.getBoundingClientRect();
    var x = (e.clientX != null ? e.clientX : rect.left + rect.width / 2) - rect.left;
    var y = (e.clientY != null ? e.clientY : rect.top + rect.height / 2) - rect.top;
    // 押した点から一番遠い角までの距離 = 要素を必ず覆う半径
    var r = Math.sqrt(
      Math.pow(Math.max(x, rect.width - x), 2) +
      Math.pow(Math.max(y, rect.height - y), 2)
    );
    var span = document.createElement('span');
    span.className = 'ripple';
    span.style.width = span.style.height = (2 * r) + 'px';
    span.style.left = (x - r) + 'px';
    span.style.top = (y - r) + 'px';
    el.appendChild(span);
    span.addEventListener('animationend', function () { span.remove(); });
  }
  // pointerdown = マウスもタッチも、押した瞬間に出す（遷移前に見える）
  var links = document.querySelectorAll('.nav a');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener('pointerdown', ripple);
  }
})();
