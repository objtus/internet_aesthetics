# Internet Aesthetics 調査プロジェクト

「インターネット美学（Internet Aesthetics）」という現象の成立史・発生メカニズム・文化的意味を調査し、文章化するためのリサーチプロジェクト。

---

## プロジェクトの目的

「vaporwave」「cottagecore」「liminal space」のような、インターネット上で生まれ増殖した美学ミームの群れを対象として——

- それらがいつ、どこで、なぜ生まれたのかを一次資料に基づいて記録する
- 「aesthetic」という語がどのように哲学用語から大衆的ラベルへと転化したかを追う
- 美学ミームが成立するための条件（技術的・文化的・社会的）を理論化する
- この現象に関する学術研究および批評的言説を整理する

---

## 作業の進め方

1. **正文の正本**は [`草稿.md`](./草稿.md)。分割稿（`第N章_*.md`）は参照用で、食い違えば草稿が正。
2. **事実・日付の正本**はテーマごとに [`context-map.md`](./context-map.md) §1-2 の表に従う。横断の日付索引は [`timeline.md`](./timeline.md)（本編520項目＋【要検証】V1〜V23）。
3. **推敲・文体**は汎用 [`docs/文体メモ.md`](docs/文体メモ.md)（または Claude Code スキル [`.claude/skills/manuscript-style/SKILL.md`](./.claude/skills/manuscript-style/SKILL.md)）＋プロジェクト固有 [`docs/project-style-notes.md`](docs/project-style-notes.md) を併読する。
4. **改稿の優先順位**（2026-07-06 通読）は [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) の総括 A→B→C→E に従う（旧章番号の相互参照更新が最優先）。
5. **タスク管理**は [`next_tasks.md`](./next_tasks.md)。反映済み文案は [`archive/反映済み文案/`](./archive/反映済み文案/) へ移す。一次資料は [`sources/`](./sources/)、編集・レビュー・計画は [`docs/`](./docs/) を正とする。

資料の優先順位（矛盾時の解決手順の要約）は [`context-map.md`](./context-map.md) §1-3 を参照。

---

## ファイル構成

### 作業基盤・横断資料（2026-07 整備）

| ファイル | 内容 |
|---|---|
| [`context-map.md`](./context-map.md) | **資料全体地図。** 正本ルール（L0〜L5）、章⇔ノート対応、ノート間矛盾、【要検証】V1〜V23、更新が必要な箇所 |
| [`timeline.md`](./timeline.md) | **日付の統合インデックス**（2026-07-06 生成）。各正本ノートの日付記述を横断参照。原典は L1 ノート |
| [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) | 草稿全文の整合性通読（2026-07-06）。timeline／context-map 照合つき。指摘約60件・修正優先度付き |
| [`docs/project-style-notes.md`](docs/project-style-notes.md) | 本稿固有の用語・構成・章参照対応表・出典運用 |
| [`docs/文体メモ.md`](docs/文体メモ.md) | **汎用**の文体・推敲基準（プロジェクト非依存） |
| [`.claude/skills/manuscript-style/SKILL.md`](./.claude/skills/manuscript-style/SKILL.md) | 文体メモのスキル版（推敲チェックリスト・具体例つき）。Claude Code 用 |
| [`docs/編集方針.md`](docs/編集方針.md) | 文案の作成・反映に関する方針（政治化・日本語圏射程・seapunk 読み道） |
| [`next_tasks.md`](./next_tasks.md) | タスクトラッカー。進捗管理・調査状況・参照ファイル一覧 |

### 草稿と関連ファイル

| ファイル | 内容 |
|---|---|
| [`草稿.md`](./草稿.md) | **本プロジェクトの中心成果物。** 「インターネット美学のクロニクル」序文＋全8章＋後記 |
| [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) | 事実・章参照・出典の横断レビュー（現行の改稿チェックリスト） |
| [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) | 草稿の通読分析と改稿方針。構造・内容・論理上の問題点と修正優先度 |
| [`docs/草稿_明晰さレビュー.md`](docs/草稿_明晰さレビュー.md) | 章ごとの明晰さ評価。誤記・章番号不一致・比重の偏り等の指摘一覧 |
| [`docs/草稿_ファクト補強調査.md`](docs/草稿_ファクト補強調査.md) | 事実関係の補強調査 |
| [`docs/草稿_レビュー論点メモ.md`](docs/草稿_レビュー論点メモ.md) | レビュー時の論点整理 |

