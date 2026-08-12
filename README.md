# namakoo-dev.github.io

**[basrun](https://github.com/namakoo-dev/basrun) / [ailine](https://github.com/namakoo-dev/ailine) のランディングページと、開発者（Namakoo）の紹介ページ。**

公開先: **https://namakoo-dev.github.io/**

| ページ | 内容 |
|---|---|
| `index.html` / `index.en.html` | basrun の LP |
| `ailine.html` / `ailine.en.html` | ailine の LP |
| `about.html` / `about.en.html` | 開発者ページ |

## つくりについて

- **手書きの HTML / CSS / JS。** フレームワーク・ビルドツールなし。push すると
  GitHub Pages がそのまま配信する（約 30 秒で反映）。
- **外部への通信は 0 件。** CDN・外部フォント・計測タグを使わない。アイコンは
  [Lucide](https://lucide.dev/) を同梱（ライセンスは `NOTICE`）。
- **日英は別ファイル方式。** 各ページに `*.en.html` の対があり、`hreflang` と
  ナビの言語トグルで双方向に行き来できる。
- **AI が書き、AI が描画して確かめた。** コードは AI アシスタント（Nagi）が書き、
  変更のたびに実ブラウザで描画して崩れを検査してから push している
  （検査道具は [tools](https://github.com/namakoo-dev/tools) の `qa.py`）。
  commit の著者名もその立て付けのまま（`git log` は `Nagi <nagi@stg.local>`）。
- `make_og.py` は OG 画像（`assets/og.jpg`）を作り直すためのローカル用スクリプト。
  サイトの配信には関与しない。

## 検査

視覚の変更は、複数の画面幅（360 / 390 / 768 / 1280px）で実際に描画し、
ナビの折り返し・横はみ出し・リンクの生存を確認してから公開している。
`qa_*.png` などの検査生成物は `.gitignore` で追跡外。
