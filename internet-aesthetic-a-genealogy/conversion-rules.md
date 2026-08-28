# MD→HTML 変換ルール（internet aesthetic: a genealogy）

個人サイト（100%health / `txt/internet-aesthetic-a-genealogy/`）公開用。正本は [`草稿.md`](../草稿.md)。変換単位は同期済み [`manuscript/`](../manuscript/) の9ファイル。

---

## 1. デプロイフォルダ

リポジトリの [`internet-aesthetic-a-genealogy/`](./) を、サイトの `txt/internet-aesthetic-a-genealogy/` へ**フォルダごとコピー**する。

```
internet-aesthetic-a-genealogy/
  index.html                      ← 目次
  intro.html
  ch01.html … ch08.html
  img/                            ← build.py が ../img/ から同期
  build.py
  conversion-rules.md
```

| ソース | 出力 HTML |
|---|---|
| `序文.md` | `intro.html` |
| `第1章_土壌.md` | `ch01.html` |
| … | … |
| `第8章_制度化.md` | `ch08.html` |

---

## 2. パス（`txt/internet-aesthetic-a-genealogy/` 配置時）

| 参照先 | 相対パス |
|---|---|
| サイト共通 CSS/JS | `../../1column.css`, `../../js/main.js` 等 |
| txt 共通 CSS | `../text.css` |
| 100%health トップ | `../../index.html` |
| txt 目次 | `../txt_main.html` |
| 本シリーズ目次 | `index.html` |
| 図版 | `img/filename.png` |

---

## 3. ビルド

```bash
python internet-aesthetic-a-genealogy/build.py
```

- 章 HTML を再生成
- `img/` をリポジトリルートの [`img/`](../img/) から同期コピー
- `index.html` は手編集（build 対象外）

再生成前に `manuscript/` を [`草稿.md`](../草稿.md) と同期すること。

---

## 4. 章ナビ

各章末尾：目次（`index.html`）＋前章｜次章。パンくずは `100%health > txt > internet aesthetic: a genealogy > {章}`。

---

## 5. 画像と HTML コメント

草稿・分割稿では、画像の直後に HTML コメントで出典 URL や補足を書く。

```markdown
![キャプション](img/filename.png)
<!-- https://example.com/source-page -->
<!-- 補足（URLなしも可） -->
```

`build.py` がこれを `<figure class="fig-screenshot">` に変換する。

```html
<figure class="fig-screenshot">
  <a href="img/filename.png">
    <img width="500" height="500" src="..." alt="..." loading="lazy" />
  </a>
  <figcaption>
    <p>キャプション</p>
    <p class="fig-source">
      <a href="...">出典</a>
    </p>
  </figcaption>
</figure>
```

- `<p>` … キャプション（alt テキスト）
- `<p class="fig-note">` … コメント内の説明文（URL を除いた部分）
- `<p class="fig-source"><a …>` … コメントから抽出した URL（ラベルはホスト名、`web.archive.org` は「Internet Archive」）
- `<img>` … `width="500" height="500"`、`loading="lazy"`（Luminous 用に `<a>` で包む）

`[![…](img/x)](https://…)` 形式（YouTube サムネ等）は従来どおり画像自体が外部リンク。

---

## 6. 見出しと section

各見出しは `<section id="{slug}">` で包み、§ リンク付きの見出しに変換する。

```html
<section id="geocities">
  <h2 class="heading_title">GeoCitiesという楽園と、その消滅<a href="#geocities" class="header-link">§</a></h2>
  …
</section>
```

| 項目 | ルール |
|---|---|
| ページタイトル | `<h1 class="title">`（章名・序文） |
| 序文の section 起点 | MD の `###` → HTML の `<h2>` |
| 各章の section 起点 | MD の `##` → HTML の `<h2>`（章タイトル行 `# 第N章…` は省略） |
| 下位見出し | MD の `###` → `<h3>`、`####` → `<h4>` …（ネストした `<section>`） |
| `id`（slug） | 見出し行末に `{#english-slug}` を書く（Pandoc 形式）。HTML の `section id` と § リンクに使う。未指定時は従来どおり自動生成 |
| § リンク | 各見出し末尾に `<a href="#{slug}" class="header-link">§</a>` |

見出しレベルはスキップしない（h1 の次は h2）。序文では `## 序文` を出力せず、`###` を h2 に繰り上げる。同级の `<section>` の間は空行を1行入れる。

---

## 7. その他

リンク・出典・画像の詳細ルールは従来どおり。本文出典は公開 URL のみ（[`project-style-notes.md`](../docs/project-style-notes.md) §6）。