---

### [`草稿.md`](./草稿.md) の章構成

タイトル：「インターネット美学のクロニクル」

- **序文**：射程・方法論・鍵概念（命名・充填・制度化）の導入
- **第1章　土壌——Tumblrとフォークソノミー**：GeoCities→mp3ブログ→MySpace→Tumblrのアーキテクチャ→フォークソノミー→ポストインターネットアート→New Aesthetic→Reblorg
- **第2章　シーンと土壌**：2009〜2011年のマイクロジャンル見取り図。OPN・Ferraro・witch house・Salem・20jfg・GATEKEEPER・Hippos in Tanks・Post T.V.
- **第3章　命名の時代**：vaporwave・chillwave・hypnagogic pop・witch house・seapunkの命名過程。ラベル先行型の発生パターン。DMY Magazine
- **第4章　lo-fiとHD**：proto-vaporwave→Steyerl「In Defense of the Poor Image」→distroid→PC Music→deconstructed club→hyperpop
- **第5章　「aesthetic」という語——包含関係の逆転**：批評・プラットフォーム・ミームが「aesthetic」を充填し、音楽ジャンルの形容詞から見た目とムードの分類軸へ逆転する過程
- **第6章　名前があとから来る（2015〜2019年）**：サフィックスの生産性、normcore、vaporwave政治化、dark academia、cottagecore、Tumblr NSFW BAN
- **第7章　爆発（2020〜2021年）**：COVID-19→liminal space→TikTok→The Backrooms→hyperpop→Discord
- **第8章　制度化：分類するという欲望**：Frutiger Aero→CARI→Aesthetics Wiki→Discord承認→Neocities（対位法）→後記

---

### 調査参照ファイル

| ファイル | 内容 |
|---|---|
| [`インターネット美学（Internet Aesthetics）調査ノート.md`](./インターネット美学（Internet%20Aesthetics）調査ノート.md) | メインの調査記録。個別美学の発生史、語義転換史、発生パターン分類（A〜F）、先行研究 |
| [`美学ミームの成立条件についての覚書.md`](./美学ミームの成立条件についての覚書.md) | 理論的考察。フォークソノミー、包含関係の逆転、充填、遡行的確定 |
| [`CARIの歴史.md`](./CARIの歴史.md) | Consumer Aesthetics Research Instituteの機関史 |
| [`aesthetic wiki 歴史レポート.md`](./aesthetic%20wiki%20歴史レポート.md) | Aesthetics Wiki（aesthetics.fandom.com）の詳細な機関史 |
| [`Nanoformatsの概要と歴史.md`](./Nanoformatsの概要と歴史.md) | ハッシュタグ誕生の技術的前史。Microformats→Nanoformats→#tag |
| [`Web 2.0の詳細年表.md`](./Web%202.0の詳細年表.md) | プラットフォーム生態系の通史（1999〜2021年） |
| [`docs/文章構成プラン.md`](docs/文章構成プラン.md) | 草稿の章構成計画 |

---

### 個別調査ノート

