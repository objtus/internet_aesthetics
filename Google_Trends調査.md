# Google Trends 調査

本書（*internet aesthetics*）の執筆補助として、検索語の時系列関心を Google Trends から取得・可視化した。**代理指標**として使う。一次史料（Wayback・Reddit・記事）の代替ではない。

関連タスク: [`next_tasks.md`](./next_tasks.md) §9-man 追補（任意）、[`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md) §全体像 4.

---

## 取得条件

| 項目 | 値 |
|---|---|
| 地域 | Worldwide |
| 粒度 | 月次 |
| 期間 | 2004-01 — 2026-06 |
| 取得日 | 2026-06-23 |
| エクスポート元 | [Google Trends](https://trends.google.com/) CSV |

`<1` は 0 として扱う。

---

## データの二種類

### 1. 単独 CSV（15 語）

1 クエリ = 1 語。Google Trends がその語の**全期間ピークを 100** に正規化する。

| ファイル（`googletrendscsv/`） | ピーク月 | 2010年以降 first>0 | 2010+ 平均 |
|---|---|---|---|
| aesthetic | 2020-09 | 2004-01 | 29.4 |
| aesthetics | 2026-05 | 2004-01 | 26.3 |
| cottagecore | 2020-11 | 2019-04 | 15.9 |
| dark academia | 2021-01 | 2009-01 | 17.0 |
| internet aesthetic | 2026-05 | 2013-03 | 6.8 |
| internet aesthetics | 2026-05 | 2013-04 | 4.2 |
| liminal space | 2026-06 | 2006-08 | 12.9 |
| seapunk | 2012-11 | 2011-09 | 13.0 |
| seapunk aesthetic | 2020-09 | 2020-09 | 1.8 |
| soft grunge | 2014-08 | 2010-08 | 30.4 |
| tumblr aesthetic | 2018-07 | 2010-06 | 29.3 |
| vaporwave | 2017-01 | 2012-09 | 36.2 |
| vaporwave aesthetic | 2026-02 | 2014-07 | 13.2 |
| witch house | 2020-10 | 2004-01 | 37.3 |
| witch house aesthetic | 2020-02 | 2020-02 | 5.2 |

**用途**: 各語の絶対的な「関心の山」の年月をざっくり把握。語と語の**大小関係は比較できない**（正規化基準が語ごとに異なる）。

### 2. patch CSV（4 セット）

複数語を**同一クエリ**にまとめた比較用。バッチ内で最も高い点が 100、他語は相対値。

| patch | 章・論点 | 同時比較語 |
|---|---|---|
| **patch1** | 第2章（2010年代ミーム） | vaporwave, seapunk, witch house, soft grunge, tumblr aesthetic |
| **patch2** | 第4–5章（2020美学） | vaporwave, cottagecore, dark academia, liminal space, internet aesthetic |
| **patch3** | 第3章（○○ aesthetic 複合語） | vaporwave, internet aesthetics, vaporwave aesthetic, seapunk aesthetic, witch house aesthetic |
| **patch4** | 汎用語 | vaporwave, aesthetic, aesthetics |

各 patch に **vaporwave をアンカー**として入れ、章をまたいだ「同じ語の見え方」の差も示せるようにした（ただし patch 間の数値は**依然として比較不可**）。

#### patch 内ピーク（バッチ相対値）

**patch1** — 2010年代ミームの同時比較

| 語 | max | ピーク月 |
|---|---:|---|
| vaporwave | 100 | 2017-01 |
| tumblr aesthetic | 99 | 2018-07 |
| witch house | 82 | 2020-10 |
| seapunk | 21 | 2012-11 |
| soft grunge | 14 | 2013-12 |

**patch2** — 2020美学

| 語 | max | ピーク月 |
|---|---:|---|
| cottagecore | 100 | 2020-11 |
| dark academia | 75 | 2021-01 |
| vaporwave | 54 | 2017-01 |
| liminal space | 49 | 2026-06 |
| internet aesthetic | 11 | 2026-05 |

**patch3** — 複合語

| 語 | max | ピーク月 |
|---|---:|---|
| vaporwave | 100 | 2017-01 |
| vaporwave aesthetic | 20 | 2026-02 |
| internet aesthetics | 8 | 2026-05 |
| seapunk aesthetic | 0 | — |
| witch house aesthetic | 0 | — |

**patch4** — aesthetic / aesthetics

| 語 | max | ピーク月 |
|---|---:|---|
| aesthetic | 100 | 2020-09 |
| aesthetics | 16 | 2026-05 |
| vaporwave | 1 | 2015-10 |

---

## 解釈上の注意

1. **patch 間・単独 CSV 間でスケールは比較できない。** 同じ vaporwave でも patch1 では 100、patch2 では 54、patch4 では 1 になる。
2. **patch 内**では「同じ年にどの語が相対的に目立ったか」が読める。
3. **witch house** は音楽ジャンルとして 2004 年から非ゼロの値があり、美学ミーム語との比較ではノイズになりうる → 可視化では初期 OFF 推奨。
4. **seapunk aesthetic / witch house aesthetic** は patch3 ではほぼ検索されない（2020 以降の単独 CSV ではピークあり → 複合語としての検索行動は弱い）。
5. Google Trends は後からデータが更新・再正規化される。**取得日 2026-06-23** のスナップショットである。

---

## ファイル一覧（`googletrendscsv/`）

### 生データ

- `*_time_series_Worldwide_20040101-0900_20260623-*.csv` — 単独 15 + patch 4

### 生成物

| ファイル | 内容 |
|---|---|
| `trends_data.json` | patch1–4 統合 JSON（18 系列・16 注釈） |
| `trends_data.js` | 同上（`const TRENDS_DATA = …`、file:// 用） |
| `trends.html` | インタラクティブグラフ |
| `patch1_plot.png` | patch1 静的プロット（matplotlib） |

### スクリプト

| スクリプト | 用途 |
|---|---|
| `build_trends_data.py` | CSV → `trends_data.json` / `.js` |
| `summarize.py` | 単独 CSV のピーク一覧（patch ファイル名は対象外） |
| `analyze_patches.py` | patch 内容・vaporwave アンカー確認（要修正: load のインデントバグあり） |
| `plot_patch1.py` | patch1 の PNG 出力（注釈・witch house 非表示） |

---

## 可視化

### インタラクティブ（推奨）

[`googletrendscsv/trends.html`](./googletrendscsv/trends.html) をブラウザで開く。

- patch 1–4 タブ切替
- 系列チェックボックスで ON/OFF（すべて ON/OFF ボタン付き）
- 表示系列に応じて**縦軸を自動再スケール**（非表示にした語のピークが上限から外れると、残り系列のピークが頂点に来る）
- イベント注釈（破線 + ラベル、グラフ下に一覧）
- デザイン参考: [`リサフランク420_再生数推移.html`](./リサフランク420_再生数推移.html)

**再ビルド**（CSV 更新時）:

```powershell
python googletrendscsv/build_trends_data.py
```

### 静的

```powershell
python googletrendscsv/plot_patch1.py
# → googletrendscsv/patch1_plot.png
```

---

## 注釈一覧（`build_trends_data.py` の `ANNOTATIONS`）

編集は `build_trends_data.py` → 再ビルド。

### patch1

| 月 | ラベル |
|---|---|
| 2011-06 | seapunk ツイート |
| 2011-09 | SuperSuper 特集 |
| 2012-03 | VICE 年表 |
| 2012-07 | Harper vaporwave |
| 2012-11 | Rihanna SNL |
| 2014-08 | soft grunge |
| 2017-01 | vaporwave peak |
| 2018-07 | tumblr aesthetic |

### patch2

| 月 | ラベル |
|---|---|
| 2019-04 | cottagecore 上昇 |
| 2020-03 | lockdown / TikTok |
| 2020-11 | cottagecore peak |
| 2021-01 | dark academia peak |

### patch3

| 月 | ラベル |
|---|---|
| 2020-02 | witch house aesthetic |
| 2026-02 | vaporwave aesthetic |

### patch4

| 月 | ラベル |
|---|---|
| 2020-09 | aesthetic peak |
| 2026-05 | aesthetics peak |

---

## 本書執筆への含意（たたき台）

| 観察 | 草稿への示唆 |
|---|---|
| seapunk ピーク 2012-11（patch1・単独一致） | Rihanna SNL 週のメディア熱と整合。第2章 seapunk 節の**時期補強** |
| vaporwave ピーク 2017-01 | Floral Shoppe 再評価期・Reddit 拡散期と**おおむね同世代**（因果ではない） |
| tumblr aesthetic 2018-07 | Tumblr 美学語の**別ピーク** — vaporwave と同時期ピークではない |
| cottagecore / dark academia 2020–2021 | 第4–5章の**パンデミック美学**の外部指標 |
| aesthetic 2020-09 vs aesthetics 2026-05 | 単数・複数の**ピーク時期のずれ** — 第3章 Wikipedia 単複議論の背景データ候補 |
| internet aesthetic(s) は patch 内で低い | 複合語・上位概念としての検索は、ミーム語より**弱い**（定義語は検索されにくい） |
| 再生数推移（Wayback）との併用 | [`リサフランク420_再生数推移.html`](./リサフランク420_再生数推移.html) と並べると「プラットフォーム内行動 vs 検索行動」の対比になる |

**未反映**: 上記は調査メモ段階。`草稿.md` への直接引用・図表挿入は未着手（任意タスク）。

---

## データから読み取れること

Google Trends は「何人がその語を検索したか」の**外部指標**である。Tumblr の投稿数でも、Reddit の購読者数でも、YouTube 再生数でもない。だからこそ、**プラットフォーム内の熱**（Wayback 再生数など）と**検索行動**を並べると、同じ時期でも形がずれる。

### 1. 美学ミームは「一つの波」ではなく**連鎖するピーク**

単独 CSV のピーク月を時系列に並べると、2010年代は**重なりつつも頂点の年月がずれる**。

```
2012-11 seapunk
2014-08 soft grunge
2017-01 vaporwave
2018-07 tumblr aesthetic
```

patch1（同時比較）でも同じ順序が見える。seapunk は 2012-11 に自分のピークの 50% に到達（**急峻なスパイク**）。vaporwave は 2016-02 に 50%、2017-01 に頂点（**なだらかな上昇**）。tumblr aesthetic は 2016-06 に 50%、2018-07 に頂点（**vaporwave の後追い**）。

**含意**: 「2012年に全部始まった」ではなく、**名前付きの美学が次々と検索語として立ち上がる**構図。草稿の第2章で seapunk → vaporwave → Tumblr 美学語の**継代**を書くとき、時期の根拠として使える。

### 2. patch1 をそのまま読むと witch house が「支配」して見える

patch1 の**年次平均**で最も値が高い語を取ると:

| 期間 | 支配的な語（年次平均） |
|---|---|
| 2010–2015 | witch house |
| 2016–2017, 2019–2020, 2022 | vaporwave |
| 2018, 2021 | tumblr aesthetic |
| 2023–2026 | witch house |

witch house は 2004 年から検索されている**音楽ジャンル名**であり、seapunk / vaporwave とは別回路の関心が混ざる。**witch house を非表示にして再スケール**（`trends.html` のトグル）すると、2010年代ミーム語同士の比較がはっきりする。

**含意**: 「美学ミームの検索関心」と「既存ジャンル名の検索関心」は Google Trends 上で分離が必要。分析時は witch house を除外するか、脚注でノイズと明記する。

### 3. 2020 年前後は**第二クラスター**ができる

単独 CSV のピークをざっくり世代分けすると:

| 世代 | 語 | ピーク |
|---|---|---|
| 2010年代 Tumblr 系 | seapunk, soft grunge, vaporwave, tumblr aesthetic | 2012–2018 |
| 2020 パンデミック期 | cottagecore, dark academia, aesthetic, witch house aesthetic | 2020–2021 |
| 2020 後半〜2026 | liminal space, internet aesthetic(s), aesthetics, vaporwave aesthetic | 2024–2026 |

patch2 でも cottagecore（2020-11）→ dark academia（2021-01）の**数か月差**でピークが並ぶ。vaporwave は同じ patch 内で 2017-01 ピークのまま（54）— **2020 美学の「新しさ」とは時期がずれる**。

**含意**: 第4–5章の「感情が先に来る」「TikTok 美学」と、2010年代ミーム美学は、検索行動上も**別フェーズ**として扱える。

### 4. 「○○ aesthetic」複合語は、ミーム語より**検索されにくい**

patch3 では vaporwave が 100 のとき:

- vaporwave aesthetic … max 20
- internet aesthetics … max 8
- seapunk aesthetic / witch house aesthetic … ほぼ 0

一方、単独 CSV では `seapunk aesthetic`（2020-09）、`witch house aesthetic`（2020-02）にピークがある。**複合語として検索する人は少数**だが、**単独で調べると存在は確認できる**。

**含意**: 第3章の「aesthetic という語法」— ミーム名そのもの（vaporwave）と、ミーム名＋aesthetic（vaporwave aesthetic）の**検索行動の差**。百科事典的な上位語（internet aesthetics）より、**具体ミーム名の方が強い**。

### 5. aesthetic / aesthetics の**逆転が起きている**

単独 CSV 同士（各語ピーク = 100 正規化）の**年次平均比**を見ると:

| 年 | aesthetic ÷ aesthetics |
|---:|---:|
| 2015 | 0.29（複数形の方が相対的に高い） |
| 2020 | 1.99（単数形が急伸 — patch4 でも aesthetic peak 2020-09） |
| 2022 | 2.38 |
| 2026 | 0.65（複数形 aesthetics が再び上） |

2020 年付近の「aesthetic」急伸は、TikTok 等での**形容詞・タグ用法**の一般化と整合しうる。2026 年の aesthetics 再ピークは、Wikipedia の単数↔複数議論（第3章）と**同時代**だが、因果は言えない。

**含意**: 単数 / 複数は「どちらが正しいか」ではなく、**検索行動として交替する二つのピーク**として書ける。

### 6. vaporwave は patch によって**全く別物のスケール**に見える

2017-01（vaporwave 単独ピーク月）の patch 内相対値:

| patch | vaporwave |
|---:|---:|
| patch1 | 100 |
| patch2 | 54 |
| patch3 | 100 |
| patch4 | 1 |

patch4 では aesthetic / aesthetics と比べると vaporwave は**ほぼ検索されない**。同じ語でも、**比較相手を変えると「目立つ／目立たない」が反転**する。

**含意**: 「vaporwave の時代」は patch1・2 の文脈では成立するが、「aesthetic 一般」の時代（patch4）では**周辺語**に降格する。本書の章構成（第2章 vs 第3章）と対応する。

### 7. 一次史料との**突合**で初めて意味を持つ

| 外部指標 | 何を測るか | 例 |
|---|---|---|
| Google Trends | 検索好奇心・語の一般化 | seapunk 2012-11 |
| Wayback 再生数 | プラットフォーム内の蓄積 | リサフランク420 は 2015–2017 に急伸 |
| Reddit / Tumblr | コミュニティ内の言語化 | r/vaporwave 2012-07 |

vaporwave の検索ピーク（2017-01）と Floral Shoppe 再生数の急伸（2015–2016）は**おおむね同世代**だが、**ピークの月は一致しない**。検索は「語を知る・調べる」行動、再生は「既に知ったものを聴く」行動。

---

## どう分析すると情報が引き出せるか

### 分析の型（3 層）

```
┌─────────────────────────────────────────┐
│ A. 単独 CSV … 各語の「生涯ピーク」カレンダー │
├─────────────────────────────────────────┤
│ B. patch CSV … 同時代語の相対的支配関係    │
├─────────────────────────────────────────┤
│ C. 注釈・一次史料 … スパイクの「中身」     │
└─────────────────────────────────────────┘
         A だけ → 時期の羅列
         B だけ → スケール混同のリスク
         A+B+C → 執筆に使える叙述
```

### 手順 1 — ピーク年表を作る（単独 CSV）

`summarize.py` で全語の peak_date を一覧化し、**年表の横軸**に並べる。

- **読めること**: どの語がいつ「検索上の頂点」を迎えたか
- **読めないこと**: 語 A が語 B より「人気だった」か（正規化が別）

### 手順 2 — 同時代比較（patch CSV + trends.html）

章ごとの patch を開き、**witch house 等のノイズ語を OFF** にして縦軸を再スケール。

- **読めること**: 同じ年にどのミーム語が相対的に目立ったか（例: 2018 年は tumblr aesthetic 年）
- **テクニック**: 「年次平均で支配語を取る」「ピーク月の前後 ±6 か月を拡大」

### 手順 3 — 上昇速度の比較

各語について「ピーク値の 50% に達した月」を取る（seapunk = 急、vaporwave = 緩）。

- **読めること**: メディアイベント型（SNL 一発）vs コミュニティ醸成型（Reddit 拡散）
- **草稿への接続**: seapunk 節（イベント駆動）vs vaporwave 節（慢性的上昇）

### 手順 4 — 複合語 vs 単語（patch3 + 単独 CSV 対照）

patch3 で弱い語を、単独 CSV で再確認。

- **読めること**: 「○○ aesthetic」は**言語現象としては存在**するが、**検索クエリとしては弱い**
- **第3章への接続**: aesthetic の語法 — タグとして使う vs 検索語として使う

### 手順 5 — 単数 / 複数の年次比（aesthetic vs aesthetics 単独 CSV）

同じ年の値を並べ、比率の転換点（2020 前後）を見る。

- **読めること**: 語形の「時代」の切り替わり候補
- **注意**: 両方とも各自ピーク = 100 正規化なので、比較しているのは**形状の相似**であり絶対量ではない

### 手順 6 — 一次史料との三点突合

注釈（`ANNOTATIONS`）の月に、Trends スパイク・Wayback・記事日付を並べる。

| 月 | Trends | 史料 |
|---|---|---|
| 2012-11 | seapunk peak | Rihanna SNL |
| 2017-01 | vaporwave peak | Reddit 拡散期 |
| 2020-09 | aesthetic peak | TikTok / ロックダウン |

**スパイクが史料とずれる月**も記録する（ずれ自体が「検索とコミュニティの非同期」を示す）。

### やってはいけないこと

| NG | 理由 |
|---|---|
| patch 間で vaporwave の数値を比較 | 正規化基準がクエリ構成ごとに変わる |
| 単独 CSV の peak 値で人気順を作る | 全語 peak = 100 |
| Trends だけで因果を書く | 検索 ≠ 起源 |
| witch house を美学ミームと同列 | ジャンル名のベースライン |

### 追加分析のアイデア（未実装）

- **地域別取得**（US / UK / JP）— 本書の事例が英語圏中心なら Worldwide より精緻
- **Related queries** のスクショ保存 — 「aesthetic」が何と一緒に検索されるか
- **Wayback 再生数との相関係数** — 2013–2018 月次で formal な検証
- **注釈 ±3 か月の平均 vs 前後** — イベントの「検索への効き」量化（seapunk は効く、vaporwave は緩い、など）

---

## 草稿との対照——補強できる記述・できない記述

一次史料（Wayback・Reddit・記事）が**中身**を担い、Google Trends は**時期・相対的知名度・継代の順序**を外部指標として足す。脚注1文＋「検索関心（Google Trends, Worldwide, 月次, 2026-06 取得）」程度が無難。

### 補強の強さ（凡例）

| 記号 | 意味 |
|---|---|
| ◎ | 草稿の叙述と整合。脚注・1文追記向き |
| ○ | 方向性は合うが、因果・起源までは言えない |
| △ | 書き方を**限定・修正**しないと誤解を招く |
| × | Trends では補強不能（別史料が必要） |

---

### 第2章 — seapunk / vaporwave

| 草稿の記述（要約） | 行付近 | 確度 | Trends | 根拠・使い方 |
|---|---|:---:|---|---|
| 「2012年11月時点、vaporwave より **seapunk のほうが名前が知られていた**」 | L624 | 中（比較の定量化なし） | **◎** | patch1：seapunk ピーク **2012-11**（バッチ内 21、急峻）。vaporwave は **2016 以降**に支配。2012-11 は seapunk の検索スパイク月＝SNL 週と一致 |
| 「Floral Shoppe が**広く知られるのはもう少し先**」 | L443, L602 | 中 | **◎** | vaporwave 単独：first>0 **2012-09**、ピーク **2017-01**。Wayback 再生急伸（2015–16）と**同世代**だが月はずれる →「コミュニティ内蓄積→検索・再生の山は数年後」 |
| 「seapunk は**短命**／2012-11 が楔」 | L588–591 | 中〜高 | **◎** | seapunk 単独ピーク **2012-11** のみ。patch1 でも以降は vaporwave・tumblr aesthetic が年次平均で上回る（witch house 除外時） |
| 「seapunk の遺産は **vaporwave に引き継がれた**」 | L596–598 | **低**（本文も「具体的に示すのは難しい」） | **○**（継代のみ） | ピークの**連鎖**（2012-11 → 2017-01 → 2018-07）で「同時期の一つの波」ではなく**時系列の継代**と書ける。**音楽・視覚の継承の因果は Trends では証明不可** |
| 「2012年7月 Harper 記事が vaporwave 認知の**きっかけ**」 | L622 | 中 | **△** | 2012-07 注釈月は vaporwave 上昇前。批評は**先行**、検索ピークは **2017** →「言語化は2012、**一般検索の頂点は後**」と時制を分けると補強になる |
| 「Blank Banshee 0 は seapunk **に近い**」 | L604 | 中（分類の揺れ） | × | 検索語としては seapunk/vaporwave の**交差**を測れない。Rate Your Music・MASSAGE の方が適切 |
| Mario Zoots / Megazord の**並行**「かもしれない」 | L291 | 低 | × | 影響関係は Trends では不可 |

**追記文案（L624 付近・脚注向け）**

> 2012年11月時点で、同じ検索クエリに seapunk と vaporwave などを並べた Google Trends（Worldwide, 月次）では、seapunk の関心が Rihanna SNL の月にスパイクし、vaporwave の検索ピーク（2017年）はまだ来ていなかった。これは「メディア上の名前の知名度」の**代理指標**であり、コミュニティ内の充実度そのものではない。

---

### 第3章 — aesthetic / internet aesthetic

| 草稿の記述 | 行付近 | 確度 | Trends | 根拠・使い方 |
|---|---|:---:|---|---|
| 「2012夏–2015末、**aesthetic が vaporwave と結びついていく**」 | L626 | 中 | **○** | `aesthetic` 単独の急伸は **2020-09** ピーク。vaporwave は **2017-01**。→「2010年代前半の結びつき」は **X・Reddit 側**が主証拠。Trends は「**検索上の一般化は2020年代**」と**時期を後ろにずらす限定**に使える |
| 「**internet aesthetic** は2019–20ごろメディアに」 | L938 | 高（メディア日付） | **○** | 単独 `internet aesthetic` first>0 **2013-03** だが patch2 内では cottagecore 等に比べ**極めて弱い**（max 11）。→「**メディアの複合語**」と「**検索クエリとしての弱さ**」の対比。上位概念はミーム語より検索されにくい |
| 「aesthetic → 上位枠への**逆転**」 | L902–916 | 高（文法・史料） | **○** | patch4：`aesthetic` 100 vs `vaporwave` 1（2020-09 付近）。「vaporwave の時代」と「aesthetic 一般の時代」は**検索行動上も別フェーズ** |
| 「**aesthetic / aesthetics** の単複」 | L948 付近 Wiki | 中 | **◎** | 単独 CSV 年次比：2015 は aesthetics 優位 → 2020 に aesthetic 急伸 → 2026 に aesthetics 再優位。Wiki 単複移動（2025–26）と**同時代**（因果は言わない） |
| 「○○ **aesthetic** 複合語」 | L445, 第3章全体 | 中 | **◎** | patch3：vaporwave aesthetic max 20、seapunk/witch house aesthetic ≈0。**複合語としての検索は弱い**＝「批評・タグでは使われても、Google ではミーム名本体が強い」 |
| 「プラットフォーム速度の非対称（**筆者の推測**）」 | L920 | **低**（仮説） | **○** | seapunk＝1ヶ月でピーク50%到達、vaporwave＝約1年、 tumbler aesthetic＝約2年。**上昇速度の差**はイベント型 vs 醸成型の**たとえ**に使える。ただし「見た目が勝った」とは言わない（草稿 L920 の注意と一致） |
| Floral Shoppe コメント欄 **aesthetic 起源** | 第3章・§9 | **低**（KYM 緩め済） | **×** | Trends は**起源を証明しない**。Wayback 否定的事実が優先 |

**追記文案（L938 付近）**

> cottagecore や dark academia が個別の検索語として立ち上がる一方、それらを束ねる internet aesthetic という複合語の検索関心は、同時期のミーム語に比べ Google Trends 上は弱い（2026-06 時点の Worldwide 月次）。メディアが複合語を使い始めた時期と、ユーザーがその語で検索する時期は、必ずしも一致しない。

---

### 第4–5章 — 2020 美学

| 草稿の記述 | 確度 | Trends | 根拠 |
|---|---|:---:|---|
| cottagecore・dark academia の**パンデミック期** | 高（日付多数） | **◎** | cottagecore **2020-11**、dark academia **2021-01**（patch2・単独一致）。lockdown 注釈 **2020-03** と上昇期が接続 |
| 2020 美学と 2010 年代ミームの**別フェーズ** | 中 | **◎** | patch2：2020 ピークは cottagecore/dark academia。vaporwave は同 patch 内で **2017** ピークのまま（54） |
| liminal space / Backrooms | 中 | **○** | 単独ピーク **2026-06**（後追い）。第5章の「爆発」と**同世代**だが、草稿の起源叙述は別史料が主 |

---

### 第1章 — 土壌（間接的）

| 草稿の記述 | 確度 | Trends | 根拠 |
|---|---|:---:|---|
| soft grunge → seapunk 等の**土壌** | 高（Tumblr 史料） | **△** | 検索ピークは soft grunge **2014-08**、seapunk **2012-11** → **Tumblr 流通と検索ピークはずれる**。「土壌が先・検索の山は後」または「別語が先にスパイク」と注記しないと矛盾に見える |
| 「タグの意味は**事後的**に確定」 | 高（理論） | ○ | seapunk の**急峻スパイク**は「メディアイベント後に検索語として固定」の**一例**にできる |

---

### 補強できない（×）——草稿を Trends で書き換えない

| 論点 | 理由 | 草稿で使うべき史料 |
|---|---|---|
| aesthetic の**起源**（YouTube コメント等） | 検索 ≠ 発話 | Wayback コメント、X 2012、Reddit |
| seapunk → vaporwave の**内容的継承** | 時系列のみ | BuzzFeed 擁護記事、Blank Banshee タグ、MASSAGE |
| witch house を美学ミームの**同列** | 2004–からのベースライン | Pitchfork 2009、フォーラム |
| 「**最も**人気だったジャンル」 | 正規化が語ごとに別 | 不可。patch **内**の相対のみ |
| GeoCities / Tumblr **投稿数** | Trends は検索のみ | Wayback、Tumblr アーカイブ |

---

### 草稿への反映優先度（提案）

1. **L624** — seapunk が 2012-11 時点で検索上目立っていた（◎）
2. **L443 / L602** — vaporwave の「広く知られる」時期は 2017 前後（◎）＋ Wayback と並記
3. **L938 付近** — internet aesthetic 複合語の検索弱さ（○）
4. **第4章 cottagecore** — 2020-11 / 2021-01 ピーク（◎）
5. **L596–598** — 「継承」を「**検索上の継代**」と限定して1文（○）
6. **L626** — aesthetic–vaporwave 結合の**検索一般化は2020年代**と時制整理（○、既存叙述と突合要）

**反映しない方がよいもの**：起源論（×）、witch house 系譜の強化（△）、「Trends が証明する」と読める因果文。

### 三点突合の型（草稿用）

```
記事・SNL の月  →  Trends スパイクの有無
Wayback 再生    →  同月か？（多くはずれる）
Reddit 創設     →  コミュニティ先行か？
```

例：**2012-11** — SNL ◎ / seapunk Trends ◎ / vaporwave 検索ピーク × / r/vaporwave 既存 ○（7月）  
→ 草稿 L624 の「seapunk のほうが名前が知られていた」を**検索代理指標**で足せる。

例：**2017-01** — vaporwave Trends ◎ / Floral Shoppe 再生急伸 ◎（やや先行）/ fashwave 論争 ○  
→「知名度の山は2015–17、批評言語化は2012」と**層を分けて**書ける。

---

## 今後（任意）

- [ ] patch2–4 の matplotlib 静的プロット
- [ ] `analyze_patches.py` の load バグ修正
- [ ] 草稿 L624・L443・第4章への脚注文案反映（上表「草稿との対照」参照）
- [ ] Google Trends 再取得（四半期ごとなど）時の差分メモ
- [ ] 単独 CSV も JSON に統合し 1 ページで切替（現状は patch のみ）

---

*最終更新: 2026-06-23（草稿対照・補強可否表を追記）*