| ファイル | 内容 |
|---|---|
| [`Seapunk 詳細調査ノート.md`](./Seapunk%20詳細調査ノート.md) | Seapunkの一次資料に基づく詳細調査 |
| [`CARI_調査ノート.md`](./CARI_調査ノート.md) | CARI関連の調査メモ |
| [`vaporwave政治化_調査ノート.md`](./vaporwave政治化_調査ノート.md) | vaporwaveの政治化に関する調査 |
| [`witchhouse-chillwave調査メモ.md`](./witchhouse-chillwave調査メモ.md) | witch house・chillwaveの調査 |
| [`HipposInTanks_調査ノート.md`](./HipposInTanks_調査ノート.md) | Hippos in Tanksレーベルの調査 |
| [`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](./MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md) | mp3ブログ時代の調査 |
| [`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) | 「internet aesthetic」の語と制度化 |
| [`Google_Trends調査.md`](./Google_Trends調査.md) | Google Trendsデータ分析（**代理指標**。起源・因果の根拠にしない） |
| [`ハイパーポップの歴史.md`](./ハイパーポップの歴史.md) | hyperpopの発展史 |
| [`インディーウェブの歴史年表.md`](./インディーウェブの歴史年表.md) | IndieWeb・Neocities・cursed images 関連の年表 |
| [`tumblrタイムライン.md`](./tumblrタイムライン.md) | Tumblrの歴史的タイムライン |
| [`§8-2_Tumblr_ForYou_調査メモ.md`](./§8-2_Tumblr_ForYou_調査メモ.md) | Tumblr For You アルゴリズムの調査 |
| [`aesthetic_文法分析メモ.md`](./aesthetic_文法分析メモ.md) | 「aesthetic」の文法的用法の分析 |
| [`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md) | aesthetic関連の手動調査（X・Wayback・Reddit） |
| [`匿名性の美学_後半展開_論点ノート.md`](./匿名性の美学_後半展開_論点ノート.md) | 匿名性と美学に関する論点 |
| [`KYM_liminal_編集史メモ.md`](./KYM_liminal_編集史メモ.md) | Know Your Meme liminal 条目の編集史（2020-08〜2023-09） |
| [`liminal_制度化_Backrooms_言説メモ.md`](./liminal_制度化_Backrooms_言説メモ.md) | liminal space の制度化・メディア言説・Backrooms とのラベル分岐（第7章文案用） |
| [`khole-arena-archillect-researtch.md`](./khole-arena-archillect-researtch.md) | K-HOLE・normcore・VVORK・Archillect・rare.jpg・DIS 人脈 |
| [`Arena設計思想調査ノート.md`](./Arena設計思想調査ノート.md) | Are.na 設計思想・CARI との関係 |
| [`サフィックス系譜比較調査ノート.md`](./サフィックス系譜比較調査ノート.md) | -core/-wave/-punk サフィックスの系譜 |
| [`scene_subculture_notes.md`](./scene_subculture_notes.md) | Scene・Indie Sleaze・Soft Grunge・MySpace サブカル |
| [`supersuper.md`](./supersuper.md) | SuperSuper! Magazine（nu rave→witch house→seapunk 系譜） |
| [`timeline.md`](./timeline.md) | 日付の横断統合インデックス（詳細は上記「作業基盤」） |

---

### 一次資料（L0）

| パス | 内容 |
|---|---|
| [`sources/README.md`](./sources/README.md) | 一次資料フォルダの説明 |
| [`sources/transcripts/`](./sources/transcripts/) | 記事・動画・ZINE・note の転写 |
| [`sources/papers/`](./sources/papers/) | 学術論文・批評記事の全文抽出（.md）と PDF |

### 資料・文字起こし

| ファイル | 内容 |
|---|---|
| [`FrankJavCee文字起こし.md`](./sources/transcripts/FrankJavCee文字起こし.md) | FrankJavCee動画の文字起こし |
| [`SilentGenerationEp22.md`](./sources/transcripts/SilentGenerationEp22.md) | Silent Generation Ep.22の記録 |
| [<./sources/papers/Vaporwave Is (Not) a Critique of Capitalism_Genre Work in An Online Music Scene.md>](<./sources/papers/Vaporwave Is (Not) a Critique of Capitalism_Genre Work in An Online Music Scene.md>) | 論文メモ |
| [`Vaporwave_Politics_Protest_and_Identity.md`](./sources/papers/Vaporwave_Politics_Protest_and_Identity.md) | 論文メモ |
| [`RA_No-Music-on-a-Dead-Internet.md`](./sources/papers/RA_No-Music-on-a-Dead-Internet.md) | Resident Advisor記事メモ |
| [`RA_There-Is-No-Sound-Of-The-2020s-Yet.md`](./sources/papers/RA_There-Is-No-Sound-Of-The-2020s-Yet.md) | Resident Advisor記事メモ |
| [`Unveiling_Tumblr's_Unique_Subcultures-Digital_Tribes_and_Self-Expression.md`](./sources/papers/Unveiling_Tumblr's_Unique_Subcultures-Digital_Tribes_and_Self-Expression.md) | Tumblrサブカルチャー論文メモ |
| [`vice_seapunkwashesup.md`](./sources/transcripts/vice_seapunkwashesup.md) | VICE「Seapunk Washes Up」転写 |
| [`nytimes_littlemermaidgoespunk.md`](./sources/transcripts/nytimes_littlemermaidgoespunk.md) | NYT seapunk 記事転写 |
| [`note_極右の世界のBGM.md`](./sources/transcripts/note_極右の世界のBGM.md) | note 転写（**二次資料**。正文出典にしない） |
| [`musicplusghost.md`](./sources/transcripts/musicplusghost.md) | FEECO *MUSIC + GHOST* 全文転写（src-1 正本） |

---

### メタ・編集作業（L4）

| パス | 内容 |
|---|---|
| [`docs/README.md`](./docs/README.md) | 編集作業フォルダの説明 |
| [`docs/`](./docs/) | 文体・編集方針、草稿レビュー、章 reorg 計画、取込計画 |

### 編集作業ファイル（詳細）

| ファイル | 内容 |
|---|---|
| [`docs/6d-review_aesthetic論点整理.md`](docs/6d-review_aesthetic論点整理.md) | aesthetic章のレビュー論点整理 |
| [`docs/6d-review_第2章構成案.md`](docs/6d-review_第2章構成案.md) | 第2章の構成案 |
| [`docs/第2章_aesthetic章分離_考察.md`](docs/第2章_aesthetic章分離_考察.md) | aesthetic章を分離する際の考察 |
| [`docs/第2章_ed3_seapunk読み道_計画.md`](docs/第2章_ed3_seapunk読み道_計画.md) | seapunk節の読み道計画 |
| [`docs/第3章_aesthetic_rev1_考察.md`](docs/第3章_aesthetic_rev1_考察.md) | aesthetic章の改訂考察 |
| [`docs/Seapunk調査_取り込み計画.md`](docs/Seapunk調査_取り込み計画.md) | Seapunk調査の取り込み計画 |
| [`docs/lofi-HD草稿全体の構造メモ.md`](docs/lofi-HD草稿全体の構造メモ.md) | lo-fi/HD章と全体構造の検討 |
| [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) | 資料の仕分け |
| [`docs/intro-kojiateki_引用メモ.md`](docs/intro-kojiateki_引用メモ.md) | 序文の引用関連メモ |
| [`inv-opn-cook_年表.md`](./inv-opn-cook_年表.md) | OPN・Cook関連年表 |
| [`docs/第7章_reorg_計画.md`](docs/第7章_reorg_計画.md) | 第7章「爆発」再構成の計画・帰属確認 |
| [`archive/反映済み文案/第7章_reorg_文案.md`](./archive/反映済み文案/第7章_reorg_文案.md) | 第7章再構成の**文案正本**（`草稿.md` 反映済・2026-07-23） |
| [`docs/第6章_reorg_計画.md`](docs/第6章_reorg_計画.md) | 第6章 reorg 計画 |
| [`archive/反映済み文案/第6章_reorg_DA-cottagecore_文案.md`](./archive/反映済み文案/第6章_reorg_DA-cottagecore_文案.md) | 第6章 reorg 文案（反映済・2026-07-07） |

---

### 個別章ファイル（草稿.mdに統合済み、参照用に保持）

> **注意**：ファイル名は旧6章構成の番号のまま。現行8章との対応は [`context-map.md`](./context-map.md) §2／[`docs/project-style-notes.md`](docs/project-style-notes.md) §5 を参照。**第2章（シーンと土壌）・第4章（lo-fiとHD）には分割稿がない。** 手動同期のため草稿より遅れることがある——相互参照・事実確認は常に [`草稿.md`](./草稿.md) を正とする。章をまたぐ「第N章で見た」参照の点検表は [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) 総括 A。

| ファイル | 対応章（現行8章） |
|---|---|
| [`序文.md`](./序文.md) / [`序文_改稿.md`](./序文_改稿.md) | 序文 |
| [`第1章_土壌.md`](./第1章_土壌.md) | 第1章 |
| — | 第2章（分割稿なし） |
| [`第2章_命名の時代.md`](./第2章_命名の時代.md) | 第3章（命名の時代） |
| — | 第4章（分割稿なし） |
| [`第3章_aestheticという語.md`](./第3章_aestheticという語.md) | 第5章（aestheticという語） |
| [`第4章_感情が先に来る.md`](./第4章_感情が先に来る.md) | 第6章（名前があとから来る） |
| [`第5章_爆発.md`](./第5章_爆発.md) | 第7章（爆発） |
| [`第6章_制度化.md`](./第6章_制度化.md) | 第8章（制度化） |

### archive/

| ディレクトリ | 内容 |
|---|---|
| [`archive/反映済み文案/`](./archive/反映済み文案/) | 草稿に反映済みの文案ファイル（31件・2026-08-04整理） |
| [`archive/Seapunk取込文案/`](./archive/Seapunk取込文案/) | Seapunk調査の取り込み文案 |

### データファイル

| ファイル | 内容 |
|---|---|
| `googletrendscsv/` | Google Trendsの生データ（CSV）と可視化スクリプト |
| `img/` | 草稿用スクリーンショット・図版（挿入計画: [`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md)） |
| `リサフランク420_再生数推移.html` / `.png` | リサフランク420のYouTube再生数推移グラフ |
| `.claude/skills/manuscript-style/` | Claude Code 用推敲スキル |

---

## 主要な調査テーマ

| テーマ | 主な参照ファイル |
|---|---|
| 「aesthetic」という語の歴史 | aesthetic手動調査 / internet_aesthetic語ノート / 草稿 第5章 |
| 個別美学の発生史 | 調査ノート / timeline.md / 草稿 第3章・第6章・第7章 |
| liminal space・Backrooms・KYM編集史・メディア制度化 | [`liminal_制度化_Backrooms_言説メモ.md`](./liminal_制度化_Backrooms_言説メモ.md) / [`KYM_liminal_編集史メモ.md`](./KYM_liminal_編集史メモ.md) / timeline.md |
| 美学ミームの発生パターン分類 | 覚書 / 調査ノート |
| 充填という概念・成立条件の理論化 | 覚書 / 草稿 第3章・第5章 |
| 分類の制度化（Aesthetics Wiki / CARI） | CARIの歴史 / aesthetic wiki歴史レポート / 草稿 第8章 |
| ハッシュタグ・フォークソノミーの技術的起源 | Nanoformats / Web 2.0年表 / 草稿 第1章 |
| シーン史（2009〜2013年） | 草稿 第2章 / MP3ブログノート / witchhouse-chillwaveメモ |
| lo-fi/HD論 | [`docs/lofi-HD草稿全体の構造メモ.md`](docs/lofi-HD草稿全体の構造メモ.md) / 草稿 第4章 |
| 推敲・文体 | [`docs/文体メモ.md`](docs/文体メモ.md) / [`docs/project-style-notes.md`](docs/project-style-notes.md) / manuscript-style スキル |
| 日付・矛盾の横断確認 | timeline.md / context-map.md / [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) |

---

## 主要参照先

| カテゴリ | 資料 |
|---|---|
| 学術論文 | Giolo & Berghman (2023) *First Monday* / de Gruyter (2022) / Lara López Millán (cottagecore) |
| 一次資料アーカイブ | Aesthetics Wiki / Know Your Meme / CARI / 4plebs / Wayback Machine |
| 批評・ジャーナリズム | VICE / BuzzFeed (2012) / The Atlantic (2021) / Chicago Reader / DIS Magazine / Cluster Mag |
| 理論的背景書 | Marc Augé *Non-Places* / Mark Fisher *Ghosts of My Life* / Simon Reynolds *Retromania* / Hito Steyerl「In Defense of the Poor Image」 |
| 日本語文献 | ばるぼら「蒸気波大辞典」（『新蒸気波要点ガイド』所収）/ 捨て垢（sute_aca）記事 / obakeweb「ドラゴンファンクの5000年」 |
| 日本語書籍 | 古屋蔵人・高岡謙太郎 編『Designing Tumblr』（BNN、2012年9月）/ MASSAGE編集部・庄野祐輔・高岡謙太郎 編『MASSAGE 9: INTERNET CULTURE』（MASSAGE MAGAZINE、2014年1月10日） |

---

*最終更新：2026-07-07（作業基盤整備：timeline / context-map / 整合性レビュー / 文体分離・スキル化）*
