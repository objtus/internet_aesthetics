# 次のタスク

**正本**：[`草稿.md`](./草稿.md)  
**論点バックログ**：[`docs/草稿_レビュー論点メモ.md`](docs/草稿_レビュー論点メモ.md)（2026-06-02 同期済）  
**編集方針**：[`docs/編集方針.md`](docs/編集方針.md)（政治化・日本語圏射程・seapunk 読み道）  
**資料地図**：[`context-map.md`](./context-map.md)／[`timeline.md`](./timeline.md)  
**改稿チェックリスト**：[`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md)（2026-07-06 通読・約60件／**cons-1 反映完了 2026-07-07**）
**文体**：[`docs/文体メモ.md`](docs/文体メモ.md)＋[`docs/project-style-notes.md`](docs/project-style-notes.md)（Claude Code: `.claude/skills/manuscript-style/SKILL.md`）  
**認知リズム**：[`cognitive-rhythm-writing/SKILL.md`](./cognitive-rhythm-writing/SKILL.md)（**crw-*** 推敲の正本）  
**フラクタル推敲**：[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)（**fractal-*** 推敲の正本。文→段落→節→章の順）

**直近完了（2026-08-19）**：**第3章全体の流れの再点検** ☑——「hypnagogic pop」節の分割後、著者の依頼で第3章全体を通し読みし、以下2点を発見・対応。①「憑在論と郷愁の言語」節末尾（L731）がAdam Harper・Charlie Jones・distroidを名指ししていたが、これらが正式に紹介されるのは約250行あとの「DMY Magazine」節（L981・L997）で、前方参照になっていた。おそらく憑在論節を章前半へ移動・格上げした際の副作用。固有名詞を落として一般化し解消（「Nick Landの加速主義と結びつけて読まれることもあった」）。②vaporwave節（L735-747）はchillwave・hypnagogic pop節（新設・拡充後）に比べて分量が薄く、旧明晰さレビューの「vaporwaveの命名過程の分析がseapunkに比べて薄い」指摘がさらに目立つ形になっていた。加筆は推敲の範囲を超えるため、既存引用（捨て垢の記事、L747）の紹介の仕方を変え、「本節は命名経緯に絞っているが、この記事はその後の展開までを一貫して扱っており、総説として参考になる」という一文を追加し、読者への導線とした。

**直近完了（2026-08-19）**：**inv-hypnagogic 反映分の節構造の是正** ☑——著者指摘により、「### hypnagogic pop と二重の命名」節（11段落）が姉妹節「### chillwave——冗談から定着」（3段落）に比べて突出して長いことが判明。fractal-revision-guideの節レベル基準「問いの単一性」で見ると、実質3つの異なる問い（命名の経緯／音とアーティストの異同／批評語としての流通と分岐）を1節に詰め込んでいたため、3分割：「### hypnagogic pop——由来と定義」（4段落）／「### 音とアーティストの異同」（4段落）／「### 同義的な流通と分岐」（3段落）。分量は3・4・4・3段落となりバランスが是正された。

**直近完了（2026-08-19）**：**inv-hypnagogic 反映分の再推敲** ☑——著者がmainに直接反映した第2章L379・L385、第3章「名前は冗談から生まれる——chillwave・hypnagogic pop」節（新設）・「憑在論と郷愁の言語」節（再配置・格上げ）を、ブランチをoriginから作り直した上で[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)の手順で再点検。まず節レベルの確認（「憑在論と郷愁の言語」節の前後橋渡し良好、旧明晰さレビュー指摘の情報過密段落も分割済みと確認）を行い、続けて上から4段落ずつ、文体メモも参照しながら文レベル・段落レベルを詳細に再点検（対象：L677-729、chillwave・hypnagogic pop命名の2小節＋憑在論節）。反映した指摘は計9件——帰属の曖昧さ解消1件（James Ferraro発言の紹介者を明確化）、情報量のピーク分割5件（Wire306流通経緯の文／Keenanの定義文／Carles・Keenanの命名理論化文／glo-fiレビューの事実と推論の分離／Retromania3層分類）、訳語1件（oneiric→「夢想的な」、既出の「夢」モチーフに合わせた）、出典への誠実さ1件（Keenan「堕落形」宣言に英語原文を追加、文体メモ§5）、語順1件（第3章冒頭「の上で」→「を踏まえ」）。時制の不統一（地の文の記述文と資料説明文での書き分け）は著者判断で**現状維持**（日本語として自然、統一不要）。[`docs/inv-hypnagogic_取り込み計画.md`](docs/inv-hypnagogic_取り込み計画.md)の「反映後チェックリスト」8項目もgrep照合ですべて充足を確認しチェック済みに更新。**次：§確定タスクの残り（MySpace年号・章番号詳細・第3章アーキテクチャ節・corecore・IndieWeb節の扱い）、または新規追加ファイル（`docs/inv-hypnagogic_取り込み計画.md`／`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`）の内容確認**

**直近完了（2026-08-18）**：**明晰さレビュー全章検証** ☑——2026-06-25版[`docs/草稿_明晰さレビュー.md`](docs/草稿_明晰さレビュー.md)の指摘（全体課題6点＋章別指摘28件）を序文＋全8章にわたって現物と照合。既存指摘の再検証というアプローチで実施（新規通読は行わず）。結果、大半がfractal-1〜8・各種reorg作業で既に構造ごと解消済みと判明。未解消として残った3件（第4章：第3章末尾との記述重複／第4章：末尾アーキテクチャ節の薄さ／第8章：「遡行的確定」の術語注釈なし）は著者確認のうえ**いずれも対応不要と判断**し、明晰さレビューは全項目クローズ。詳細は下記§明晰さレビュー節。**次：§確定タスク（MySpace年号・章番号詳細・第3章アーキテクチャ節・corecore・inv-hypnagogic文案・IndieWeb節の扱い）**

**直近完了（2026-08-18）**：**fractal-8** ☑——第8章「制度化：分類するという欲望」＋後記「クロニクルの終わりにあたって」を[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)で全節点検・反映（文／段落→節→章。全11節・15コミット）。これで**fractal-1〜8、全8章の主線パイプラインが完走**。主な内容：論理矛盾の修正1件（「Aero」＝Vista一製品の名 vs 時代全体を束ねるラベルの不在）、内容に踏み込んだ議論2件（章冒頭「あの感じ」自体が遡行的確定の産物であることの自己言及追加／盗用の主体をリポジトリ内一次資料で確認して明確化）、節見出しの変更2件（「IndieWebとNeocities」→「Neocities」＝本文にIndieWeb記述がなかったため、「語り直すために、アーカイブが要る」→「物語ることの偏り」＝結論を先取りしない見出しへ）、表記統一6件（facebook/discord→Facebook/Discord）、誤字修正2件（Subprime Morgage→Mortgage、2016年の重複）、引用の訳追加4件、情報量のピーク分割3件、主語の欠落・曖昧性の修正3件、段落の削除1件（Dismiss Yourselfへの唐突な言及、文脈接続が弱く本題から外れていたため）。節をまたいだ重複は第7章との1件のみ（Tumblr NSFW BAN以降の移行先の記述）を発見し前方参照を追加。運用面：見出し変更や内容解釈にかかわる指摘は**著者との協働的な検討**（複数往復での文案修正、リポジトリ内一次資料の確認）を経てから反映する運用が有効だった。**次：明晰さレビュー**（`docs/草稿_明晰さレビュー.md`の章別再確認リスト、下記§参照）

**直近完了（2026-08-15）**：**fractal-5** ☑——第5章「「aesthetic」という語——包含関係の逆転」を[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)で全節点検・反映（文／段落→節→章。全7節・19コミット）。主な内容：自己言及文の反復（「本章で見るのは」型が1節に3回）を統合、誤植（余分な半角スペース）5件、英語引用の形式不統一・訳の欠落5件（文体メモに「簡潔な引用は訳を省略可」の基準を新設）、主題の一意性＋情報量のピーク分割6件、帰属の遅延1件、確信度の書き分け不整合1件（伝聞と断定の混在）、括弧の入れ子（3層）を分割で解消、第3章L733との事実不整合（日付精度・名義の前後関係）を修正、project-style-notes§2の禁止例（「人は二つのものさしで見ていた」）とほぼ同型だった断定文を受け身化、体言止めの断片文を修正。節をまたいだ最大の重複（「プラットフォームと速度のずれ」節と「振り返り」節末尾）は**振り返り節の要約機能として現状維持**と判断。運用面：節レベル点検の逆アウトラインは段落単位ではなく**トピック展開単位**（論理的な繋がりを追う）に変更、fractal-6〜8で継続。**次：fractal-6（第6章）**

**直近完了（2026-08-07）**：**fractal-2** ☑——第2章・**全12節**を [`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md) で点検・反映（文／段落レベル→段落／節レベル再点検・厳格判定→章レベル確認まで完走）。主な作業：全節の文レベル指摘反映、段落の孤立文統合・密度分割（Luke Wyatt段落・アーキテクチャ節の667/671行等）、節をまたいだ重複の前方参照化（witch house「暗いルート」「Unicode記号」等）、第7節見出し変更、アーキテクチャ節を3中見出しに再構成。詳細は git log（`claude/chapter-2-revision-7xq8sg` ブランチ、コミット 61219d7〜6364ca3）参照。**fractal-1-meta を経ずに fractal-2 に着手**（ユーザー指示で第2章を先行）

**直近完了（2026-08-09）**：**8-reorg-0**（計画）——第8章「クロニクルの終わりにあたって」「＜後記＞」の再構成計画を作成。RA（Resident Advisor）特集記事2本（[`sources/papers/RA_There-Is-No-Sound-Of-The-2020s-Yet.md`](sources/papers/RA_There-Is-No-Sound-Of-The-2020s-Yet.md)／[`sources/papers/RA_No-Music-on-a-Dead-Internet.md`](sources/papers/RA_No-Music-on-a-Dead-Internet.md)）と草稿の接続点11個（Altered Zones・GeoCities/MySpace・indie sleaze・retromania≒lo-fi/HD・Mark Fisher・Simon Reynolds・The Caretaker・PC Music/Throbbing Gristle・DJ Harvey発言等）を整理。アーキテクチャ節は新設しない方針。計画は[`docs/第8章_後記reorg_計画.md`](docs/第8章_後記reorg_計画.md)。**次：後記の段落配置・文案化**（ユーザー判断で8-reorgを次に進める）

**直近完了（2026-08-09）**：**inv-hypnagogic**（調査）——第2章L385・第3章L695〜707の「hypnagogic popはchillwaveとほぼ同じ音楽群」「しばしば同義に使われた」という記述を裏取り。結論：「同義に使われた」自体は誇張ではなく良く裏付けられるが、Reynolds『Retromania』の3層アーティスト分類とKeenan自身の後年の分岐宣言（chillwaveを「堕落形」と呼ぶ）を使えば、より正確で聴感の違和感とも整合する記述に書き換えられる。調査は[`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`](notes/chillwave-hypnagogicpop-Retromania_調査ノート.md)（Retromania本文p.345–349の逐語確認・The Wire誌306号「Childhood's End」書誌確認・glo-fi命名史含む）。**文案・草稿反映は未着手**

**直近完了（2026-08-07）**：**fractal-3** ☑——第3章・**全節**を [`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md) で点検・反映（文／段落レベル→章レベル確認まで完走）。主な作業：`Lil Internet と Lil Government の年表`〜`レーベルと正史`〜`SuperSuper! Magazine`〜`seapunkの死と遺産`〜`DMY Magazine`の全節で文レベル指摘反映（表記ゆれ・反復・段落分割）、章レベル確認で3件指摘——`witch-house.com`見出しの重複的な命名を解消（→「witch-house.com フォーラムとseapunkの受容」）、DMY Magazine節の時系列逆行は再検討の結果**現状維持**（Adam Harperの伏線＝715行と「引用が原典を歪める」という構成上の山場を優先）、seapunk節への記述配分の偏りは節冒頭に前置き文を追加して対応。詳細は git log（`claude/chapter-2-revision-7xq8sg` ブランチ、コミット 046adf9〜8bf8992）参照

**直近完了（2026-08）**：**ed-7** ☑——序文圧縮（[`草稿.md`](./草稿.md) L3–L41・**3 `###` 節**）。削除：`### 制度化`（→第5章初出定義）、`### 「インターネット美学」という言葉の来歴`、`### アーキテクチャと各章`。末尾は問い3つ＋第1章への繋ぎ文。**分割稿同期・fractal-1-meta 序文パスは任意**

**直近完了（2026-08）**：**RBMA字幕** ☑——ep5/ep6 字幕の草稿反映（第1章 `## RBMA『H∆SHTAG$』`、第3章 seapunk 小節、第5章 Dodecahedron 圧縮）。Le1f avatar（r03）は**意図的に未反映**。位置変更・統合あり → [`docs/RBMA反映計画.md`](docs/RBMA反映計画.md) 草稿反映メモ

**直近完了（2026-08-01）**：**fractal-1** ☑——第1章・**文／段落レベル**（全節）を [`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md) で点検・反映。序文 L3–L69、GeoCities／mp3ブログ／MySpace／Tumblr／フォークソノミー／ポストインターネット（A1–A6・B1–B3）／James Bridle・Reblorg（A1–A4・B5–B7・「more overtly arty corners」意訳）／`## アーキテクチャが開いた可能性の空間` L344–L368。第1章末 L370 直前まで

**直近完了（2026-07-07）**：**6-reorg-0〜5** ☑——第6章「名前があとから来る」の再構成が完了。normcore読み筋・匿名性→liminal space伏線・`## 名付け親の分からない美学` 統合節（dark academia／cottagecore）に加え、`## vaporwave の政治的受容` 節全体を -wave サフィックス系列の実例として再構成（⑥-full。当初計画になかった追加作業）。文案は [`第6章_reorg_DA-cottagecore_文案.md`](./archive/反映済み文案/第6章_reorg_DA-cottagecore_文案.md)、経緯は [`docs/第6章_reorg_計画.md`](docs/第6章_reorg_計画.md)。すべて `草稿.md` へ反映済み

**直近完了（2026-07-07）**：**cons-1** ☑——整合性レビュー（P-1〜8-9）を [`草稿.md`](./草稿.md) へ反映。還流は cons-2 継続

**直近完了（2026-07-07）**：作業基盤整備——`timeline.md`／`context-map.md`／`docs/草稿_整合性レビュー.md`／`docs/project-style-notes.md`／文体メモ改訂・manuscript-style スキル作成

**直近完了（2026-07-01）**：**ed-6** ☑（序文に新設節「「インターネット美学」という言葉の来歴」反映）／**meta-1** ☑（序文冒頭に動機ツイート2件を要約統合）／序文の全体再構成（新設「「インターネット美学」とは何か」節・用語3層整理・章番号ずれ修正・「aesthetic という語」節削除）／**meg-1〜3** ☑（2026-06-30）／**inv-khole-1c** ☑（第8章 CARI Are.na L1571–1577 反映）

**直近完了（2026-07-24）**：**crw-1** ☑（区間点検**一時停止**）——[`草稿.md`](./草稿.md) **L1–L1843** 全区間点検済（L1–L156 のみ反映、L158–L1843 は検討のみ。**反映は筆者判断**）。再開時は未反映提案を再押ししない

**直近完了（2026-07-24）**：**ban-cons-1** ☑（**草稿正本確認**）——L1320–1340 基準で L1576・L1789 ほか grep。移行先・CNBC 因果の**章間矛盾なし**。残：L1330 `Instagram` 表記（任意）／分割稿・`tumblrタイムライン.md`（**cons-2**）

**直近完了（2026-07-23）**：**crw-1** 一部——[`草稿.md`](./草稿.md) L1–L156 認知リズム推敲（検討・反映）。序文 L1–L58、第1章 GeoCities／mp3ブログ／MySpace／Tumblr／フォークソノミー

**直近完了（2026-07-23）**：**7-reorg-0〜2** ☑（**1d・1e** 含む）——第7章「爆発」の reorg パイプライン完了。計画 [`docs/第7章_reorg_計画.md`](docs/第7章_reorg_計画.md)、文案 [`第7章_reorg_文案.md`](./archive/反映済み文案/第7章_reorg_文案.md)。KYM 編集史・制度化節（[`KYM_liminal_編集史メモ.md`](notes/KYM_liminal_編集史メモ.md)／[`liminal_制度化_Backrooms_言説メモ.md`](notes/liminal_制度化_Backrooms_言説メモ.md)）反映済み。`草稿.md` L1362–1644 へ全文差替え（章末 `## アーキテクチャ：TikTokとDiscordという対照` 復元含む）。**7-reorg-3／4** はユーザー判断でスコープ外（計画・文案タスクはここで終了）

**直近完了（2026-08-13）**：**台帳検証・クローズ**——8月末の完成を見据えて未完了☐を全件洗い出し、草稿の現物と git log で突き合わせた。結果、**すでに終わっているのに☐のまま残っていた10件をクローズ**——**fractal-3**（全節完走済。残1件は下記）／**meg-1〜3**（草稿 L246・L526 に現存）／**inv-khole-1b**（L1395–1439＋第1章 L227 に現存）／**inv-khole-1c**（L1914–1922 に現存）／**6b 残**（L771 で著者明示済）／**明晰さレビューの誤字6件のうち4件**（grep で該当なし＝修正済）／**crw-1**（fractal-* が別線で全章を通すため再開不要）／**meta-3**（8-reorg で L2019・L2025・L2033 に実装済）。原因は**同じIDの状態が4箇所に重複記載**され更新が表だけに入っていたこと。**状態は §タスク索引 と各詳細節の2箇所のみに書く**運用へ変更。残存が確定した小タスクは §確定タスク に集約。**次：fractal-5（第5章）**

**直近完了（2026-08-12）**：**fractal-4** ☑——第4章「lo-fiとHD」を[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)で全節点検・反映（文／段落→節→章）。合計25件の指摘（反映23件・保留2件）。主な内容：主題の一意性違反（「は」複数）を7件分割、節をまたいだ内容の重複（Eccojams/Far Side Virtual、PC Music/SOPHIE再掲、vaporwave対置・hyperpop命名の逐語反復）を前方参照化、密度ピーク文の分割、誤植（半角スペース混入）4件、段落の一段落一トピック違反1件を3段落に分割。セッション運用ルール（2段落ずつ・節レベルで逆アウトライン+語句重複を明示・番号付き報告・反映前に必ず確認）を`next_tasks.md`に明文化、fractal-5〜8で再利用予定。**次：fractal-5（第5章）**

**直近完了（2026-08-11）**：**8-reorg-3** ☑——[`草稿.md`](./草稿.md) L2009・L2015の重複する「持ち込んだ図式」告白を1箇所へ統合（本稿が持ち込んだ図式にすぎない）。「この文章」→「本稿」表記統一も解消。**次：inv-hypnagogicの文案化**

**直近完了（2026-08-10）**：**8-reorg-1・8-reorg-2** ☑——第8章末尾を[`docs/第8章_後記_文案.md`](docs/第8章_後記_文案.md)（第9稿）の内容で`草稿.md`へ反映。「## クロニクルの終わりにあたって」「## ＜後記＞」の二見出し・全17段落を、「## クロニクルの終わりにあたって」一つ＋`###`二節（「十年後にどう見えるか、という問い」「語り直すために、アーカイブが要る」）構成に統合。RA（Resident Advisor）特集記事2本を軸に、indie sleaze／seapunk／FairyPageの反復パターン、PC Music・Throbbing Gristleの評価反転、A.G. Cook/Spotify論争、DJ Harvey発言などを配置。**次：反映後の通読チェック**（下記「8-reorg-3」参照）

**その次**：**inv-hypnagogic の文案化**（第2章L385・第3章L695〜707。調査は[`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`](notes/chillwave-hypnagogicpop-Retromania_調査ノート.md) ☑ 完了）

**以降**：**fractal-1-meta**（第1章・節→章レベル。文／段落レベルは fractal-1 で完了済み）。着手順はユーザー判断——第2・3章（fractal-2・fractal-3）を先行完了済み。あるいは第4章以降への fractal-4 着手も選択肢

**その次**：**cons-2**（timeline／context-map／分割稿還流。ban-cons 残：tumblrタイムライン L285–290 の CNBC 投稿数と 30% 減の整理、第7章分割稿の旧 Discord 叙述）

**crw-1**：☑ **クローズ**（2026-08-13。区間点検は2026-07-24完了。fractal-* が別線で全章を通すため再開不要）

**その後（低優先）**：**inv-vektroid**／**concl-2**／**meta-2**（**meta-3** は 2026-08-13 クローズ——8-reorg で本文実装済み）

**使い方**

1. 下記 **§アクティブ・パイプライン** で依存関係を確認  
2. **§タスク索引** から ID を選び、該当セクション（rev／src／cari／concl／ed）の手順に従う  
3. 完了時に ☐→☑、[`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) に改稿ログ  
4. 事実・日付を確定・還流するときは [`context-map.md`](./context-map.md) §1-2 の正本ノートと [`timeline.md`](./timeline.md) を更新  

**作業の型**（3層を混同しない）

| 層 | 意味 | 例 |
|---|---|---|
| **調査** | ノートに事実を溜める。正文を止めない | `cari-inv`、`rev-7` 調査段階 |
| **文案** | 反映用段落を別ファイルに書く | `第2章取込_*_文案.md` |
| **反映** | [`草稿.md`](./草稿.md) へ貼り付け・分割稿同期 | rev-7 反映、cari-draft |

1. 調査ノート／[`docs/草稿_ファクト補強調査.md`](docs/草稿_ファクト補強調査.md) から候補を選ぶ  
2. **文案ファイル**を作成  
3. 草稿に反映 → 目視照合  
4. 本ファイル・分割稿のステータスを更新  
5. 反映済み文案は [`archive/`](./archive/) へ  

---

## アクティブ・パイプライン（2026-08-12 更新）

**フラクタル推敲（fractal-*）——現在の主線**

```
fractal-1 第1章・文／段落（各節）──────────────────→ ☑ 2026-08-01
         │
         ├→ fractal-1-meta 第1章・節→章 ──────────→ ☐ 保留中
         │
         └→ fractal-2 第2章（文／段落→節→章）─────→ ☑ 2026-08-07（fractal-1-meta 未経由で先行着手）
                    └→ fractal-3 第3章（文／段落）──→ ☑ 2026-08-07
                              └→ fractal-4 第4章（文／段落→節→章）→ ☑ 2026-08-12（運用ルールは下記§参照）
                                        └→ fractal-5 第5章（文／段落→節→章）→ ☑ 2026-08-15
                                                  └→ fractal-6 第6章（文／段落→節→章）→ ☑ 2026-08-17
                                                            └→ fractal-7 第7章（文／段落→節→章）→ ☑ 2026-08-18
                                                                      └→ fractal-8 第8章＋後記（文／段落→節→章）→ ☑ 2026-08-18（全8章・主線パイプライン完走）
```

**規範**：[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)＋[`manuscript-style`](./.claude/skills/manuscript-style/SKILL.md)／[`docs/project-style-notes.md`](docs/project-style-notes.md)。**原意保持・最小介入**。段落分割・主語明示・密度管理可。**crw-1**（認知リズム・削除のみ）とは別線。

**ノート・分割稿還流**

```
cons-2 timeline／context-map／分割稿 ──→ 草稿改稿の還流
         │  ban-cons 残：tumblrタイムライン.md L285–290（8400万→3000万と30%減の混在）
         │  第7章_reorg_文案.md L246 等（旧「Discord＋TikTok へ移行」叙述）
         └→ 草稿 L1320–1340 を正本（移行先・CNBC 因果）
```

**crw-1**（2026-07-24 **一時停止**）

```
crw-1 草稿.md L1–L1843 ☑ 区間点検済（第5章〜後記は 2026-07-24）
         │  規範：cognitive-rhythm-writing/SKILL.md（削除／ニュアンス修正のみ）
         │  L1–L156 ☑ 反映済（2026-07-23）
         │  L158–L1843 ☑ 検討済（反映は筆者判断・未反映提案の再押しなし）
         └→ 再開時は任意区間から
```

**ban-cons-1**（草稿確認済 2026-07-24）

```
ban-cons-1 草稿 L1320–1340 基準 ──→ ☑ grep 確認（L1576・L1789 含む整合）
         │  移行先：Twitter/Patreon 優先、Discord はひとつ、TikTok は 2020 年
         │  投稿数半減：2014→2018 長期衰退（ban 直接因果にしない）
         └→ 分割稿・年表は cons-2 へ
```

**整合性レビュー反映 → ノート還流**（crw-1 と並行可）

```
cons-1 草稿改稿（整合性レビュー A→B→E）──────────────────→ 草稿.md ☑ 2026-07-07
         │  総括A: 旧章番号相互参照（grep+レビュー表）
         │  総括A: 章間同文重複の圧縮
         │  総括B: 人名・数値・断定の訂正
         └→ cons-2 ノート・timeline 還流（総括C。cons-1 と並行可）
```

**第2章・PC Music 系の土台づくり → 第5章 CARI 接続 → 結論**（2026-06 以前のパイプライン・大部分完了）

```
rev-7（ed-1）政治化 ─────────────────────────┐
                                              ├→ rev-4 / rev-8 / rev-9（並行可）
src-2 SuperSuper! ──→ src-5 vaporwave前史（HIT）──→ src-4 ハイパーポップ ──┤
                                              ↓
                         cari-draft（第5章 1段落＋Facebook 補強）
                                              ↓
                         concl-1（Guardian 問い・クロニクル末尾）→ ed-4（後記・Cook／歴史化）

cari-inv ☑（§8 残3件は任意）──── 草稿反映のブロッカーではない
ed-3 seapunk 読み道整備 ────── ☑ 草稿（Phase 1–2）。分割稿同期は任意
meta-1 執筆動機ツイート ────── 序文 or 後記・単独可
meta-3 遡行的確定・本稿の自己言及 ─ 後記追記・単独可（meta-1 後推奨）
concl-2 HTML後方互換／アーカイブ危機／ベンダーロックイン ─ 末尾1段落・単独可（優先度低）
meta-2 振り返りパート新設 ──── 草稿**末尾**・単独可（優先度低・最後に）
```

**Guardian 2016 は2種類**（混同注意）

| 記事 | タスク | 行先 |
|---|---|---|
| Leigh Alexander・Y2K aesthetic（2016-05-19） | cari-inv／cari-draft／concl-1 | 第5章 CARI・結論 |
| Michael Hann・fashwave（2016-12-14） | rev-7（ed-1） | 第2章 Harper 節後 |

---

## 確定タスク（2026-08-13 の検証で実在が確認された小タスク）

fractal-5〜8 の主線とは別に、**現物確認で残存が確定した**もの。合計1稼働日弱。まとめて片付けて閉じる。

| # | 内容 | 現物の状態 | 見積 |
|---|---|---|---|
| 1 | **誤字2件** | ☑ **修正済（2026-08-18・fractal-8）**。草稿L1915「特に2016年以降に2016年4月に」重複／L1916「理由にある可能性がある」→「理由である可能性がある」。facebook表記ゆれも第8章分は同時に解消 | — |
| 2 | **MySpace データ消失年の精度** | 草稿 **L117**「そして**2019年、サーバー移行の不手際によって**12年分…」が残存。[BBC](https://www.bbc.com/news/technology-47610936) では移行が2018年初頭、公表が2019年3月。「2018年の移行、2019年3月に発覚」等へ | 15分 |
| 3 | **第3章 `## アーキテクチャ：命名とプラットフォーム` 節** | fractal-3 で唯一、点検記録が見当たらない節（第2章の同名節は推敲済） | 10分 |
| 4 | **第7章 corecore／yabujincore 追記** | inv-khole-1b の積み残し。1文 | 10分 |
| 5 | **章番号の不一致**（明晰さレビュー課題②） | distroid の章番号、「第5章以降」、序文の第7章欠落。grep で全数確認 | 20分 |
| 6 | **6c 残／6d-review 残** | 6c は Cluster Mag 直後の接続文（当時 L254 → 現 L689・L1221 へ移動）、6d-review は witch house 節の分量・時系列と seapunk 節への接続。**いずれも fractal-2／3 の全節通過後なので吸収済みの可能性が高い**——確認して閉じる | 20分 |
| 7 | **inv-hypnagogic の文案化** | 調査 ☑（[`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`](notes/chillwave-hypnagogicpop-Retromania_調査ノート.md)）。第2章 L385・第3章 L695〜707 が対象。「同義に使われた」は**削らず**、Reynolds の3層分類と Keenan の分岐宣言を足す | 0.5日 |

---

## タスク索引（未完了）

凡例：☐ 未着手／進行中　☑ 完了　— 任意・低優先

### 最優先（今週）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **fractal-1-meta** | **第1章・節レベル＋章レベル推敲**——全節の橋渡し・射程・密度波・章冒頭／章末の一致を点検 | ☐ 保留中 | fractal-1 ☑ | [`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md) §2–3 → [`草稿.md`](./草稿.md) L71–L369。下記詳細節 |
| **fractal-2** | **第2章・フラクタル推敲**（文／段落→節→章。全12節完走） | ☑ 2026-08-07 | fractal-1-meta 未経由で先行着手 | 同上。`草稿.md` 第2章（`claude/chapter-2-revision-7xq8sg` ブランチ）。下記詳細節 |
| **fractal-3** | **第3章・フラクタル推敲**（文／段落→章レベル。全節完走） | ☑ 2026-08-07 | fractal-2 ☑ | 同上。`草稿.md` 第3章。**残1件**：`## アーキテクチャ：命名とプラットフォーム` 節の点検記録なし（10分確認）。下記詳細節 |
| **crw-1** | **草稿全体・認知リズム推敲**——削除／ニュアンス修正のみ（**文の入れ替え禁止**） | ☑ **クローズ 2026-08-13** | 単独可 | 区間点検は2026-07-24完了。fractal-* が別線で全章を通すため再開不要。下記詳細節 |
| **6-reorg-0** | **第6章 reorg 計画**——流れ・三幕・文案（§4） | ☑ | cons-1 ☑ | [`docs/第6章_reorg_計画.md`](docs/第6章_reorg_計画.md)（2026-07-07 流れ・文体追記） |
| **6-reorg-1** | **文案正本化**——§4 を `第6章_reorg_DA-cottagecore_文案.md` へ | ☑ | 6-reorg-0 ☑ | [`第6章_reorg_DA-cottagecore_文案.md`](./archive/反映済み文案/第6章_reorg_DA-cottagecore_文案.md)（2026-07-07 完了） |
| **6-reorg-2** | **第6章 reorg 草稿反映** | ☑ | 6-reorg-1 | [`草稿.md`](./草稿.md)（2026-07-07 完了。①〜⑨＋⑧b＋⑩⑪） |
| **6-reorg-5** | `## vaporwave の政治的受容` 節全体の再構成（⑥-full。計画外の追加作業） | ☑ | 6-reorg-2 ☑ | [`草稿.md`](./草稿.md) L1268–1302（2026-07-07 完了）。経緯は[`docs/第6章_reorg_計画.md`](docs/第6章_reorg_計画.md)更新4 |
| **cons-1** | **草稿整合性レビュー反映** | ☑ | — | 2026-07-07 完了 |
| **ban-cons-1** | **Tumblr NSFW BAN 叙述の章間一貫性**——移行先・時期・CNBC 投稿数因果。L1320–1340 を基準に grep | ☑ 草稿確認済（2026-07-24） | — | 下記詳細節。分割稿・年表は **cons-2** |
| **cons-2** | **timeline／正本ノート還流**——総括 C 残り | ☐ | 並行可 | [`timeline.md`](./timeline.md) 等 |
| **7-reorg-0** | **第7章 reorg 計画**——問題点・流れ・文案下書き・inv-vernacular-photo 採用範囲 | ☑ | 6-reorg ☑ | [`docs/第7章_reorg_計画.md`](docs/第7章_reorg_計画.md)（2026-07-12） |
| **7-reorg-0b** | ユーザー判断の確定（hyperpop＝C案／poor image＝D/W節本籍／見出し確定／D/W移動＋lo-fi/HD回収段落＝Y-light） | ☑ | 7-reorg-0 ☑ | 計画 更新1（2026-07-12） |
| **7-reorg-0c** | 帰属確認（「4chan起源」通説の出どころ／Augé 参照の公開URL） | ☑ | 7-reorg-0 ☑ | 計画 更新2（2026-07-12）。①英語版Wikipedia②Aesthetics Wiki |
| **7-reorg-1** | **文案正本化**——再構成後の第7章**全文**＋変更点一覧（M1〜7・A1〜16・C1〜6・S1〜10） | ☑ | 7-reorg-0c ☑ | [`第7章_reorg_文案.md`](./archive/反映済み文案/第7章_reorg_文案.md)（2026-07-12 正本化。2026-07-23 草稿反映で確定） |
| **7-reorg-1d** | **KYM liminal 編集史**を文案へ反映（L140 ほか。正本 [`KYM_liminal_編集史メモ.md`](notes/KYM_liminal_編集史メモ.md)） | ☑ | 7-reorg-1 ☑ | 制度化節・爆発節へ反映済み（2026-07-23） |
| **7-reorg-1e** | **制度化節**（Backrooms×liminal 言説仮説）文案確定・[`liminal_制度化_Backrooms_言説メモ.md`](notes/liminal_制度化_Backrooms_言説メモ.md) 照合。重複段落削除・WP URL | ☑ | 7-reorg-1 ☑ | [`草稿.md`](./草稿.md) L1508–1548（2026-07-23） |
| **7-reorg-2** | **第7章 reorg 草稿反映**（章全体を文案 §1 で丸ごと差し替え） | ☑ | 7-reorg-1d・1e ☑ | [`草稿.md`](./草稿.md) L1362–1644（2026-07-23）。§2・§3-2 目視照合は任意 |
| **7-reorg-3** | クロスチャプター点検（計画 §7 の表＋grep 全数） | — | — | **スコープ外**（2026-07-23。ユーザー判断で reorg パイプライン終了。必要なら cons-2 等で随時） |
| **7-reorg-4** | 通読・next_tasks／context-map／timeline 還流（cons-2 と合流） | — | — | **スコープ外**（同上。第7章還流は cons-2 に統合） |
| **8-reorg-0** | **第8章 後記 reorg 計画**——RA記事2本と草稿の接続点整理・現状の後記構造の課題整理 | ☑ 2026-08-09 | — | [`docs/第8章_後記reorg_計画.md`](docs/第8章_後記reorg_計画.md)。アーキテクチャ節は新設しない方針で確定 |
| **8-reorg-1** | **後記の段落配置・文案化**——接続点11個から使うもの3〜5点を絞り込み、段落順を確定して文案を書く | ☑ 2026-08-10 | 8-reorg-0 ☑ | [`docs/第8章_後記_文案.md`](docs/第8章_後記_文案.md)（第9稿まで確定。「十年後にどう見えるか、という問い」「語り直すために、アーカイブが要る」の`###`二節構成） |
| **8-reorg-2** | **第8章 草稿反映**——見出し「## クロニクルの終わりにあたって」「## ＜後記＞」を統合し、[`docs/第8章_後記_文案.md`](docs/第8章_後記_文案.md)の本文で丸ごと置き換え | ☑ 2026-08-10 | 8-reorg-1 ☑ | [`草稿.md`](./草稿.md) L2003以降（旧L2001–2034を置換）。「## ＜後記＞」見出しは削除済み |
| **8-reorg-3** | **草稿反映後の残課題**——①「十年後の今から振り返ったとき……それは**この文章**自体が設定した図式によるものだ。」（L2015付近）が「本稿」統一方針から外れたまま残存。同段落の直前文はすでに「筆者が持ち込んだ図式だ」と修正済みで、表現が重複気味でもある。②「いま／今」の表記ゆれ・反復は著者が別途自分で直す予定（対応不要） | ☑ 2026-08-11 | 8-reorg-2 ☑ | ①L2009末尾の重複告白文を削除、L2015を「もっとも、この結節点も、さきほどの見取り図と同じく、本稿が持ち込んだ図式にすぎない。」に統合（断定→逡巡の拍・「本稿」表記統一）。②対応不要のまま |

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **rev-7** | 2016 vaporwave 政治化（コミュニティの応答） | ☑ | — | [`vaporwave政治化_調査ノート.md`](notes/vaporwave政治化_調査ノート.md) → [`第2章取込_vaporwave政治化_文案.md`](./archive/反映済み文案/第2章取込_vaporwave政治化_文案.md) |
| **ed-1** | 編集方針 §1 政治化 | ☑ | rev-7 と同一 | 上記（2026-06-02 反映） |

### 第2章・外部ノート（rev-7 後 or 並行）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **src-2** | SuperSuper! Magazine 追記 | ☑ | rev-7 後推奨 | [`supersuper.md`](notes/supersuper.md) → [`第2章取込_SuperSuper_文案.md`](./archive/反映済み文案/第2章取込_SuperSuper_文案.md) |
| **src-5** | vaporwave前史見直し（Hippos In Tanks） | ☑ | **src-2 直後** | [`HipposInTanks_調査ノート.md`](notes/HipposInTanks_調査ノート.md) → [`第2章取込_vaporwave前史_文案.md`](./archive/反映済み文案/第2章取込_vaporwave前史_文案.md) |
| **src-6a** | MP3ブログ調査ノート——仕分け確定 | ☑ | §1–§19 確定済 | [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) |
| **src-6b** | 第2章・前史（§2・§3・§6） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_mp3blog前史_文案.md`](./archive/反映済み文案/第2章取込_mp3blog前史_文案.md) |
| **src-6c** | 第1章・プラットフォーム（§1 mp3ブログ・§17 MySpace・§18 Tumblr補強） | ☑ | 草稿反映済（2026-06-16） | [`第1章取込_プラットフォーム_文案.md`](./archive/反映済み文案/第1章取込_プラットフォーム_文案.md) |
| **src-6d** | 第2章・命名系譜（§12–§13） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_命名系譜_文案.md`](./archive/反映済み文案/第2章取込_命名系譜_文案.md) |
| **src-6e** | 第2章・アーキテクチャ総括（§10） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_アーキテクチャ総括_文案.md`](./archive/反映済み文案/第2章取込_アーキテクチャ総括_文案.md) |
| **src-6f** | 匿名性（§7）——rev-9 と統合 | ☑ | 草稿反映済（2026-06-16）。「匿名性の美学」主題化＋後記 callback | [`第2章取込_witchhouse匿名性_文案.md`](./archive/反映済み文案/第2章取込_witchhouse匿名性_文案.md) |
| **inv-vektroid** | Vektroid名義増殖——調査（src-6f 派生） | ☐ | **低優先・後回し**。正文は書かない | 調査のみ → [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) スレッドB |
| **inv-msv** | Mater Suspiria Vision / Cosmotropia de Xam / AAVV 調査 | ☑ | 並行可 | 調査＋草稿反映済（2026-06-17）。第2章に「Post T.V.」節を新設 → [`第2章取込_lofi映像Post-TV_文案.md`](./archive/反映済み文案/第2章取込_lofi映像Post-TV_文案.md)／§5.4 |
| **inv-swan** | Daniel Swan の軌跡（lo-fi→HD美学・PC Music・Ecco2k） | ☐ | 並行可。Post TV 文案で起点に言及済 | Lux Laze(2010)→DIS Mag 2012→Jam City/Dux Content/Lifesim→Ecco2k「GT-R」(2017)。下記詳細節 |
| **inv-dclub** | Night Slugs / Fade To Mind（deconstructed club・HD美学）と PC Music の応答 | ☑ | 並行可。草稿反映済（2026-06-17） | [`第2章取込_deconstructedclub_文案.md`](./archive/反映済み文案/第2章取込_deconstructedclub_文案.md)（PC Music 節の後に「並走」節）。下記詳細節 |
| **inv-steyerl** | Hito Steyerl「貧しいイメージの擁護（In Defense of the Poor Image）」節の追加 | ☑ | Post T.V. 節反映済（2026-06-17） | [`第2章取込_steyerl_文案.md`](./archive/反映済み文案/第2章取込_steyerl_文案.md)（Post T.V. 節末 `####`）。下記詳細節 |
| **inv-piajp** | 日本のポストインターネットアート受容——雑誌特集の簡単な紹介節 | ☑ | 草稿反映済（2026-06-17） | [`第1章取込_piajp_文案.md`](./archive/反映済み文案/第1章取込_piajp_文案.md)（第1章・Designing Tumblr 直後）。下記詳細節 |
| **inv-tabor** | Tabor Robak ネットワーク整理・BrandNewPaintJob.exe（Jon Rafman との共作） | ☐ | 並行可 | [taborrobak.com](https://www.taborrobak.com/) / 草稿 L318・L439・L598・L994 既出 |
| **inv-hypnagogic** | chillwave／hypnagogic popの命名史・音楽的異同——**草稿反映済・再推敲済**（2026-08-19） | ☑ 調査／☑ 反映／☑ 推敲 | なし | 計画 [`docs/inv-hypnagogic_取り込み計画.md`](docs/inv-hypnagogic_取り込み計画.md)（反映後チェックリスト充足確認済）／調査 [`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`](notes/chillwave-hypnagogicpop-Retromania_調査ノート.md) |
| **inv-oesb** | OESB（Todd Ledford）× OPN「Time Decanted」MV 接点 | ☑ | 草稿反映済（2026-06-17） | [Vimeo](https://vimeo.com/7616034) / 草稿 L314 |
| **inv-frkwys** | FRKWYS Vol.7（RVNG Intl.）——Ferraro・OPN・Laurel Halo 同席の記録 | ☑ | 草稿反映済（2026-06-17） | [Discogs](https://www.discogs.com/ja/master/353721-Borden-Ferraro-Godin-Halo-Lopatin-FRKWYS-7-) / 2011年7月 |
| **inv-opn-cook** | OPN × A. G. Cook——**vaporwave 系譜と PC Music の交差**（コラボ年表） | ☑ | 並行可。src-4 ☑ 後推奨 | [`inv-opn-cook_年表.md`](notes/inv-opn-cook_年表.md) → [`第2章取込_OPN_Cook_文案.md`](./archive/反映済み文案/第2章取込_OPN_Cook_文案.md)。草稿 L733 直後反映（2026-06-22） |
| **intro-kojiateki** | **骨架的**インタビュー挿話——「その頃のインターネットの雰囲気」（**第2章冒頭・新設節**） | ☑ | 単独可。引用 ☑（書籍確認済） | [`第2章取込_骨架的挿話_文案.md`](./archive/反映済み文案/第2章取込_骨架的挿話_文案.md)／[`docs/intro-kojiateki_引用メモ.md`](docs/intro-kojiateki_引用メモ.md)。草稿 L238 付近反映（2026-06-22） |
| **src-4** | ハイパーポップの歴史（PC Music 2013–2016 厚み） | ☑ | src-2 後（src-5 と並行可） | [`ハイパーポップの歴史.md`](notes/ハイパーポップの歴史.md) → `archive/反映済み文案/第2章取込_ハイパーポップ_文案.md` |
| **src-4b** | ハイパーポップ追記（Spotify「Hyperpop」命名→brat summer） | ☑ | src-4 ☑ | [`第4章取込_hyperpop_Spotify-bratsummer_文案.md`](./archive/反映済み文案/第4章取込_hyperpop_Spotify-bratsummer_文案.md)。草稿反映（2026-06-22） |
| **src-1** | musicplusghost 洗い出し | ☑ | 草稿反映なし（2026-06-22 確定） | [`musicplusghost.md`](./sources/transcripts/musicplusghost.md) |
| **src-3** | r/witchhouse 歴史スレ参照 | ☑ | rev-9 と重複なし | `#### コミュニティの正史` 末尾1文+URL（2026-06-17 反映済） |
| **rev-8** | Eccojams vs Far Side Virtual | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_FSV対比_文案.md`](./archive/反映済み文案/第2章取込_FSV対比_文案.md) |
| **rev-9** | witch house 匿名性 | ☑ | src-6f に統合済（2026-06-16） | [`第2章取込_witchhouse匿名性_文案.md`](./archive/反映済み文案/第2章取込_witchhouse匿名性_文案.md) |
| **rev-4** | ムードボード対比 | ☐ | 並行可 | `第1章取込_ムードボード対比_文案.md` |
| **ed-3** | seapunk 読み道整備（節頭地図等・圧縮以外） | ☑ | 2026-06-22 草稿反映。分割稿→任意 | 下記 ed-3 節 |

### 第5章・CARI・結論（第2章土台の後）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **cari-inv** | CARI 調査（§8 要確認・Global Village 等） | ☑ | — | [`CARI_調査ノート.md`](notes/CARI_調査ノート.md)。2026-06-17 完了判定：DV-i ☑、Shenzhen Miracle ☑、GVC ☑。§8 残3件（Collins URL・トレーラー照合・Terrell Davis）は**任意** |
| **cari-draft** | CARI 草稿反映（Guardian・Neo-Y2K 1段落、Facebook 補強） | ☑ | **src-2＋src-4 後** | 同上 → `archive/反映済み文案/第5章取込_CARI_文案.md` |
| **concl-1** | Guardian 2016 結論の時代診断問いかけ（ユーザー改稿・案A） | ☑ | cari-draft ☑ | [`第5章取込_結論_Guardian問いかけ_文案.md`](./archive/反映済み文案/第5章取込_結論_Guardian問いかけ_文案.md) |
| **concl-2** | 末尾——HTML後方互換・アーカイブ危機・ベンダーロックイン（軽く触れる） | ☐ | 単独可。**優先度低・最後** | 下記詳細節。`## クロニクルの終わりにあたって` または `## ＜後記＞` 末尾 |
| **ed-2** | 日本語圏は射程外（1〜3文） | ☑ | 単独可 | [`序文取込_ed2_日本語圏射程_文案.md`](./archive/反映済み文案/序文取込_ed2_日本語圏射程_文案.md) |
| **ed-6** | 序文——「インターネット美学」と「制度化」の説明節 | ☑ | 単独可。**aesthetic-rev-2 と分担** | [`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) → `archive/反映済み文案/序文取込_ed6meta1_文案.md`（2026-07-01反映） |
| **ed-7** | **序文の圧縮・読者向け再構成**——長さと入口の整理 | ☑ | **ed-6 ☑ 後** | 下記 **ed-7** 節。[`草稿.md`](./草稿.md) L3–L41（3 `###`）。**ユーザー判断で一区切り**（2026-08） |
| **ed-4** | 本稿の制度化・Cook 歴史化・著者の不确定性（後記） | ☑ | concl-1 と同批 | [`後記取込_制度化ループ_文案.md`](./archive/反映済み文案/後記取込_制度化ループ_文案.md) |
| **ed-5** | r/AestheticWiki 制度化追記（what aesthetic is this?） | ☑ | 単独可 | 第5章「分類する欲望」節（2026-06-17 反映済） |

### メタ・著者性（meta-*）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **meta-1** | 執筆動機ツイート追記 | ☑ | 単独可 | 序文（2026-07-01反映）。捨て垢・布施琳太郎のツイート2件を要約統合 |
| **meta-2** | 振り返りパート新設 | ☐ | 単独可。**優先度低・最後** | [`草稿.md`](./草稿.md) **末尾**（新 `##` 節）。11万字の定期的振り返り |
| **meta-3** | 遡行的確定——本稿が行っていることの自己言及（後記追記） | ☑ **クローズ 2026-08-13** | — | **8-reorg-1〜3 の後記改稿で本文実装済み**（草稿 L2019・L2025・L2033）。下記詳細節に検証ログ |

### 章再編・aesthetic 節（aesthetic-reorg-* / aesthetic-rev-*）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **aesthetic-reorg-0** | 第2章 `## 「aesthetic」という語` の**独立章化——考察・必要性測定** | ☑ | 単独可。**最初** | [`docs/第2章_aesthetic章分離_考察.md`](docs/第2章_aesthetic章分離_考察.md)（2026-06-19。**分離推奨・案A**） |
| **aesthetic-reorg-1** | 章分離実行（草稿・分割稿の機械移動） | ☑ | reorg-0 ☑ | 2026-06-19 反映済 |
| **aesthetic-reorg-2** | 章番号付け直し・序文章概観・相互参照・橋渡し | ☑ | reorg-1 後 | 下記詳細節 |
| **aesthetic-rev-1** | aesthetic 節/章——**文法分析**に基づく書き換え・拡張 | ☑ | reorg-0 後（reorg-1 後推奨） | [`aesthetic_文法分析メモ.md`](notes/aesthetic_文法分析メモ.md) |
| **aesthetic-rev-2** | aesthetic 節/章＋第5章——**制度化調査ノート**反映（ed-6 とセット） | ☑ | reorg-0 後。**ed-6 と並行可** | [`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) |

**推奨パイプライン（aesthetic 節のみ）**

```
aesthetic-reorg-0（考察）
    ↓ 承認
aesthetic-reorg-1 → aesthetic-reorg-2（分離・番号・橋渡し）
    ↓
aesthetic-rev-1（文法）＋ aesthetic-rev-2（制度化・ed-6 分担）
```

**ed-6 との分担**（[`aesthetic_文法分析メモ.md`](notes/aesthetic_文法分析メモ.md) 補遺A）：ed-6 で序文に足した来歴・制度化は **ed-7** で序文から外し、**制度化**定義は第5章初出。**Wikipedia AfD・EBSCO** は aesthetic-rev-2／第5章へ。

**注意**：[`khole-arena-archillect-researtch.md`](notes/khole-arena-archillect-researtch.md) の取込（**inv-khole-***）は**別調査・別パイプライン**。aesthetic 節の reorg／rev とは**独立**（下記）。

### 匿名キュレーション・normcore・Are.na（inv-khole-* / inv-cari-arena）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **inv-khole-0** | **挿入位置の測定**（VVORK→Archillect 系譜／K-HOLE／normcore／Are.na） | ☑ | — | [`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md)＋[`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md) |
| **inv-cari-arena** | **CARI の Are.na 活用——追加調査** | ☑ | inv-khole-0 ☑ | [`Arena設計思想調査ノート.md`](notes/Arena設計思想調査ノート.md)（2026-06-27） |
| **inv-khole-1a** | 文案：**第4章** VVORK 節（画像bot仕込み） | ☑ | inv-cari-arena ☑ | [`archive/反映済み文案/第4章取込_VVORK_文案.md`](./archive/反映済み文案/第4章取込_VVORK_文案.md)。草稿 L734–746（6段落） |
| **inv-khole-1b** | 文案：**第6章** サフィックス来歴（~10行）＋normcore＋K-HOLE→DIS→Are.na＋Archillect/rare.jpg（短節8-15行）。**第1章** L155 Indie Sleaze→Soft Grunge 追記（1-2文）。**第7章** L1381 を第6章後方参照に書き換え＋L1421 corecore/yabujincore 追記 | ☑ | inv-cari-arena ☑ | 草稿 `## ラベルが増えるとき` L1103–1141（6小節）＋第1章 L155＋第7章 L1383/L1421。文案 [`第6章_normcore追加_文案.md`](./archive/反映済み文案/第6章_normcore追加_文案.md) |
| **inv-khole-1c** | 文案：**第8章** CARI の Are.na 追記（L1484〜プラットフォーム論補完） | ☑ | 草稿 L1571–1577 反映済み（2026-06-29） | 同上 |

**推奨パイプライン（inv-khole 改訂）**

```
inv-khole-0 ☑（挿入位置確定：計画ファイル2件）
    ↓
inv-cari-arena ☑（Are.na 設計思想＋CARI 研究基盤。「プラットフォーム共有」確定）
    ↓
inv-khole-1a ☑（第4章 VVORK）＋ inv-khole-1b（第6章 サフィックス来歴＋normcore＋Are.na。第1章 Indie Sleaze 追記・第7章 L1355/L1395 書き換えを含む）並行可
    ↓
inv-khole-1c（第8章 CARI Are.na。実行可能——三段階知識生産フローが新材料）
```

**aesthetic-reorg との関係**：**依存なし**。並行可。khole ノートは「語彙の逆転」ではなく**画像キュレーション・ポストインターネット圏の系譜**調査。

### Megazord 追補（meg-*）

| ID | 内容 | 状態 | 依存 | 反映先 |
|---|---|---|---|---|
| **meg-1** | Megazord **Tumblr** URL を本文に追加 | ☑ | 単独可 | **草稿 L246 に現存確認**（2026-08-13 検証）。Wayback の `megazord.tumblr.com` |
| **meg-2** | Megazord **MySpace** URL を本文に追加 | ☑ | 単独可 | **草稿 L526 に現存確認**（同上）。Wayback の `myspace.com/megazordlove` |
| **meg-3** | **Gatekeeper** が Megazord MySpace にコメントしていたことの追記 | ☑ | meg-2 後推奨 | **草稿 L526 に現存確認**（同上）。「2009年9月には GATEKEEPER が Megazord の MySpace ページ…」 |

**背景**：**rev-5** ☑（[`第1章取込_Megazord_文案.md`](./archive/反映済み文案/第1章取込_Megazord_文案.md)）の追補。GATEKEEPER 自身の MySpace（L324 付近）とは別に、**Megazord 側プロフィール**の URL と、そこへの Gatekeeper コメントを足す。

**手順（各 meg-*）**

1. URL・日付を Wayback 等で**確定**（文案執筆メモに記録）  
2. 1〜2文で追記文案 → ユーザー承認 → 草稿・分割稿反映  
3. **em dash 不使用**（編集方針）

**ステータス**：☑ **meg-1〜3 すべて完了**（2026-06-30 反映／2026-08-13 に草稿現物で検証・クローズ）。この節は履歴として残す。

### 第4章・その他

| ID | 内容 | 状態 | 依存 | 備考 |
|---|---|---|---|---|
| **rev-10** | Jon Rafman 9 Eyes → liminal 前史 | ☑ | 草稿反映済（2026-06-16–17） | 第4章。9 Eyes＋Still Life/DREAM JOURNAL＋Ch2 協働接続 |
| **src-4b** | hyperpop 追記（Spotify 命名→brat summer） | ☑ | src-4 ☑ | [`第4章取込_hyperpop_Spotify-bratsummer_文案.md`](./archive/反映済み文案/第4章取込_hyperpop_Spotify-bratsummer_文案.md) |
| **rev-12** | Caretaker × liminal／Backrooms | ☐ 先送り | rev-10 関連 | 第4章 |
| — | 8番出口と liminal space 美学 | 判断待ち | — | 第4章追加可否 |
| — | 第5章 Frutiger Aero 節との整合 | 任意 | cari-draft 後でも可 | 境界論・第2章フェーズ2 |
| — | 第4章 L640 TikTok/Discord 文案 B | 任意 | — | §8 残 |
| — | KYM 訂正ログ（ファクト補強調査） | 任意 | — | §8 残 |
| — | **MySpaceデータ消失年の精度修正**——第1章L117「2019年、サーバー移行の不手際によって」は移行（2018年初頭）と公表（2019年3月）を混同している可能性。著者調査：[BBC「MySpace admits losing 12 years' worth of music uploads」](https://www.bbc.com/news/technology-47610936)。「2018年のサーバー移行、2019年3月に発覚」等へ精度を上げる | 任意 | 8-reorg（RA記事読み合わせ）で発見（2026-08-09） | 第1章L117 |
| — | **RA記事Aの「世代間の断絶」（第IV章）の取り込み検討**——業界と若い世代の好みのギャップという論点。本稿の「2014 Tumblrリバイバル」「TikTok世代への継承」（第7章）と接続できる可能性。DJ Harveyの引用（第8章後記で使用済み）自体がこのテーマを体現している | ☐ 考察のみ | 8-reorg（RA記事読み合わせ）で発見（2026-08-09） | 第7章 or 第8章 |
| — | Google Trends（aesthetic） | 任意 | — | §9-man 追補 |
| — | ブロック F →「確定」 | 任意 | — | ファクト補強 §9 |
| **inv-vernacular-photo** | non-place・匿名性の美学・poor image・ヴァナキュラー写真の接続——考察 | ☐ 考察のみ・正文未定 | 匿名性ノートの延長・並行可 | 下記詳細節 |

### inv-hypnagogic. chillwave／hypnagogic popの命名史・音楽的異同

**背景（著者提起・2026-08-09）**：第2章L385・第3章L695〜707は「hypnagogic popはchillwaveとほぼ同じ音楽群」「しばしば同義に使われた」とフラットに書いているが、実際に両ジャンルの代表曲を聴き比べると音楽的にかなり異なる（chillwaveはポップ/ダンス寄り、hypnagogic popは実験音楽/ドローン寄りで荒い）。

**調査結果（[`notes/chillwave-hypnagogicpop-Retromania_調査ノート.md`](notes/chillwave-hypnagogicpop-Retromania_調査ノート.md)、一次資料確認済み）**：

- 「同義に使われた」という記述自体は誇張ではない。2009年のPitchfork（Marc Hoganが5語を互換的に列挙）、2012年のLA Weekly、2025年12月のSimon Reynolds自身のブログ（"chillwave a/k/a hypnagogic pop"）まで、16年間一貫して同義的に扱われている。**ここは削らない**。
- ただし「同義」＝「ほぼ同じ音楽」ではない。Reynolds『Retromania』本文（p.345–346、一次確認済み）は、この一群を**3層**（chillwave寄り：Ariel Pink's Haunted Graffiti・Neon Indian・Washed Out等／コズミック・シンセ寄り：Emeralds・OPN等／トライバル・エキゾチカ寄り：James Ferraro・Sun Araw等）に分けている。CarlesがchillwaveとしたWashed Out・Neon Indianと、Keenanが2011年のFrieze誌でhypnagogic pop側として名指ししたFerraro・Sun Araw・Spencer Clark等は、ほぼ重ならない。
- David Keenan自身が2011年1月（The Wire誌323号）、chillwaveを自分が名付けた運動の「意味のない通称」「無思考で脱政治化された」堕落形と呼び、**分岐を宣言**している。
- 「数週間後」という時系列表現は要再検討（The Wire306号の実発売日が表紙月表記より早い可能性、状況証拠のみで確定はしていない）。

**反映方針（未定稿）**：「批評語としては同義的に流通したが、名指しされた顔ぶれは最初からズレており、のちに命名者自身が『商業性 vs 実験性』の分岐を宣言した」という弧のある記述に書き換える。詳細は調査ノート§4。

**手順**：①調査ノート§4を踏まえ文案を書く（第2章L385は短く、第3章L695〜707は分岐の経緯まで含めて厚めに） ②草稿反映 ③分割稿同期は任意。

**計画正本**：[`docs/inv-hypnagogic_取り込み計画.md`](docs/inv-hypnagogic_取り込み計画.md)（2026-08-19。Wire 306＝表紙月表記／文案は計画書 §文案 に集約／承認後に草稿直反映）

**ステータス**：☑ 調査完了（2026-08-09）。☑ 計画承認・草稿反映（2026-08-19。[`草稿.md`](./草稿.md) 第2章 L379・L385、第3章「hypnagogic pop と二重の命名」節・憑在論節）。☑ 反映後の再推敲完了（2026-08-19。帰属の曖昧さ1件修正、節の接続・チェックリスト8項目を確認）。**完了**。

---

### inv-vernacular-photo. non-place・匿名性の美学・poor image・ヴァナキュラー写真——接続の考察

**背景（ユーザー提起・2026-07-07）**
本稿にはすでに次の4つの糸がそれぞれ別の章で語られている。

| 糸 | 章 | 出典・草稿位置 |
|---|---|---|
| ヴァナキュラーウェブ（vernacular web） | 第1章 | Olia Lialina の用語。草稿 L71 |
| 匿名性の美学（作り手のペルソナ→画像の出自の消失） | 第2・4・7章 | rev-9／src-6f→[`匿名性の美学_後半展開_論点ノート.md`](notes/匿名性の美学_後半展開_論点ノート.md)。草稿 L1448 |
| poor image／ゴミ画像 | 第4章 | Hito Steyerl・Nukeme。草稿 L832–838（inv-steyerl ☑）・L850–852 |
| non-place（非-場所）／anemoia | 第7章 | Marc Augé・John Koenig。草稿 L1460（liminal space節）・L1520（Dreamcore節） |

これらは個別には書かれているが、**互いの接続は本文でもノートでも明示されていない**。以下は2026-07-07の対話で出た考察を、時系列の追記ではなく論点ごとに整理したもの。

**核になる仮説（1行）**

> 特定性（歴史・関係・アイデンティティ）の欠如は感覚を消すのではなく、匿名性でなければ生まれない固有の感覚——質感・既視感・懐かしさ——を生み出す。

以下の観察は、すべてこの1行にぶら下がる。

1. **二層の非-場所性**——草稿はすでに両方を書いているが、接続していない。L1448（`## r/LiminalSpaceとReddit` 節末、画像の匿名化＝「プラットフォームをまたいで転載が重なるうち、オリジナルが何だったのかは消える」）と L1460（`## 世界がliminal化した` 節、描かれた場所の非-場所性＝「Marc Augéが…non-place と呼んだ、まさしく匿名の通過が想定される空間」）は隣接する節にありながら、同じ語（non-place）で結ばれていない。liminal space は**モチーフとしての非-場所**（空港・モール・廊下という、関係性も歴史もアイデンティティも持たない被写体）と、**画像としての非-場所**（撮影者・文脈・キュレーターの痕跡を失い、匿名の閲覧者が摩擦なく消費していく画像そのもの）の二重構造を持つのではないか。草稿は現状「画像論」として匿名性を語り（L1448）、「場所論」として non-place を語る（L1460）という役割分担のままになっている。

2. **poor image／ゴミ画像との理論的対応**——[Oxford Reference](https://www.oxfordreference.com/display/10.1093/oi/authority.20110803100237780)／[Wikipedia](https://en.wikipedia.org/wiki/Non-place)の定義によれば、Augé の非-場所は「ATMが銀行員より速い、回転式改札の方が摩擦がない」という機能主義（関係を排した効率性）を核にする。Steyerl の poor image（L832–838。劣化しながら速く広く出回ることに価値がある）、Nukeme の「ゴミ画像」（L850–852。意図も出どころも読めない画像が与える「混乱を楽しむ」感覚）は、**画像における同じ機能主義**として読める。「poor image は画像における non-place、non-place は空間における poor image」という対応が成立するなら、第4章と第7章をまたぐ接続になる。

3. **anemoiaの発生条件も同じ論理で説明できる**——anemoia（L1520。John Koenig、2012年、「自分が知ったことのない時代や場所へのノスタルジア」）は、non-place の定義（歴史性・関係性・アイデンティティの不在）そのものから生まれると読める。ある場所が誰か一人の記憶にも固有に属さないからこそ、不特定多数の記憶に部分的に触れられる。行ったことのない場所が懐かしいのは、その場所が無数の似た経験（蛍光灯の廊下、モールの一角）の統計的な合成物のように働き、どの記憶にも一致するが、どの記憶にも固有には属さないからだ、と言い換えられる。非-場所性は anemoia の副作用ではなく発生条件。これは2の「質感」と対になる——空間の匿名性がanemoiaを、画像の匿名性がゴミ画像の質感を生む。

4. **Weirdcore／Dreamcoreの分岐も同じ軸で説明できるかもしれない**——L1512–1518 は Weirdcore（違和感の増幅として設計されたビジュアル）と Dreamcore（anemoiaを作り出すビジュアル）を並べているが、共通の生成源（文脈・出自不明の視覚素材）には触れていない。上記の軸を通せば、Weirdcore＝匿名性が生む不気味さ、Dreamcore＝匿名性が生む懐かしさ、という対として整理できる可能性がある。

5. **cursed imagesの二重の脱文脈化**——cursed images は見つけた人が「奇妙さ」を選ぶファウンドフォト的な能動的キュレーション行為から始まる（一段階目の文脈が残る）。しかし転載が重なると、原作者だけでなく**この最初の発見者・キュレーターの文脈も失われる**（二段階目の脱文脈化）。L1448「プラットフォームをまたいで転載が重なるうち」はこの二段階目を指していると読める。

6. **「インターネット／SNSは場所か非-場所か」という軸**——第1章の「土壌」（GeoCities・MySpace・Tumblrブログ）は、HTML/CSSカスタマイズ（アイデンティティ）・リブログの蓄積（関係性）・タグやアーカイブ（歴史）を持ち、Augéの定義における「場所」側にある。対して TikTok の For You やアルゴリズム的な画像流通（Archillect 等）は、「匿名の群衆への摩擦のない通過」という非-場所の定義に近い。この軸が成立するなら、本稿全体の「土壌→プラットフォーム拡大→アルゴリズム的流通」という流れを非-場所化のプロセスとして読み直せる。Oxford Referenceの「誰もが等しく疎外されているがゆえに、誰もが等しく『くつろげる』」という逆説は、liminal spaceの普遍的既視感の理論的な説明にもなりうる。第7章 TikTok/For You 論（`§8-2_Tumblr_ForYou_調査メモ.md`）との接続候補。

7. **vernacular photographyとの歴史的並行**——ヴァナキュラー写真（スナップ・家族写真・拾われた写真など、当初は美術的価値を意図されなかった写真群）は、のちに収集家・キュレーターが遡って「ジャンル」として発見・分類し、展覧会やアーカイブの対象にした、という制度化の経緯を持つ。Olia Lialinaの「ヴァナキュラーウェブ」はおそらくこの語からの転用（要検証）。成立するなら、この糸は**meta-3（遡行的確定・本稿の自己言及）**とも合流する——vernacular photographyが後から収集・分類されてジャンル化した歴史は、本稿がインターネット美学に対して行っていること（匿名の画像群に名前を与え、歴史を書く）の先行例として使える可能性がある。

**現時点での留保**

- vernacular photography が実際に vernacular web の語源であるかは未確認（Olia Lialina の原文・インタビューでの言及有無を要調査）。こじつけにならないよう、確認できない場合は「類似の発想」程度の弱い接続にとどめる。
- 7つの観察を無理に一本の理論にまとめると、6-reorg で廃止したばかりの「造語による理論武装」と同じ轍を踏む。既存の具体的な記述（画像・タグ・投稿）を主語にする本稿の書き方を踏襲し、新しい抽象概念（「非-場所的画像」等の新造語）は増やさない方針で臨む。
- 反映するとしても本文どこか一箇所に大きな新設節を作るより、liminal space節内の橋渡し（1・2文）＋後記かmeta-3への軽い合流、という分散型の反映が本稿の構成に馴染む可能性がある。挿入位置は調査後に判断。

**手順（着手する場合）**

1. vernacular photography の定義・代表的な論者（例：Geoffrey Batchen 等）と、Olia Lialina の vernacular web 命名の経緯（語源に言及した一次資料があるか）を調査
2. 7つの観察のうちどれが「こじつけ」でなく本稿の実証的トーンで書けるか、調査結果をもとに取捨選択（全部を使う必要はない）
3. 成立する場合のみ、`匿名性の美学_後半展開_論点ノート.md`または新規ノートに考察を記録 → 文案 → liminal space節／後記／meta-3に反映
4. 成立しない・弱いと判断した場合は「不採用」として本ファイルまたは匿名性ノートの「不採用・見送り」欄に理由とともに記録

**ステータス**：**部分反映済み**（2026-07-23）。観察1（二重の非-場所・中心）・3・4（任意）・2（任意の1文）は **7-reorg** ☑（[`docs/第7章_reorg_計画.md`](docs/第7章_reorg_計画.md) §4-5・§4-9）で [`草稿.md`](./草稿.md) 第7章へ反映済み。観察5・6は見送り、観察7（vernacular photography 語源）は要調査のまま **meta-3 着手時に検討**。

### Seapunk 後続・第2章残（任意）

| ID | 内容 | 状態 | 備考 |
|---|---|---|---|
| **6b-reorg 後続** | M.I.A.・Tim and Eric（激怒記事直後） | ☑ | [`Seapunk取込_6b-reorg後続_MIA_TimEric_文案.md`](./archive/反映済み文案/Seapunk取込_6b-reorg後続_MIA_TimEric_文案.md) |
| **6b-reorg 後続** | H∆SHTAG$ ep5 厚み（seapunk 節） | ☑ | RBMA字幕反映でカバー（2026-08） |
| **RBMA字幕** | ep5/ep6 字幕の草稿反映（Zombelle NYT・Nate・Charli 等） | ☑ | [`docs/RBMA反映計画.md`](docs/RBMA反映計画.md)（2026-08）。**Le1f avatar（r03）は意図的に削除** |
| **6c 残** | L254 接続文・年表順の整理 | ☐ | Cluster Mag 直後 |
| **6d-review 残** | 分量・時系列、seapunk 節との接続 | ☐ | witch house 節 |
| **6b 残** | 文案メタ混入チェック、VICE 年表著者明示 | ☑ 2026-08-13 | **草稿 L771 で著者明示を確認**（「Lil Internet と Lil Government 自身による年表だ。2012年3月、VICE…」）。メタ混入は fractal-3 の全節通過で解消 |

**原則**：草稿に調査ノート § 参照は入れない（公開 URL のみ）。メタは文案の執筆メモ。

---

## 進捗サマリー

| # | フェーズ | 状態 | 成果物 |
|---|---|---|---|
| 1 | ブロック F（D/F 重複）の推敲 | ☑ | 草稿改稿（ニュアンス未確定） |
| 2 | 音楽ジャンル・美学・デザインスタイルの境界 | ☑ | 第2章境界論段落（第5章段落は未） |
| 3 | ドキュメント整理①（第1・2章中心） | ☑ | 差分リスト＋更新方針 |
| 4 | ファクト補強——第3〜5章 | ☑ | 章別文案→草稿（#11〜22・訂正1件） |
| 5 | ドキュメント整理②（全体同期） | ☑ | 第3〜5章分割稿・README 等 |
| **6a** | Seapunk 調査ノート——影響評価（統合しない） | ☑ | [`docs/Seapunk調査_取り込み計画.md`](docs/Seapunk調査_取り込み計画.md)（6b〜6f 実行済） |
| **6b** | Seapunk 本体の段階取込 | ☑ | 文案→草稿 第2章 seapunk 節（2026-06-02） |
| **6c** | aesthetic 年表——中間層の段階取込 | ☑ | 文案→草稿 第2章 aesthetic 節（2026-06-02） |
| **6b-reorg** | seapunk 初期節の叙述順・節構成の整理 | ☑ | 改稿版文案→草稿反映（2026-06-02） |
| **6d** | witch house 前史——§2 還流（hypnagogic 小節） | ☑ | 草稿 L143 差し替え（2026-06-02）。**本文は要再検討** → **6d-review** |
| **6d-review** | 第2章 chillwave／憑在論／witch house 節の改稿 | ☑ | 草稿反映・案A ####・vaporwave 前史接続（2026-06-02） |
| **6e** | vaporwave 接続——段階取込 | ☑ | 文案→草稿 `## seapunkの死と遺産`（2026-06-02） |
| **6f** | Seapunk 後続（VICE 年表節・MASSAGE 9・slimepunk） | ☑ | 方針 A 反映済（2026-06-02） |
| 7 | ドキュメント整理③（Seapunk 取込後） | ☑ | 第2–4章分割稿・§5 還流・後記 L841（2026-06-02） |
| §8 | 序文改稿・Tumblr For You・KYM Wayback | ☑ | 草稿・分割稿一部（§8-1〜3、2026-06-01） |
| **§9** | aesthetic 包含関係・語法分析 | ☑ | 文案→草稿 aesthetic 節（2026-06-02） |
| **§9-man** | [`aestheticに関する手動調査.md`](notes/aestheticに関する手動調査.md)——草稿反映 | ☑ | §9 文案に統合反映 |

**依存関係（完了フェーズ・履歴）**

```
1 → 2 → 3 ─────────────────────────→ 5
              4（第3〜5章）──────────↗
1, 2 完了後 → 6a → 6b → 6c → 6b-reorg → 6f → 6d-review → 7 → §9 ＋ §9-man ☑
```

**現行パイプライン**は §アクティブ・パイプライン を参照。

---

> **未完了タスクの一覧は §タスク索引 を正本とする。** 以下は ID ごとの手順書。

---

## レビュー論点メモ由来（rev-*）

正本：[`docs/草稿_レビュー論点メモ.md`](docs/草稿_レビュー論点メモ.md) §13。§9・6d-review 完了後の改稿バックログ。

| ID | 内容 | 状態 | 文案（案） |
|---|---|---|---|
| rev-11 | L564 未完成文・L512 要検証 | ☑ | 推敲メモ 続39 |
| rev-1 | 第1章 Reblorg 節 | ☑ | `archive/反映済み文案/第1章取込_Reblorg_文案.md` |
| rev-2 | Internet Archaeology＋One Terabyte | ☑ | `archive/反映済み文案/第1章取込_GeoCities土壌_文案.md` |
| rev-3 | dump.fm／Jogging／流れ2 | ☑ | 上記に統合 |
| rev-4 | ムードボード対比 | ☐ | `第1章取込_ムードボード対比_文案.md` |
| rev-5 | Megazord 修正 | ☑ | `第1章取込_Megazord_文案.md` |
| rev-6 | aesthetic 大仰さ総括 | ☑ | `archive/反映済み文案/第2章取込_aesthetic大仰さ_文案.md` |
| rev-7 | 三読み＋2016 政治化 | ☑ | 文案・草稿反映（2026-06-02）。推敲メモ 続45 |
| rev-8 | Eccojams vs FSV | ☑ | [`第2章取込_FSV対比_文案.md`](./archive/反映済み文案/第2章取込_FSV対比_文案.md)（2026-06-16 反映済） |
| rev-9 | witch house 匿名性 | ☑ | src-6f に統合・反映済（2026-06-16）。[`第2章取込_witchhouse匿名性_文案.md`](./archive/反映済み文案/第2章取込_witchhouse匿名性_文案.md) |
| rev-10 | 9 Eyes → liminal | ☑ | 草稿・分割稿反映済（2026-06-16–17）。9 Eyes＋Still Life/DREAM JOURNAL＋Ch2 協働接続。文案なし（直書き） |
| rev-12 | Caretaker × liminal／Backrooms | ☐ 先送り | 上記「第4章 Caretaker×liminal」と同一 |

**推奨着手順（2026-06-22 以降）**：**ed-6** polish／**intro-kojiateki**（並行可）。**inv-vektroid** は**低優先・後回し**。**meta-1**／**meta-2** は後回し（meta-2 は草稿末尾・最後）

### rev-7 進捗——**完了（2026-06-02 拡張反映）**

☑ 調査 [`vaporwave政治化_調査ノート.md`](notes/vaporwave政治化_調査ノート.md) → [`第2章取込_vaporwave政治化_文案.md`](./archive/反映済み文案/第2章取込_vaporwave政治化_文案.md) → 草稿 L426–452・分割稿同期。推敲メモ 続45。

**任意残**：obakeweb／togetter、Boriswave（同ノート §6）。r/vaporwave 声明・weaponized nostalgia は打ち切り ☒。

## 外部調査ノート由来（src-*）

| ID | 内容 | 状態 | 文案（案） | 依存 |
|---|---|---|---|---|
| src-1 | musicplusghost 洗い出し | ☑ | 草稿反映なし | 2026-06-22 確定。下記 §src-1 |
| src-2 | SuperSuper! Magazine 追記 | ☑ | [`第2章取込_SuperSuper_文案.md`](./archive/反映済み文案/第2章取込_SuperSuper_文案.md) | 草稿・分割稿反映済（2026-06-11） |
| src-5 | vaporwave前史見直し（Hippos In Tanks） | ☑ | [`第2章取込_vaporwave前史_文案.md`](./archive/反映済み文案/第2章取込_vaporwave前史_文案.md) | コア反映・分割稿同期（2026-06-11） |
| src-6a–f | MP3ブログ調査ノート——仕分けと段階取込 | ☑ | [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) → 章別文案 | 6a–6f 完了（2026-06-16） |
| src-3 | r/witchhouse 歴史スレ参照 | ☑ | 草稿・分割稿反映済（2026-06-17）。`#### コミュニティの正史` 末尾に1文+URL | rev-9 と重複注意 |
| src-4 | ハイパーポップの歴史（PC Music 厚み） | ☑ | `archive/反映済み文案/第2章取込_ハイパーポップ_文案.md` | src-2 後（src-5 と並行可。cari-draft の前提） |
| src-4b | ハイパーポップ追記（Spotify 命名→brat summer） | ☑ | `第4章取込_hyperpop_Spotify-bratsummer_文案.md` | src-4 ☑ |

### src-1. musicplusghost.md——参考箇所の洗い出し——**完了（2026-06-22）**

**背景**  
平山悠編『MUSIC + GHOST : FEECO Magazine extra issue』（憑在論・Ghost Box・英国郊区派）。草稿 `#### 憑在論と郷愁の言語`（L173）で ZINE 名と [atochietebura リンク](https://atochietebura.com/HD/h024.html) は**既出**。本タスクは全文（[`musicplusghost.md`](./sources/transcripts/musicplusghost.md)）から**追記に値する箇所を選別**する。

**洗い出し候補（優先度順）**

| 調査ノート § | 内容 | 草稿の行先候補 |
|---|---|---|
| 序文・Ch1 Twisted Memories | Ghost Box／郊区派 hauntology（Burial 偏重の補正） | 憑在論小節 L173 付近 |
| Ch2 Memory Digger | Jim Jupp（Ghost Box）インタビュー | 同上 or witch house 前史 |
| Ch5 Beyond the Dead Future | 90年代後半ビデオゲーム再読 | vaporwave 前史・Megazord 文脈 |
| Extra / Ch6 | 日本の憑在論受容・個人的郷愁の限界 | 憑在論小節（短い注記に留めるか判断） |

**手順**

1. [`musicplusghost.md`](./sources/transcripts/musicplusghost.md) を章単位で読み、上表に**採用／保留／射程外**を付ける  
2. 採用候補ごとに公開 URL・部分引用を文案に整理（正文は URL のみ）  
3. [`草稿.md`](./草稿.md) 反映 → 分割稿同期  

**注意**：FEECO 誌面の長文引用は避け、既出の MUSIC+GHOST 言及と**重複しない**範囲で足す。

**洗い出し結果（2026-06-22）**——採用は**任意**。必須追記なし。

| 判定 | 箇所 | 草稿との関係 | メモ |
|---|---|---|---|
| **A 任意** | 序文 | L237 憑在論節 | 日本語圏メディアは Burial／クラブ偏重、Ghost Box 郊外派は相対的に見えにくい——**1文脚注**可（ed-2 射程） |
| **A 任意** | Ch2 Jim Jupp インタビュー | 同上 | デジタル以前の記憶・TV 子供時代の音の**感情的重構**（正確な復元ではない）。Ghost Box 節の**具体化**に最も使える |
| **A 任意** | Ch5＋Jupp（WIRE 2012 経由） | L233–237／L384 付近 | Julian House：Ferraro＝壊れた鏡の iPad 感 vs Ghost Box の時間塊——hypnagogic／米国憑在の**対比1文** |
| **A 任意** | Ch5 Reynolds 論 | L233 Keenan 節 | 『Retromania』「国ごとの憑在論」——米国＝hypnagogic。命名済み論点の**批評語彙**補強 |
| **B 保留** | Ch1 Twisted Memories | 第5章制度化？ | Scarfolk／Tumblr 経由のレトロ商業化、Fisher 資本主義リアリズム——**憑在論の消費化**1文なら可。長い |
| **B 保留** | Ch2 liminal／vaporwave 質問 | 第4章 liminal | Fisher×Ghost Box（Non-Place、Pye Corner Audio）。Caretaker 節と近いが**本稿は別ルート** |
| **— 射程外** | Beyond the Dead Future | — | PS1 個人回想・Mother2/LSD・ゲーム CM ノスタルジー。草稿のゲーム言及（Savvy J 等）と**軸がずれる** |
| **— 射程外** | Extra／Bring Back My Ghost | — | 日本憑在音楽ガイド、個人郷愁の限界（著者メタ）。ZINE 言及で**足りる** |
| **— 既出** | Ghost Box／Keenan／Fisher／Factory | L237 等 | ファクト骨格は草稿済。Jim Jupp 名・Julian House WIRE 評は**未出**だが必須ではない |

**結論**：追記不要。**草稿反映は行わない**（2026-06-22 確定）。

**ステータス**：☑ **完了**（2026-06-22）。洗い出しのみ。文案・草稿反映なし。

---

### src-2. SuperSuper! Magazine——**完了（2026-06-11）**

☑ [`supersuper.md`](notes/supersuper.md) → [`第2章取込_SuperSuper_文案.md`](./archive/反映済み文案/第2章取込_SuperSuper_文案.md) → 草稿・分割稿同期。推敲メモ 続50–51。

### src-5. vaporwave前史（HIT）——**完了（2026-06-11）**

☑ [`HipposInTanks_調査ノート.md`](notes/HipposInTanks_調査ノート.md) → [`第2章取込_vaporwave前史_文案.md`](./archive/反映済み文案/第2章取込_vaporwave前史_文案.md) → 草稿 L239–249。推敲メモ 続52–53。

### src-6. MP3ブログ時代とエクスペリメンタル・シーン——段階取込

**正本（仕分け・フェーズ）**：[`docs/src-6_仕分け.md`](docs/src-6_仕分け.md)  
**調査資料**：[`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](notes/MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md)

第1章〜第2章にまたがる19節＋スレッド3本。**1文案にまとめられない**ため Seapunk 6a 型で段階化。

| ID | 内容 | 状態 |
|---|---|---|
| **src-6a** | 仕分け確定（§1–§19、委譲表、スレッドA/B/C） | ☑ |
| **src-6b** | 第2章・前史 §2・§3・§6（Block A はおさらい化） | ☑ 草稿反映済 → [`第2章取込_mp3blog前史_文案.md`](./archive/反映済み文案/第2章取込_mp3blog前史_文案.md) |
| **src-6c** | 第1章・プラットフォーム §1 mp3ブログ／§17 MySpace／§18 Tumblr補強 | ☑ 草稿反映済 → [`第1章取込_プラットフォーム_文案.md`](./archive/反映済み文案/第1章取込_プラットフォーム_文案.md) |
| **src-6d** | 第2章・命名系譜 §12–§13 | ☑ 草稿反映済 → [`第2章取込_命名系譜_文案.md`](./archive/反映済み文案/第2章取込_命名系譜_文案.md) |
| **src-6e** | 第2章・アーキテクチャ §10 | ☑ 草稿反映済（2026-06-16） |
| **src-6f** | 匿名性 §7 → **rev-9** と統合 | ☑ 草稿反映済（2026-06-16） |

**役割分担（2026-06-15）**：§1 mp3ブログ**一般**は第1章の新設節（6c）へ移設。第2章 Block A（6b）は「第1章で見た mp3ブログ」の**おさらい**＋20jfg・Tri Angle に絞る。第1章は mp3ブログ節と MySpace 節を**別立て**。

**src-5 との重複**：§4 HIT・§16 *Young Chronos* は **射程外**（src-5 ☑）。§14 *Exo* は第4章 or 第1章 L91。詳細は仕分け表の委譲表。

**手順**（各フェーズ共通）

1. [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) で対象節・行先・第1章 節構成案を確認  
2. 文案 `第*章取込_*_文案.md` を作成  
3. [`草稿.md`](./草稿.md) 反映 → 分割稿同期 → 推敲メモ  
4. 仕分け表の「文案／草稿反映」列と本ファイル索引を ☑ 更新  

**次の1手**：**ed-6** polish／**intro-kojiateki** 等。**inv-vektroid** は低優先・後回し。**ed-3** ☑（分割稿同期のみ任意）。**inv-opn-cook** ☑（2026-06-22）。

---

### inv-vektroid. Vektroidの名義増殖とシーン形成——調査（src-6f 派生）

**背景**  
[`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) スレッドBで浮上した仮説：Vektroid（Ramona Andra Xavier）が2011年に複数名義で短期間に大量リリースしたことが、外部から「複数アーティストによるシーン」のように映り、vaporwave の認知・定着を後押しした可能性。

**調査事項**

- Vektroid 2011 各名義のリリース時期・本数（Bandcamp・Discogs・Wayback）
- 当時のフォーラム等で「同一人物」と認識されていたかの記録
- Beer on the Rug カタログにおける名義の並び（src-6b §3 と関連）
- 既存 Seapunk／vaporwave政治化ノートへの関連記述

**ステータス**：調査のみ。**正文は書かない**。**低優先・後回し**（2026-06-22）。

**手順**

1. 調査結果をノートにまとめる（`Vektroid_調査ノート.md` または既存追記）  
2. 結果を [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) スレッドB／6b（L254）へ還流  
3. 裏付けなしの場合は Vektroid 2名義併記への軽い接続のみ残す

---

### inv-msv. Post T.V. / AAVV——**完了（2026-06-17）**

☑ [`第2章取込_lofi映像Post-TV_文案.md`](./archive/反映済み文案/第2章取込_lofi映像Post-TV_文案.md) → 第2章「Post T.V.」節。派生：inv-swan／inv-dclub。

### inv-swan. Daniel Swan——lo-fi から HD 美学への軌跡

**背景**  
Daniel Swan は inv-msv で扱う「Post T.V. - Lo-Fi For The Eyes」（2010, ローマ国際映画祭）の参加者の一人。出発点は lo-fi 寄りで、2010年の短編映画『[Lux Laze](https://u-t-t-e-r.bandcamp.com/album/lux-laze)』は全編 VHS 撮影、サウンドトラックを **Jack Latham（Jam City）** が担当し、VHS＋コミック＋DVD-R のセット＋50本限定カセットという物理形態で自主リリースされた。その後 Swan は高精細・CGI 寄りの HD 美学へ転回し、PC Music 周辺の主要な映像作家になる。Post-TV 文案（[`第2章取込_lofi映像Post-TV_文案.md`](./archive/反映済み文案/第2章取込_lofi映像Post-TV_文案.md)）では「転回の起点」として軽く前振りするにとどめ、軌跡の本格的整理はここで行う。

**確認済み事実（要草稿位置検討）**

| 事項 | 年 | 典拠 |
|---|---|---|
| 『Lux Laze』（全編VHS・Jack Latham サントラ・VHS/コミック/DVD-R/50本カセット） | 2010 | [Utter Bandcamp](https://u-t-t-e-r.bandcamp.com/album/lux-laze) |
| DIS Magazine が特集（"I'm in love, his name, Daniel Swan"） | 2012 | [DIS Magazine](https://dismagazine.com/blog/29818/im-in-love-his-name-daniel-swan/) |
| A.G. Cook が声がけ、PC Music 関与開始 | 2012〜 | [Dazed 100](https://www.dazeddigital.com/projects/article/22392/1/daniel-swan-interview) |
| Dux Content「Lifestyle」MV | 2013 | [Vimeo](https://vimeo.com/80669303) |
| Jam City・Rustie・RL Grime 等の MV、Thy Slaughter カバー、PC Music 用ループ映像 | 2012〜 | [Dazed 100](https://www.dazeddigital.com/projects/article/22392/1/daniel-swan-interview)・[dmy.co](https://dmy.co/features/music-visual-artist-interview-gallery-feature-2014) |
| Lifesim「IDL」MV | 2015 | [YouTube](https://www.youtube.com/watch?v=SySgCOwaeLk) |
| Ecco2k「GT-R」MV（Dir/VFX、Drain Gang） | 2017 | [YouTube](https://www.youtube.com/watch?v=raLQWq_PRIE) |

**論点**  
- 「lo-fi の質感から出発した作家が HD 美学へ転回する」という個人史が、シーン全体の lo-fi → HD/distroid/PC Music の流れを縮図的に示す好例。distroid 節・PC Music 節との接続を検討。
- Jam City（Jack Latham）経由で inv-dclub（Night Slugs / deconstructed club）と連結。
- Ecco2k / Drain Gang への接続は本書の射程（時期・主題）を超える可能性があり、どこまで触れるか要判断。

**ステータス**：☐ 調査メモ作成・草稿接続検討から（計画先行）。

---

### inv-dclub. Night Slugs / Fade To Mind——**完了（2026-06-17）**

☑ [`第2章取込_deconstructedclub_文案.md`](./archive/反映済み文案/第2章取込_deconstructedclub_文案.md) → PC Music 節後「並走」節。

### inv-steyerl. Hito Steyerl「貧しいイメージの擁護」——**完了（2026-06-17）**

☑ [`第2章取込_steyerl_文案.md`](./archive/反映済み文案/第2章取込_steyerl_文案.md) → Post T.V. 節末 `####`。

### inv-piajp. 日本のポストインターネットアート受容——**完了（2026-06-17）**

☑ [`第1章取込_piajp_文案.md`](./archive/反映済み文案/第1章取込_piajp_文案.md) → 第1章 Designing Tumblr 直後。

### inv-tabor. Tabor Robak——ネットワーク節点の整理

**背景**  
Tabor Robak（ポートランド出身、のちにニューヨーク移住）は草稿に断片的に登場するが、複数の章にまたがる接続点として機能している。以下の接続が確認されており、草稿には括弧注として2点反映済み（2026-06-17）。

**確認済み接続（草稿反映状況）**

| 作品・活動 | 年 | 反映状況 |
|---|---|---|
| **Jon Rafman** と *BrandNewPaintJob.exe*（*BNPJ-EXE*）共作 | 〜2009（GATEKEEPER MySpace 出会い以前） | 未反映 |
| Fatima Al Qadiri「**Vatican Vibes**」MV 監督 | 2011 | 草稿 L439・分割稿に括弧注追記済み |
| Ford & Lopatin「**World of Regret**」MV CGI・アニメーション | 2011 | 草稿 L318・分割稿に反映済み |
| **#HDBOYZ** メンバー（ADR・Ryder Ripps ら） | 2011 | 草稿 L598 既出 |
| **GATEKEEPER *Exo*** アートワーク + Unity ゲーム環境デザイン | 2012 | 草稿 L598・分割稿に括弧注追記済み |
| **ADR *Deceptionista*** ビデオゲームデザイン | 2016 | 草稿 L994 既出 |

**重要な未反映事項**  
- **Rafman ↔ Robak**（*BrandNewPaintJob.exe*）: GATEKEEPER は MySpace で Robak に出会い、当時の Robak の唯一の実績が Jon Rafman との共作だった（[Wikipedia Gatekeeper](https://en.m.wikipedia.org/wiki/Gatekeeper_(band))）。Rafman は第4章（9 Eyes・DREAM JOURNAL）に既出——第2章と第4章が Robak を介して接続する。
- Vatican Vibes は **New Museum 個展**（2011年10月21日、Genre-Specific Xperience）で上映され、2014年には Barbican Centre「Digital Revolution」にも出展。

**調査事項**

- *BrandNewPaintJob.exe* の内容・公開経緯を確認し、Rafman ↔ Robak 接続を草稿のどこかに記録できるか検討
- Robak の活動の章をまたいだ位置づけを整理し、必要なら脚注 or 短い注記として正文に追記

**ステータス**：**暫定反映あり・要計画**。草稿 L439・L598 の括弧注（Vatican Vibes MV、Exo アートワーク/ゲーム）は2026-06-17 に直書きで追記したが、計画なしの追加であり内容・位置づけを後日あらためて検証する。**今後の作業は必ず計画（文案ファイル or 追記方針）を先に立ててから草稿に反映すること。**

---

### inv-oesb. OESB × OPN「Time Decanted」——**完了（2026-06-17）**

☑ 草稿 L314 OESB 言及直後・分割稿に1文追記。[Vimeo](https://vimeo.com/7616034)

### inv-frkwys. FRKWYS Vol.7——**完了（2026-06-17）**

☑ 草稿 L314 末尾・分割稿に2文追記。[Discogs](https://www.discogs.com/ja/master/353721-Borden-Ferraro-Godin-Halo-Lopatin-FRKWYS-7-)

### inv-opn-cook. OPN × A. G. Cook——vaporwave 系譜と PC Music の交差

**背景（ユーザー指示・2026-06-19）**  
Daniel Lopatin（Oneohtrix Point Never、OPN）は、『Memory Vague』（2009）・sunset corp.・『Chuck Person's Eccojams Vol.1』（2010）を通じて **proto-vaporwave／vaporwave オリジネーター**の一人として本稿で既出（第2章 L273–287）。A. G. Cook は **PC Music** の創設者として同章後半（L603–）で叙述済み。ふたりは**たびたびコラボレーション**しており、**減速・ノスタルジア側（vaporwave）と加速・人工性側（PC Music／hyperpop）の分岐が、人物レベルで交差していた**ことは本稿の系譜論上、重要な接点になる。

**草稿の現状**

| 箇所 | 内容 | 不足 |
|---|---|---|
| L613 | SuperSuper! が MEGAZORD・**OPN**・DIS を同列紹介→PC Music 人脈 | **OPN×Cook 直接協働**は未記 |
| L623–624 | vaporwave と PC Music の**対置** | 交差する例外として OPN が書かれていない |
| inv-oesb／inv-frkwys ☑ | OPN の 2010–2011 圏（OESB MV・FRKWYS） | Cook 以前の文脈。本タスクとは別 |

**調査済みコラボ候補（文案前に年表確定）**

| 年 | 内容 | 出典 |
|---|---|---|
| **2014** | 共作曲 **「Bubs」**（OPN × A. G. Cook） | [Pitchfork（2014-12）](https://pitchfork.com/news/57890-oneohtrix-point-never-shares-new-tracks-rush-and-bubs-collaboration-with-pc-musics-ag-cook/) |
| **2016** | Cook による OPN「**Sticky Drama**」リミックス（*Garden of Delete*） | [The FADER（2016-12）](https://www.thefader.com/2016/12/18/ag-cook-oneohtrix-point-never-sticky-drama)／[Bandcamp](https://oneohtrixpointnever.bandcamp.com/track/sticky-drama-a-g-cook-remix) |
| **2021** | Cook による OPN「**Lost But Never Alone**」リミックス | [Wikipedia: A. G. Cook discography](https://en.wikipedia.org/wiki/A._G._Cook_discography) |

**調査事項（文案前）**

- 上表以外の公式協働（リミックス・共作・ライブ・クレジット）の洗い出し  
- SuperSuper! ネットワーク（L613）と 2014「Bubs」の**時間的接続**を1文で足せるか  
- ed-4 後記の Cook 言及（Spotify プレイリスト）との**住み分け**（本タスク＝系譜・音楽的交差、ed-4＝制度化）

**論点（本文で言いたいこと）**

- vaporwave の**オリジネーターの一人**が、のちに PC Music 創設者と**反復的に協働**した  
- 第2章の「vaporwave vs PC Music／hyperpop **対置**」（L623–624）を**否定するのではなく**、同じポストインターネット世代の**別分岐が交差しうる**具体例として書く  
- Daniel Swan 橋（deconstructed club→PC Music）とは別軸：**音源・リミックスとしての直接協働**

**挿入位置（案）**

| 優先 | 行先 | 理由 |
|---|---|---|
| **A（推奨）** | L623–624 **対置段落の直後** | 対比のあとに「交差」1段落で締める |
| B | L613 SuperSuper! 段落の直後 | 人脈の延長として前振り |
| C | QT／Charli 叙述の後（L619–621 付近） | 2014「Bubs」と時系列的に近い |

**手順**

1. コラボ年表を確定（調査メモ `inv-opn-cook_年表.md` または文案執筆メモ内）  
2. 文案 `第2章取込_OPN_Cook_文案.md`（**1〜2段落上限**。代表例2〜3件＋URL）  
3. ユーザー承認 → [`草稿.md`](./草稿.md) 反映 → [`第2章_命名の時代.md`](manuscript/第2章_命名の時代.md) 同期  
4. **em dash 不使用**

**ステータス**：☑ 草稿反映済（2026-06-22）。[`inv-opn-cook_年表.md`](notes/inv-opn-cook_年表.md) → [`第2章取込_OPN_Cook_文案.md`](./archive/反映済み文案/第2章取込_OPN_Cook_文案.md)。`### vaporwave との対置` 直後（L733 付近）。分割稿 [`第2章_命名の時代.md`](manuscript/第2章_命名の時代.md) 同期済。

---

### intro-kojiateki. 骨架的インタビュー挿話——「その頃のインターネットの雰囲気」

**背景（ユーザー指示・2026-06-19）**  
佐藤秀彦編『[新蒸気波要点ガイド](https://diskunion.net/dubooks/ct/detail/DUBK237)』（DU BOOKS、2019）所収の **骨架的**（Skeleton／骷、NY）インタビュー。骨架的は OPN・James Ferraro と並ぶ **proto-vaporwave** の作り手の一人。**文案・反映は未着手**——ユーザーが書籍で確認中（2026-06-19：**引用文は確認済み**）。

**インタビューの要点（書籍確認済み・引用可）**

| 問い | 骨架的の発言（確認済み） |
|---|---|
| **のちの影響**について、2010年になぜ vaporwave 的な技法（**サンプリング**と **chopped and screwed**）で音楽を作ろうとしたのか | 「**単純にその頃のインターネットにそういう雰囲気があった**」 |
| OPN『Chuck Person's Eccojams Vol.1』と**同時期**に出した **『Holograms』** を、当時どう位置づけていたか | 「**ポスト・チルウェイブ、エクスペリメンタル、あるいはスロウ・ジャムだと思って発表した**」 |

**文案前の残作業**：頁・段落番号の記録（脚注用）。『Holograms』表記・2010年の最小確認。

**本文での役割——第2章内の「挿話」**

- **問いを第2章の入口で立てる**：「その頃のインターネットの雰囲気」とは何だったのか  
- **三つのラベル**：骨架的自身の位置づけは chillwave だけでなく **（ポスト）チルウェイブ・エクスペリメンタル・スロウ・ジャム**——**チルウェイブ、エクスペリメンタルとのつながり**を第2章の叙述でも重要視する（OPN／Ferraro のノイズシーン離脱、mp3ブログの実験音楽、Post T.V. 等）  
- **答えは第2章のなかで部分的に開く**：chillwave／witch house／proto-vaporwave 各節が背景を伝えるが、**挿話時点では総括しない**（ユーザー方針：明かされるかどうかわからない）  
- **後付けの総称との差**：制作時点に vaporwave という語はなく、作り手は別ラベルで理解していた——「命名以前」「遡行的確定」（序文 L23）への伏線

**挿入位置（ユーザー方針・2026-06-19 更新）**

| 候補 | 判定 | 理由 |
|---|---|---|
| 序文 | **却下** | 草稿**全体を貫く問い**に見えてしまうが、本稿の主題ではない |
| B：`## vaporwaveという名前以前に`（L269）冒頭 | **却下** | その時点ですでに chillwave・witch house が出ており、**問いの答えの一部が先に書かれた状態**で問いを置く |
| **C（推奨）** | **第2章冒頭に新設 `##` 節** | `# 第2章　命名の時代`（L200）・時間軸（L202）の**直後**、`## 名前は冗談から生まれる`（L204）の**前** |

**推奨構成（案）**

```
# 第2章　命名の時代（2009〜2013年）
**時間軸：2009〜2013年**

## [新設] その頃のインターネットの雰囲気——骨架的の証言（仮題）
  （挿話 1〜2 段落。新蒸気波要点ガイドへの引用＋問いの提示）

## 名前は冗談から生まれる
  ### chillwaveとhypnagogic pop
  ...
```

**節の役割**：第2章全体の**入口フレーム**。以降の chillwave → witch house → proto-vaporwave は、この問いに**順次応答する材料**として読める（挿話本文で「以下で答える」とは書かない）。

**既出文献との住み分け**

| 既出 | 関係 |
|---|---|
| inv-piajp ☑／第3章 aesthetic 節 | 同書の**ばるぼら**年表・大辞典——**別箇所** |
| 編集方針 §2 | 新蒸気波要点ガイドは**日本語圏の記録として引用可** |

**手順（反映はユーザー承認後）**

1. 頁・段落を `docs/intro-kojiateki_引用メモ.md` に記録  
2. 文案 `第2章取込_骨架的挿話_文案.md`（**1〜2段落**。em dash 不使用）  
3. 新設 `##` 節タイトル（仮題）をユーザー承認 → 草稿・[`第2章_命名の時代.md`](manuscript/第2章_命名の時代.md) 同期  
4. 後続節への相互参照は**任意**——挿話単体で完結可

**ステータス**：☑ 草稿反映済（2026-06-22）。[`第2章取込_骨架的挿話_文案.md`](./archive/反映済み文案/第2章取込_骨架的挿話_文案.md)／[`docs/intro-kojiateki_引用メモ.md`](docs/intro-kojiateki_引用メモ.md)。**頁番号は要ユーザー確認**。

---

### src-3. r/witchhouse 参照——**完了（2026-06-17）**

☑ `#### コミュニティの正史` 末尾1文+URL。rev-9／src-6f と統合済。

### src-4. ハイパーポップの歴史——**完了**

☑ [`ハイパーポップの歴史.md`](notes/ハイパーポップの歴史.md) → `archive/反映済み文案/第2章取込_ハイパーポップ_文案.md` → 第2章 PC Music 節（2026-06-11 前後）。

### src-4b. ハイパーポップ追記——Spotify「Hyperpop」命名から brat summer まで

**背景**  
**src-4** ☑ は第2章 PC Music 節（2013–2016）のみ。第4章 [`## hyperpopの浮上`](./草稿.md)（L1013–1026）は第2章分岐の要約＋Spotify プレイリスト1文だが、**名称の由来**（2019年8月）から **brat summer**（2024）までの厚みが不足している。[`第2章取込_ハイパーポップ_文案.md`](./archive/反映済み文案/第2章取込_ハイパーポップ_文案.md) 執筆メモでも §7・§13 は「第4章へ保留」と明記済み。

**正本**：[`ハイパーポップの歴史.md`](notes/ハイパーポップの歴史.md) **§7–§13**（§1–6 は src-4 ☑ 済）

**射程（ユーザー指定：Spotify プレイリスト由来→brat summer）**

| 調査 § | 内容 | 草稿との関係 |
|---|---|---|
| **§7** | 2019年8月 Spotify「Hyperpop」プレイリスト創設——**ジャンル名のプラットフォーム命名** | L1025 1文を**拡張**（由来・日付・意義） |
| **§7** | 2019年11月 Cook が J Dilla・Kate Bush を追加→コミュニティ反発 | **ed-4 後記 L1246 と重複**。第4章＝叙述、後記＝制度化の痛み。住み分け表を文案に書く |
| **§8** | 2020–2021 第二波（SOPHIE 急逝 2021-01 等） | L1019 既述との**差分のみ** |
| **§12** | 2022–2023「hyperpop 終焉」言説（Dazed 等） | **1文可**。brat summer への橋渡し |
| **§13** | 2024 *brat*・brat green・Brat Generator・brat wall・「kamala IS brat」・Collins 今年の言葉 | **本タスクの上限**。視覚美学クロニクルとしての接続を明示 |

**射程外**（別節・別タスク・本書射程外）

| 調査 § | 理由 |
|---|---|
| §9 Dismiss Yourself／HexD | 第4章 `## Dismiss Yourself` 節で別途叙述済 |
| §10–11 Dariacore／Hyperflip | hyperpop 全史の射程外。必要なら別タスク |
| §14 YEAR0001／Drain Gang | 同上 |
| §15 Yabujin | Dismiss Yourself 節に言及済 |
| Cook×Charli 年表詳細 | src-4 文案で保留。brat 節で**最小限**触れる |

**章間の役割分担**

| 章 | 役割 |
|---|---|
| 第2章 | PC Music 草創・distroid 分岐（src-4 ☑） |
| **第4章** | hyperpop **浮上・命名・2024 brat summer**（**src-4b**） |
| 後記 ed-4 | Cook プレイリスト論争＝**制度化**の事例（既述。重複しない） |

**手順**

1. 草稿 L1013–1026・後記 L1246・調査ノート §7–§13 の**重複表**を文案執筆メモに書く  
2. 文案 `第4章取込_hyperpop_Spotify-bratsummer_文案.md`（**2〜4段落上限**。em dash 不使用）  
3. [`草稿.md`](./草稿.md) `## hyperpopの浮上` に反映 → [`第4章_爆発.md`](manuscript/第5章_爆発.md) 同期  
4. 推敲メモ・本ファイル更新  

**推敲メモ参照**：[`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 続8 E「hyperpopとインターネット美学の接続」——brat green／Brat Generator を**視覚美学**の例として1文足す余地あり。

**ステータス**：☑ 草稿・[`第5章_爆発.md`](manuscript/第5章_爆発.md) 反映済（2026-06-22）。

---

## CARI（cari-*）

調査（cari-inv）と草稿反映（cari-draft）を**分離**する。調査ノート §8 の未確認は cari-draft の必須条件ではない（断定を避ける書き方で対応済み）。

| ID | 内容 | 状態 | 成果物 |
|---|---|---|---|
| cari-inv | 調査 | ☑ | [`CARI_調査ノート.md`](notes/CARI_調査ノート.md)。2026-06-17 完了判定。§8 残3件は任意 |
| cari-draft | 草稿反映 | ☑ | `archive/反映済み文案/第5章取込_CARI_文案.md` → 第5章 L780–807 付近 |

### cari-inv. 調査——**完了（2026-06-17）**

☑ [`CARI_調査ノート.md`](notes/CARI_調査ノート.md)。§8 残3件（Collins URL・トレーラー照合・Terrell Davis）は**任意**。

### cari-draft. 草稿反映——**完了**

☑ `archive/反映済み文案/第5章取込_CARI_文案.md` → 第5章 L780–807 付近（Guardian・Facebook・Neo-Y2K）。

## フラクタル推敲（fractal-*）

正本：[`fractal-revision-guide/SKILL.md`](./fractal-revision-guide/SKILL.md)（併読：[`manuscript-style`](./.claude/skills/manuscript-style/SKILL.md)／[`docs/project-style-notes.md`](docs/project-style-notes.md)）

**目的**：[`草稿.md`](./草稿.md) を **文→段落→節→章** の順で推敲する。**crw-1**（認知リズム・削除中心）とは別。**構成調整**（非対称な段落分割、橋渡し、節末の射程整理）可。原意・事実は変えない。

**手順**

1. 章または節の区間を指定  
2. エージェントが fractal 基準で点検 → チャットに **A（段落分割等）／B（文レベル修正）** 一覧  
3. ユーザー指示（「A1–A4 反映」「B も適用」等）→ [`草稿.md`](./草稿.md) へ反映  
4. 当該章の文／段落が終わったら **節レベル**（橋渡し・密度波・一節一トピック）→ **章レベル**（章冒頭射程・章末まとめ・節間の流れ）  
5. 次章へ（fractal-2 …）

### fractal-1. 第1章——文／段落レベル（各節）

**ステータス**：☑ **完了**（2026-08-01）。第1章 L71–L369（`# 第2章` 直前）。

**進捗**（行番号は [`草稿.md`](./草稿.md) 現行版。反映のたびにずれる）

| 節 | 行（目安） | 状態 | 主な反映 |
|---|---|---|---|
| 序文 | L3–L69 | ☑ | L25 分割、L13 fairypage/Wiki 分割、L35 分割、L69 橋渡し |
| GeoCities | L75–L99 | ☑ | Tumblr 前史橋渡し、em-dash 除去、L91 述語修正、Ripps/OTBKA 分割 |
| mp3ブログ | L101–L121 | ☑ | 主語明示、Fluxblog 等分割、Altered Zones・著作権段落分割 |
| MySpace | L123–L145 | ☑ | 橋渡し、カスタム/HTML、事例3分割、年表/Doctorow 分割 |
| Tumblr | L147–L177 | ☑ | Karp 分割、reblog/photoset 分割、L157–159「〜という」重複解消 |
| フォークソノミー | L179–L206 | ☑ | Messina/年表/Nanoformats/vaporwave 分割 |
| ポストインターネット | L208–L294 | ☑ | A1–A6（Megazord/dump.fm/soft grunge 等分割）、B1–B3（Ripps 移動、日本語圏分割、「示している」） |
| James Bridle | L296–L311 | ☑ | A2 Sterling 分割（A1/A3/A4 は Reblorg 節と連続反映） |
| Reblorg | L313–L342 | ☑ | A1–A4 分割、B5–B7（まさしく削除、主語明示、限界段落分割）、arty corners 意訳 |
| アーキテクチャが開いた可能性 | L344–L368 | ☑ | A1–A3 段落分割、B1–B2（呼ばれる統一、スペース修正） |

### fractal-1-meta. 第1章——節レベル＋章レベル

**目的**：上記各節を通したうえで、第1章全体として読む。

**点検項目**（fractal §2–3）

- 節間の橋渡し（GeoCities→mp3→MySpace→Tumblr→フォークソノミー→ポストインターネット→Bridle→Reblorg→アーキテクチャ）  
- 章冒頭（L71）の射程と L368 章末までの一致  
- 密度の波（高密度節の連続が3段落以上続いていないか）  
- 節末 bridge の要否（Reblorg→アーキテクチャ、章末→第2章「雰囲気」）  
- 「アーキテクチャが開いた可能性の空間」節内の ### 2つ（タグ化…／土壌の位置づけ…）の役割分担と章末 thesis（L368–L370）→第2章冒頭への接続

**ステータス**：☐ **保留中**（§アクティブ・パイプラインと表記を統一。2026-08-13）。fractal-2〜4 を先行したため、第1章のみ節→章レベルが未実施という非対称が残っている。**8月末〆では切るか短縮版にするかが未決**（→ §クイックリファレンス「スコープ外の候補」）。

### fractal-2. 第2章——文／段落／節／章レベル（全12節）

**ステータス**：☑ **完了**（2026-08-07）。**fractal-1-meta を経由せず先行着手**（ユーザー指示）。ガイドラインの手順通り「上から2段落ずつ→節が変わったら節レベル→章が変わったら章レベル」で全12節を通し、さらにユーザー依頼により**段落レベル・節レベルを判定基準を厳しめにして再確認するパス**を追加で実施。

**進捗**（節単位。行番号は反映のたびにずれるため節見出しで管理）

| 節 | 状態 | 主な反映 |
|---|---|---|
| その頃のインターネットの雰囲気 | ☑ | 帰属情報の分割、重複表現の整理 |
| マイクロジャンルの見取り図 | ☑ | 主述ねじれ修正、主題の一意性分割 |
| ノイズシーンからの離脱——OPNとFerraro | ☑ | 同語重複解消、時系列の並べ替え |
| witch houseの音響的前史 | ☑ | 「暗いルート」節またぎ重複に前方参照、主語重複整理 |
| ダークな音のmp3ブログ——20jfg | ☑ | 助詞重複・表記スペース修正 |
| ブログからレーベルへ——Tri Angle | ☑ | 文末表現の反復解消 |
| MySpaceのネットワーク（旧題：MySpaceと20jfg） | ☑ | 見出し変更、括弧内注釈の分割、比較段落の並べ替え |
| GATEKEEPER『Giza』 | ☑ | 文末反復・主述不整合修正 |
| レーベルネットワーク——HIT、OESB | ☑ | 主部二重化解消、主語交代の分割 |
| ペルソナとHD視覚 | ☑ | 反復代名詞化、主述不整合修正 |
| Post T.V. | ☑ | まとめ反復統合、密度の高い段落分割 |
| アーキテクチャ：シーンを支えた条件 | ☑ | 3中見出しへ再構成、667/671行を密度で分割 |

**厳格再確認パス（段落・節レベル）で追加反映**：witch houseプロフィールの重複テーゼ削除、孤立1文段落の統合（4箇所）、節をまたいだ重複の前方参照化、第7節見出し再検討、アーキテクチャ節の3分割・非対称分割。詳細は git log（`claude/chapter-2-revision-7xq8sg` ブランチ、61219d7〜6364ca3）参照。

### fractal-3. 第3章——文／段落／節／章レベル

**ステータス**：☑ **完了**（2026-08-07）。文／段落レベル→章レベル確認まで完走。章レベル確認3件（`witch-house.com` 見出しの明確化／DMY Magazine 節の時系列逆行は再検討のうえ現状維持／seapunk 節への配分の偏りは節冒頭に前置き文を追加）。
**残1件**：`## アーキテクチャ：命名とプラットフォーム` 節のみ、08-07 のコミットに点検記録が見当たらない（第2章の同名節は推敲済）。**確定タスクで10分確認**（下記 §確定タスク）。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| vaporwaveという名前の登場 | ☑ | 動詞反復解消、二重帰属表現の整理 |
| 名前は冗談から生まれる——chillwave・hypnagogic pop | ☑ | 第2章との章またぎ重複を前方参照化（2件）、密度の高い段落を分割。**2026-08-19：inv-hypnagogic反映後に節そのものを新設・全面差替、憑在論節を本節直後に再配置・格上げ。上から4段落ずつ文体メモも参照して再推敲済**（帰属の曖昧さ1件、情報量のピーク分割5件、訳語1件、出典への誠実さ1件、語順1件＝計9件反映。時制の不統一は著者判断で現状維持） |
| witch house——命名と充填 | ☑ | 語の反復解消、段落間の空行欠落を2箇所修正、Rhinoceropolis段落を分割 |
| seapunk（`### 2011年6月1日のツイート`まで） | ☑ | 「夢の断片」反復解消。体言止め列挙＋「これらは」型の構文が3回目の出現（台帳記録・保留） |
| seapunk（`### Lil Internet と Lil Government の年表`以降） | ☑ | 年表〜レーベルと正史節の推敲、`witch-house.com` 見出しを明確化、節冒頭に記述配分の前置きを追加 |
| SuperSuper! Magazineという記録媒体 | ☑ | 節全体の推敲 |
| seapunkの死と遺産 | ☑ | 節の推敲、seapunk と vaporwave 節の推敲、三つの流れ節の結びで末尾2文の重複を統合 |
| 2012年7月12〜13日、DMY Magazine | ☑ | 節の推敲。時系列逆行は再検討のうえ**現状維持**（Adam Harper の伏線と構成上の山場を優先） |
| アーキテクチャ：命名とプラットフォーム | ☐ **要確認** | 08-07 のコミットに点検記録なし。10分確認で閉じる |

**台帳の申し送り**：全体の空行欠落パターン（段落間の空行が抜けている箇所）を機械チェックしたところ、第3章以外に第6章・第8章にも数箇所確認（原稿全体で計6箇所、うち第3章2箇所は反映済み）。該当章の推敲時に合わせて確認すること。

### fractal-4. 第4章——文／段落レベル（節ごと進行中）

**ステータス**：☑ **完了**（2026-08-12）。節ごとに文／段落レベルを点検・反映。章レベル点検も実施（リング構成を確認、節をまたいだ重複4件を解消）。合計25件の指摘（反映23件・保留2件）。詳細は下記進捗テーブルおよびgit log参照。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| 本章の視点：遡及的確定としてのlo-fi/HD区分 | ☑ | 「この文章自身」→「本稿自身」（用語統一） |
| proto-vaporwaveの音——EccojamsとFar Side Virtual | ☑ | 指摘なし（曲名列挙の密度候補は非対称性テストで保留） |
| Hito Steyerl「貧しいイメージの擁護」（### VVORKと「無言のキュレーション」含む） | ☑ | 誤植1件（余分なスペース）、文末表現の反復1件を修正 |
| **## distroid——充填されなかった名前**（全体） | ☑ | 節レベル点検完了（逆アウトライン一致・テーマ反復は意図的と判断、新規指摘なし） |
| ### Charlie Jones 記事と distroid の定義 | ☑ | 主題の一意性違反（は2回・逆接1文）を分割 |
| ### DIS Magazine と #HDBOYZ | ☑ | 主題の一意性（は3回）＋帰属の遅延を修正 |
| ### Gatekeeper『Exo』と HDIY | ☑ | 段落を3分割（一段落一トピック違反）、入れ子修飾の深さ・主題の一意性を解消、誤植2件（余分なスペース） |
| ### 命名の失敗と James Ferraro | ☑ | 主語交代の連鎖(3回)を分割。proto-vaporwave節との節またぎ重複(ほぼ逐語)を2箇所前方参照化 |
| ### 継承と conceptronica | ☑ | 主題の一意性（は2回）を分割。体言止め列挙+「こうした要素は」型構文が4回目出現（下記台帳参照、ユーザー判断で容認・記録のみ） |
| ### Gamsonite と DIS Magazine | ☑ | 主題の一意性（は2回）を分割。節レベル点検済（橋渡し良好） |
| ### SuperSuper! と人脈の形成 | ☑ | 密度分割+重複解消(Polly Salmon)、GFOTY名義の時系列を訂正（著者確認：2012年春以降）、主題の一意性+帰属主語の曖昧さ解消(Roy=A.G.Cook)、入れ子修飾(7要素)解消。節レベル点検済 |
| ### PC Music の設立と SOPHIE | ☑ | 主述のねじれ（運用は/Dazedが）を修正。密度候補（伝記的事実の連なり）は保留 |
| ### QT と Charli XCX | ☑ | 指摘なし |
| ### vaporwave との対置 | ☑ | 指摘なし。体言止め列挙+「この方向性は」型構文が5回目出現（記録のみ） |
| ### コラム：Daniel Lopatin と A. G. Cook（#### 5小節含む） | ☑ | 主題の一意性2件（は2回×2）を分割。密度候補多数は証拠列挙として保留。節レベル点検済 |
| ## deconstructed clubという並走（Night Slugs/Future Brown/Daniel Swan/IDLコラム含む） | ☑ | 密度ピーク文2件を分割（Daniel Swan段落、IDLモチーフ段落）、年号重複1件削除。節レベル点検済 |
| ## hyperpopの浮上 | ☑ | 節冒頭の重複は保留(道標文)、PC Music/SOPHIE再掲を圧縮（評価文は温存）、誤植1件（4回目）、vaporwave対置節との逐語重複を解消。節レベル点検済 |
| ## アーキテクチャ：lo-fiとHD | ☑ | 指摘なし。「遡及的確定として」節の冒頭との反復は意図的なリング構成と判断し無変更。章レベル点検済 |

**台帳（誤植パターン）**：句読点・鍵括弧直後に余分な半角スペースが入る誤植を3回確認（L1021「。 The Jogging」、旧L1047「さらに、 Tabor」、旧L1055「「HDIY」 はその」）。3回目に達したため、章の残りでも同型の誤植に注意する。

**台帳（構文パターン）**：体言止めで要素を列挙し、「こうした/これらは〜」の文で受ける構文。第3章seapunk節で3回目の出現を記録済み（保留）、第4章「### 継承とconceptronica」（L1069）で4回目出現。**ユーザー判断（2026-08-12）：書き手の署名的パターンとして容認。以後は修正せず、出現箇所の記録のみ続ける**。第5章L1221（Cluster Mag記事末尾）で追加出現を記録（記録のみ・修正なし）。

### fractal-5. 第5章——文／段落／節／章レベル

**ステータス**：☑ **完了**（2026-08-15）。全7節（本章が追う「逆転」とは何か／音楽ジャンルに添えられた「aesthetic」／批評の語彙になる「aesthetic」／ミームになる「aesthetic」全4サブ節／音と見た目が分かれる全3サブ節／逆転の中身全3サブ節／逆転が固まるまで全5サブ節）を文／段落→節→章レベルで点検・反映。章レベル点検で節をまたいだ重複1件を確認。19コミット。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| 本章が追う「逆転」とは何か | ☑ | 自己言及文の反復（「本章で見るのは」型が1節に3回）を2回に統合 |
| 音楽ジャンルに添えられた「aesthetic」 | ☑ | 誤植（余分な半角スペース）1件 |
| 批評の語彙になる「aesthetic」 | ☑ | 英語引用の形式統一＋簡潔な引用は訳を省略できる基準を新設、先行詞の明示（Rihanna）、密度分割2件、段落分割1件 |
| ミームになる「aesthetic」（YouTube／コメント欄／過剰な細分化／作品名とFrankJavCee） | ☑ | 密度分割4件、帰属の遅延1件、確信度の書き分け不整合1件（伝聞と断定の混在）、括弧の入れ子（3層）解消1件、第3章L733との事実不整合（日付精度・名義の前後関係）修正、主語交代の連鎖1件、段落分割1件 |
| 音と見た目が分かれる | ☑ | 章参照の明示（James Bridle→第1章）1件 |
| 逆転の中身 | ☑ | project-style-notes§2の禁止例「人は二つのものさしで見ていた」とほぼ同型の断定文を受け身化、一人称の意志表現1件、表記ゆれ（aesthetics→aesthetic）1件、体言止め断片の修正1件 |
| 逆転が固まるまで | ☑ | 誤植（「妥当かかどうか」等）、密度分割1件、英語引用の形式統一2件 |

**節をまたいだ重複（章レベル点検で発見）**：「### プラットフォームと速度のずれ」節末と「### 振り返り」節末尾がほぼ全面的に重複（画像/音の流通速度差の論証）。**ユーザー判断（2026-08-15）：現状維持**——振り返り節の要約機能として重複を許容。

**台帳（誤植パターン）**：余分な半角スペースの誤植を第5章で計3件確認（「これは 「vaporwave」 という」／「digital aesthetic 、 micro aesthetic」／「Aesthetic (internet) 」）。fractal-4に続きこのパターンが原稿全体で繰り返し出現している。

**台帳（英語引用）**：訳なし・半角引用符でない英語引用を5件発見・修正。うち1件は簡潔な引用として意図的に訳を省略（[`docs/文体メモ.md`](docs/文体メモ.md)§5に基準を新設）。同型の不整合は第4章L931・第7章L1630にも既存で確認済み（未修正・要フォロー）。

**運用ルールの更新（fractal-5で改訂）**：節レベル点検の逆アウトラインは、**段落単位ではなくトピック展開単位**で行う（段落内で話題が変わっていれば分割して要約し、論理的な繋がりを重視する）。下記セッション運用ルールに反映済み。

### fractal-6. 第6章——文／段落／節／章レベル

**ステータス**：☑ **完了**（2026-08-17）。全5節（ラベルが増えるとき——サフィックスと匿名のキュレーション全6サブ節／vaporwave の政治的受容全3サブ節／名付け親の分からない美学——dark academia と cottagecore全3サブ節／Tumblr NSFW BAN／2020年へ）を文／段落→節→章レベルで点検・反映。トピック展開単位の逆アウトラインで章レベル点検を実施、節をまたいだ重複は発見されず。13コミット。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| ラベルが増えるとき（サフィックスの生産性／normcore／態度からファッションへ／K-HOLEとDIS／Are.na／無言のキュレーション） | ☑ | 密度分割7件、誤植（余分な半角スペース・引用符前のスペース）3件、章参照の追加1件（Jon Rafman「9 Eyes」→第4章） |
| vaporwave の政治的受容（fashwave論争／コミュニティの応答／コラム：日本語圏での受容） | ☑ | 密度分割2件、誤植（読点直後の余分なスペース、日本語文字の前という稀なパターン）1件 |
| 名付け親の分からない美学（dark academia／cottagecore／Tumblrの内側で） | ☑ | 密度分割3件、ブロック引用の訳の欠落1件（Ryanの投稿、文体メモ§5準拠で引用符内に訳を追加、鍵括弧の列挙は読点区切りで統一） |
| Tumblr NSFW BAN | ☑ | 表記ゆれ1件（instagram→Instagram） |
| 2020年へ | ☑ | 指摘なし（章冒頭テーゼの意図的な回収と判断） |

**節をまたいだ重複**：発見されず。normcore・VVORKへの複数回言及はいずれも適切な圧縮参照。

**台帳（誤植パターン）**：余分な半角スペースの誤植を第6章で計3件確認（句読点前後・引用符前）。fractal-4〜5に続きこのパターンが原稿全体で繰り返し出現している。読点直後・日本語文字前のスペースという稀なパターン（本文全体で2箇所）も1件発見・修正。

**台帳（表記ゆれ）**：「instagram」表記が原稿全体で6箇所（うち第6章1箇所を今回修正）、「Instagram」表記が4箇所。project-style-notes §1のプラットフォーム名統一ルールに沿って、他章分は要フォロー。→ **fractal-7で解消**（第7章1箇所を修正。grep確認の結果、地の文の小文字表記は原稿全体で0件・残るのは全てURL内の`instagram.com`のみ）。

**台帳（章参照）**：VVORKへの複数回言及について、章参照（「第4章で見た」）を追加するかどうかユーザー判断を仰いだ結果、**追加しない**方針が確定（2026-08-17）。Jon Rafman「9 Eyes」には追加。既出概念の再言及に一律で章参照を求めるのではなく、文脈の自己完結性で個別判断する運用とする。

### fractal-7. 第7章——文／段落／節／章レベル

**ステータス**：☑ **完了**（2026-08-18）。全10節（liminal spaceの前史／世界がliminal化した／liminal spaceの爆発／liminal spaceの制度化とThe Backroomsとの関係／dreamcoreとweirdcore／cottagecoreの爆発／TikTokというアーキテクチャの転換／hyperpopのその後／Dismiss Yourself／アーキテクチャ：TikTokとDiscordという対照）を文／段落→節→章レベルで点検・反映。トピック展開単位の逆アウトラインで章レベル点検を実施、節をまたいだ重複は発見されず。15コミット。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| liminal spaceの前史（ストリートビューの視線／cursed imagesとTumblrチェーン／Twitter上のliminal space／The Backroomsと4chanスレッド／r/LiminalSpaceとReddit） | ☑ | 密度分割2件、帰属の遅延1件、コラム内の主語欠落1件、主語交代の連鎖1件（内容面：The Backroomsの匿名性＝返信の連鎖から生まれたことを明示）、論理の骨格の明確化1件（「フレーム」→「呼び名」） |
| 世界がliminal化した | ☑ | 密度分割1件（BBCの2つのデータを分離） |
| liminal spaceの爆発（2020年4月の拡散／Images with Elegiac Auras） | ☑ | 宙に浮いた主題の修正1件、同一フレーズの段落内反復の削除1件。動画年表の時制混在は著者判断で保留（リズムのための意図的表現） |
| liminal spaceの制度化とThe Backroomsとの関係（制度化のずれ／拡散の流れとメディアでの位置づけ／なぜ結びついたのか） | ☑ | 指摘なし（対句構文・確信度のヘッジ枠組みとも良好） |
| dreamcoreとweirdcore | ☑ | 指摘なし（軽微な密度候補1件は保留） |
| cottagecoreの爆発 | ☑ | 密度分割1件、主語のねじれ＋語の反復解消1件（dark academia段落） |
| TikTokというアーキテクチャの転換（Tumblrの回路を読み返す／2014 Tumblrリバイバル／-coreサフィックスの標準化） | ☑ | 密度分割1件（Twitter/Patreon移行とDiscordの位置づけ） |
| hyperpopのその後 | ☑ | 指摘なし |
| Dismiss Yourself：Discordが音楽コミュニティになる | ☑ | 節冒頭の橋渡し文の追加1件（hyperpop節→本節、TikTok/Discord対照の伏線）、主語の曖昧性の解消1件 |
| アーキテクチャ：TikTokとDiscordという対照 | ☑ | 主語交代の連鎖1件 |

**節をまたいだ重複**：発見されず。DavidCrypt・Solar Sands・cottagecore/dark academia・images/pictures/places混在の話への複数回言及はいずれも「前節で見たように」等の明示的な前方参照で適切に処理済み。

**台帳（誤植パターン）**：プラットフォーム名の小文字表記（reddit/tiktok/wikipedia/youtube/instagram/tumblr）を第7章で計8箇所修正。fractal-6のinstagram表記ゆれ指摘（原稿全体に残存・要フォロー）を含め、他章分は未フォロー。余分な半角スペースを6件確認・修正（fractal-4〜6に続き頻出パターン）。

**運用面の所見**：本章は史実の年表的記述が多く、短文の語尾が「〜た。」で連続する箇所や動画年表内の時制混在（現在形／ている形／過去形が混在）が複数見つかったが、いずれも**著者判断でリズムのための意図的な表現**として保留された。文レベルの機械的な規範違反だけでなく、リズムの意図を確認してから判断する運用が有効だった。次章以降も同型の指摘は「候補として提示→著者に意図を確認」の手順を踏む。

### fractal-8. 第8章＋後記——文／段落／節／章レベル

**ステータス**：☑ **完了**（2026-08-18）。全11節（Frutiger Aeroという問い／CARIの起源：建築家の個人アーカイブ／McBling と Frutiger Aero：命名という行為／CARI設立とプラットフォームの意味／FairyPageとAesthetics Wiki／Discordが承認プロセスになる／Neocities：対位法として／「分類する欲望」そのものが美学になった／クロニクルの終わりにあたって〈十年後にどう見えるか、という問い／物語ることの偏り〉）を文／段落→節→章レベルで点検・反映。**これでfractal-1〜8、全8章の主線パイプラインが完走**。15コミット。

**進捗**

| 節 | 状態 | 主な反映 |
|---|---|---|
| Frutiger Aeroという問い（章導入含む） | ☑ | 論理矛盾の修正1件（「Aero」＝Vista一製品の名 vs 時代全体を束ねるラベルの不在）、内容に踏み込んだ議論1件（章冒頭「あの感じ」自体が遡行的確定の産物であることの自己言及を「遡行的確定」定義パラグラフに追加。ユーザー提起の論点をめぐる複数往復の検討を経て反映） |
| CARIの起源：建築家の個人アーカイブ（Evan Collins と Y2K Aesthetic Institute／The Guardian と Neo-Y2K／系譜の重なり） | ☑ | 「さらに」の連続使用1件、情報量のピーク分割2件（Priz Tats/DIS Magazine、Valeris Mediaのshowreel） |
| McBling と Frutiger Aero：命名という行為 | ☑ | ブロック引用の訳追加1件、綴りの不一致修正1件（Subprime Morgage→Mortgage）、主語の明示1件 |
| CARI設立とプラットフォームの意味（命名する意志／Facebook から Discord へ／視覚資料の基盤としてのAre.na） | ☑ | facebook/discord表記統一6箇所、余分な半角スペース1件、誤字2件（確定タスク#1相当：2016年の重複、「理由にある」→「理由である」）。前方参照（第4章VVORK・第6章Are.na）を確認、正確 |
| FairyPageとAesthetics Wiki（設立と成長／FairyPageの失望と追放） | ☑ | 英語スローガンへの訳追加1件、情報量のピーク分割1件、主語の明示1件（一次資料`notes/aesthetic wiki 歴史レポート.md`で事実確認のうえ反映） |
| Discordが承認プロセスになる | ☑ | 段落削除1件（Dismiss Yourselfへの唐突な言及、文脈接続が弱く本題から外れていたため）、盗用の主体の明確化1件（一次資料`notes/CARIの歴史.md`確認・方向は記載なく著者の理解に基づき反映）、態の変化による読みにくさの分割1件 |
| Neocities：対位法として | ☑ | 節見出し変更1件（「IndieWebとNeocities」→「Neocities」、本文にIndieWeb記述がないため）、引用の訳追加1件、章をまたいだ重複の解消1件（第7章TikTok節とほぼ逐語一致の一文に前方参照を追加） |
| 「分類する欲望」そのものが美学になった | ☑ | 指摘なし（章の理論的結論として完成度が高いと判断） |
| クロニクルの終わりにあたって（十年後にどう見えるか、という問い／物語ることの偏り） | ☑ | 節見出し変更1件（「語り直すために、アーカイブが要る」→「物語ることの偏り」、結論を先取りしない見出しへ。ポエミーな見出しを避ける方針を確認）。前方参照多数（第1・2・4章）を確認、いずれも正確 |

**節をまたいだ重複**：第7章「TikTokというアーキテクチャの転換」節との1件（Tumblr NSFW BAN以降の移行先の記述、ほぼ逐語一致）を発見し前方参照を追加。他は発見されず。

**内容にかかわる議論（推敲の範囲を超える判断）**：本章では通常の文体上の指摘に加え、①章冒頭の描写自体が「遡行的確定」の実例であることの自己言及、②盗用の主体（Aesthetics WikiがCARIを盗用）の一次資料確認、③FairyPage関連の主語補完の事実確認——など、内容の正確性・論理構造にかかわる指摘が複数あり、いずれもリポジトリ内一次資料の確認や著者との複数往復の検討を経て反映した。

**未解決として記録した課題**：「Neocities：対位法として」節は本来IndieWebとの対位法だった可能性があるが、実際の本文はNeocitiesのみ。調査ノート[`notes/インディーウェブの歴史年表.md`](../notes/インディーウェブの歴史年表.md)を使ってIndieWeb段落を書き起こすかどうかは筆者判断（新規執筆のため今回は見出し変更のみの応急対応。上記「明晰さレビュー」節に記録）。

**運用面の所見**：第8章は制度化の経緯という性質上、命名・組織化・プラットフォーム移行の記述が多く、事実関係の正確性が特に重要だった。主語の曖昧な箇所や内容解釈にかかわる指摘では、リポジトリ内の一次資料ノート（`notes/CARIの歴史.md`、`notes/aesthetic wiki 歴史レポート.md`）を確認してから文案を出す手順が有効だった。見出し変更（IndieWeb節、後記節）はいずれも著者と複数の案を出し合って決定しており、「文案を1つ出して終わり」ではなく「方向性を相談してから絞り込む」という進め方が特に後記の見出しで効いた。

### fractal-6 以降

| ID | 章 | 行（目安） | 状態 |
|---|---|---|---|
| **fractal-6** | 第6章　名前があとから来る | — | ☑ 2026-08-17 |
| **fractal-7** | 第7章　爆発 | — | ☑ 2026-08-18 |
| **fractal-8** | 第8章＋後記 | — | ☑ 2026-08-18 |

各章は **fractal-1 と同型**（文／段落→節→章）で進める。章 ID は着手時に行番号を更新する。

### セッション運用ルール（fractal-4で確立、fractal-5で逆アウトラインの粒度を改訂。fractal-6〜8も同じ手順で進める）

**粒度**：上から2段落ずつ、文＋段落レベルを点検（ガイド6-1通り）。**節が変わったら、その節の節レベル点検を明示的に行い、結果を報告する**（問題がなくても分析内容を書く）。節レベル点検では以下を必ず当てる：

- 道標の設置／問いの単一性／段落配列の必然性（ガイド§4の既存項目）
- **逆アウトライン分析**（fractal-5で改訂：**段落単位ではなくトピック展開単位**で要約する。段落内で話題が変わっていれば分割し、論理的な繋がり〈飛躍がないか〉を重視する）
- **語句・構文の重複**（節内・直近節との重複表現、体言止め列挙や「〜こと自体が〜」型など反復しやすい構文の有無）

章が変わったら章レベル点検（逆アウトライン一致・節をまたいだ重複・文体装置の反復・主題の通し確認・確信度の一貫性・再訪可能性）も同様に明示する。

**文レベル**は規範9項目を毎回一通り当てる：語順／主題の一意性／情報量のピーク／主語交代の連鎖／修辞と事実の優先順位／簡潔性／主題直前の入れ子修飾の深さ／文末表現の反復／帰属の遅延。

**報告フォーマット**：指摘は通し番号（①②③…）を振り、各指摘に

- **該当箇所**（引用）
- **抵触する規範**
- **文案**
- **理由**（指摘・文案それぞれに）

を明示する。ユーザーは番号で指示できる（例：「①は反映、②は保留」）。

**反映・コミットの原則**：**提案は必ずユーザーの確認を取ってから実行**する。確認なしに自分の判断で反映・コミットしない。文案が立てにくい項目（トレードオフがある・機械的に直せない・著者の意図確認が必要）は、文案を押し付けず方針を伺う。

**密度候補の扱い**：絶対閾値（固有名詞・年代・数値5要素以上）超過の候補には非対称性テストを適用する。分割しても両側とも中密度にしかならない場合（列挙構文、人名・曲名リスト、伝記的事実の羅列など）は保留し、その旨を一言報告する（逐一詳細を書かず、まとめて触れる程度でよい）。

**台帳**：同型の誤植・構文パターンは都度記録し、3回目の出現で意識に上げる（fractal-4では半角スペース混入の誤植が3回出現）。

**文案作成時の注意**：新しく文を書く・書き換える際は[`docs/文体メモ.md`](docs/文体メモ.md)・[`docs/project-style-notes.md`](docs/project-style-notes.md)の禁止事項も確認する（例：em-dash「——」は本文で使わない。fractal-4で誤って使用し、指摘を受けて修正した実例あり）。

---

## 認知リズム推敲（crw-*）

正本：[`cognitive-rhythm-writing/SKILL.md`](./cognitive-rhythm-writing/SKILL.md)

### crw-1. 草稿全体——認知リズム推敲

**目的**：[`草稿.md`](./草稿.md) 全文を区間ごとに点検し、文書更新（進行予告・執筆宣言・駄文）を削除、必要箇所のみニュアンス修正する。**構成変更（文の入れ替え・段落分割・節の追加）は行わない**。

**手順**

1. ユーザーが区間を指定（例：`L20–L58`、または章単位）  
2. エージェントが **話題テスト**（状況更新 vs 文書更新）で削除候補・言い換え案を**チャット**に提示  
3. ユーザー承認 → [`草稿.md`](./草稿.md) へ反映 → 必要なら [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) にログ  
4. 次区間へ。fact 追加・調査は**別タスク**（inv-*／cons-*）と混同しない  

**進捗**（行番号は [`草稿.md`](./草稿.md) 現行版。反映のたびにずれる場合あり）

| 区間 | 行 | 状態 | メモ |
|---|---|---|---|
| 序文（全体） | L1–L58 | ☑ 反映済 | 2026-07-23。「インターネット美学とは何か」〜「充填、フォークソノミー、横断性」 |
| 第1章 GeoCities | L63–L82 | ☑ 反映済 | 同上バッチ（L59–L156） |
| 第1章 mp3ブログ | L83–L96 | ☑ 反映済 | 同上 |
| 第1章 MySpace | L97–L110 | ☑ 反映済 | 同上 |
| 第1章 Tumblr | L111–L136 | ☑ 反映済 | 同上 |
| 第1章 フォークソノミー | L137–L156 | ☑ 反映済 | 同上。L154 `#vaporwave` 例まで |
| 第1章 ポストインターネット〜章末 | L158–L277 | ☑ 検討済（crw） | 2026-07-27。**fractal-1 ☑**（2026-08-01）で文／段落反映済 |
| 第2章 | L279–L511 | ☑ 検討済 | 2026-07-27。シーン〜第3章橋（vaporwave 冒頭まで） |
| 第3章 | L513–L787 | ☑ 検討済 | 2026-07-27。命名の時代〜`## アーキテクチャ：命名とプラットフォーム` |
| 第4章 | L789–L1000 | ☑ 検討済 | 2026-07-27。lo-fi/HD〜`### 遡及的確定として`（L1003 第5章直前） |
| 第5章 | L1003–L1188 | ☑ 検討済 | `# 第5章 aesthetic` 〜 `# 第6章` 直前（2026-07-24） |
| 第6章 | L1189–L1340 | ☑ 検討済 | normcore〜Tumblr BAN〜2020年へ（2026-07-24） |
| 第7章 | L1342–L1624 | ☑ 検討済 | liminal 前史〜TikTok/Discord 対照（2026-07-24） |
| 第8章 | L1628–L1808 | ☑ 検討済 | CARI〜Neocities〜分類する欲望（2026-07-24） |
| クロニクル末・後記 | L1811–L1843 | ☑ 検討済 | 2026-07-24 |

**ステータス**：☑ **クローズ**（2026-08-13）。区間点検は2026-07-24に完了・一時停止。L1–L156 のみ反映済、L158–L1843 は検討済で**反映は筆者判断**として凍結。その後 **fractal-1〜4 が別線で全章を文／段落レベルまで通しており、fractal-5〜8 で残りも通る**ため、crw-1 として再開する必要はない。未反映提案は再押ししない。

---

### ban-cons-1. Tumblr NSFW BAN——章間一貫性修正

**背景（2026-07-27 確定）**：[`草稿.md`](./草稿.md) **`## Tumblr NSFW BAN`**（L1320–1340 付近）を改稿。移行先は Twitter／Patreon 優先、Discord は公開型とは別のサーバー型の**ひとつ**。CNBC の日次投稿数（2014 8400万→2018 3000万）は **ban 以前からの長期衰退**として L1338 に分離。30% トラフィック減は [Mashable](https://mashable.com/article/tumblr-lost-a-third-of-its-users-after-porn-ban)（ban 後）。

**目的**：上記基準と矛盾する後方記述・分割稿・年表ノートを揃える。**crw-1 とは別**（ここはファクト／因果の整合。入れ替え・段落分割可）。

**優先修正箇所**（grep 起点）

| 優先 | 草稿位置 | 問題 | 改稿方針 | 状態 |
|---|---|---|---|---|
| A | L1576（`### Tumblr の回路を読み返す`） | ban 直後に Discord・**TikTok** へ移ったと読める | TikTok は **2020 年**、Discord 急成長も **2020 年 COVID**（L1606）。ban 後の移行は Twitter／Patreon（L1330） | ☑ |
| B | L1789（Neocities 節） | 「流出は Discord へ移行した」と断定 | L1330 に合わせ分散移行。Neocities は ban 直接因果を弱め「同型の回帰」 | ☑ |
| C | L1330 | `instagram` 表記 | `Instagram`（project-style-notes） | 任意 |
| D | L1330 | 移行先の出典 | [CNBC 2018-12-21](https://www.cnbc.com/2018/12/21/tumblrs-adult-content-ban-pushes-power-users-to-twitter-patreon.html) リンク追加を検討 | 任意 |
| E | 分割稿 | `第4章_感情が先に来る.md` L101–103 | 旧叙述（TIME 30%・投稿数・Discord「多くが」）が残存 |
| F | 年表 | `tumblrタイムライン.md` L285–290、`timeline.md` L467 | Dec 17 節に CNBC 投稿数と 30% 減が混在。L1338 基準で整理 |

**手順**

1. ~~[`草稿.md`](./草稿.md) L1320–1340 を**正本**として grep~~ ☑ 2026-07-24  
2. ~~上表 A→B~~ ☑ 2026-07-24（C・D は任意）  
3. E・F を同期（**cons-2** 還流と合流可）  
4. [`docs/草稿_整合性レビュー.md`](docs/草稿_整合性レビュー.md) 8-7（Neocities）行を ban-cons-1 完了で ☑（草稿正本確認済）

**ステータス**：☑ **草稿正本確認済**（2026-07-24）。L1320–1340・L1576・L1789 整合。他章の Discord 言及は 2020 年 CARI／Wiki／Dismiss Yourself 文脈で矛盾なし。

**grep 結果（草稿.md・2026-07-24）**

| 箇所 | 判定 |
|---|---|
| L1320–L1340 `## Tumblr NSFW BAN` | ☑ 正本。Twitter/Patreon 優先、Discord はひとつ、CNBC＝2014→2018 長期衰退 |
| L1576 `### Tumblr の回路を読み返す` | ☑ L1330 と同型。TikTok＝2020 可視化と分離 |
| L1789 Neocities 節 | ☑ 同上＋Neocities を「ひとつ」 |
| L1716・L1766・L1604 等 Discord | ☑ ban 後**流出**ではなく 2020 制度化／音楽コミュニティ（別層） |
| L1817 クロニクル末「Discordが…」 | ☑ 2020 分類・保存の要約（ban 移行ではない） |

**残（cons-2／任意）**

| 優先 | 対象 | 内容 |
|---|---|---|
| C | 草稿 L1330 | `instagram` → `Instagram` |
| D | 草稿 L1330 | CNBC 2018-12-21 移行先記事リンク追加を検討 |
| E | 分割稿・文案 | `第7章_reorg_文案.md` L246 等——旧「discord サーバー＋TikTok へ移行」 |
| F | `tumblrタイムライン.md` L285–290 | 30% 減（ban 後）と 8400万→3000万（長期衰退）が同段落に混在 |

---

## 編集方針由来（ed-*）

正本：[`docs/編集方針.md`](docs/編集方針.md)

| ID | 編集方針 | 対応タスク | 状態 | 行先 |
|---|---|---|---|---|
| ed-1 | §1 政治化（コミュニティの応答） | **rev-7** と同一 | ☑ | 第2章 DMY 節 L426–452（英語圏＋受容の橋。2026-06-02） |
| ed-2 | §2 日本語圏は射程外 | 単独 | ☑ | 序文 L13 直後（2026-06-11） |
| ed-3 | §3 seapunk 読み道整備 | 単独 | ☑ | 第2章 seapunk L451–734 ほか。下記 ed-3 節 |
| ed-4 | §4 本稿の制度化への寄与（メタ自己言及） | 単独 | ☑ | `## ＜後記＞` L1028 直後（2026-06-11） |
| ed-5 | r/AestheticWiki 制度化追記 | 単独 | ☑ | 第5章「分類する欲望」節 L1109 付近（2026-06-17） |
| ed-6 | 序文——「インターネット美学」と「制度化」の説明節 | 単独 | ☑ | 序文に新設節「「インターネット美学」という言葉の来歴」として反映（2026-07-01）。下記詳細節 |

**優先度（編集方針記載順）**：ed-1 → ed-2 → **ed-6** → **ed-7** ☑ → ed-3 → ed-4 → ed-5。

### ed-3. seapunk 読み道整備——**完了（2026-06-22）**

**方針**：見出し整理・追加（**A/B/C/D**）＋節頭地図1段落。**文案不要**。見出しは草稿直接編集可。**圧縮はしない**（編集方針 §3 は別件）。

| Phase | 内容 | 状態 |
|---|---|---|
| 1 | 見出し B/C/D（年表 `###`×3、`## 三つの流れ` 昇格、SuperSuper `###`×4、レーベルと正史 `###`×3、seapunkの死 `####`×4 等） | ☑ |
| 2 | 節頭地図1段落（A・`## 2011年6月1日のツイート` 内・引用ブロック後） | ☑ |
| 3 | 分割稿同期（[`第2章_命名の時代.md`](manuscript/第2章_命名の時代.md) 等） | — **任意** |

**同日・草稿のみ**（ed-3 範囲外だが読み道整備として実施）：序文 `###`×5、DMY／distroid／PC Music／deconstructed club／アーキテクチャ総括、第5章 TikTok・CARI 等の `###` 分割。

**ステータス**：☑ 草稿上の seapunk 読み道整備は**完了見込み**。分割稿は未同期のまま可。

---

### ed-4. 本稿の制度化——**完了（2026-06-11）**

☑ [`後記取込_制度化ループ_文案.md`](./archive/反映済み文案/後記取込_制度化ループ_文案.md) → `## ＜後記＞` L1028 直後。concl-1 との住み分け：クロニクル＝外向き／後記＝内向き（Cook 歴史化・著者の不确定性）。

### ed-6. 序文——「インターネット美学」と「制度化」の説明節

**背景（ユーザー指示・2026-06-17）**  
草稿は序文 L9・第5章題で「**制度化**」を使うが、読者向けの定義節がない。同様に「**インターネット美学**」カテゴリの来歴も序盤で説明されていない。序盤に説明節を設けたい。

**調査の結論（暫定）**  
[`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) に整理済。

| 論点 | 要点 |
|---|---|
| **語の二層** | 「internet aesthetic」は古く口語的（古いネットの質感・比喩）に使われていた。今日的カテゴリ用法は **2016〜2018** 頃から（Twitter 所感）、**2019〜2020** に定着 |
| **2020** | [Washington Post cottagecore 記事](https://web.archive.org/web/20200911061944/https://www.washingtonpost.com/lifestyle/travel/how-the-cottagecore-internet-aesthetic-dovetails-with-pandemic-travel/2020/09/10/3ae54032-ed39-11ea-99a1-71343d03bc29_story.html) 等——大手メディアでの今日的用法の初期例 |
| **2022＝制度化** | Aesthetics Wiki **Category:Internet Aesthetics**（2022-06-29）、英語 Wikipedia 草稿（2022-08-05） |
| **Wikipedia** | 立項＝特筆性の関門。**英語**：AfD 脱落→2025 復帰（[Internet aesthetic](https://en.wikipedia.org/wiki/Internet_aesthetic)）。**日本語**：[インターネット・エスセティック](https://ja.wikipedia.org/wiki/%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%BC%E3%83%8D%E3%83%83%E3%83%88%E3%83%BB%E3%82%A8%E3%82%B9%E3%82%BB%E3%83%86%E3%82%A3%E3%83%83%E3%82%AF) **2023-10-11** 英訳立項 |
| **EBSCO** | [Research Starters: Internet aesthetic](https://www.ebsco.com/research-starters/social-sciences-and-humanities/internet-aesthetic)（**2025**・図書館リファレンス）。§7.5 |

**他タスクとの住み分け**

| 既出 | ed-6 で書くこと | 書かないこと |
|---|---|---|
| 序文 L19〜29（aesthetic 語史） | **internet aesthetic** カテゴリ語の来歴・2020/2022 | aesthetic 哲学史の再掲 |
| 序文 L9（制度化の予告） | **制度化**の本稿内定義＋Wikipedia 例 | 第5章 CARI の詳細 |
| **ed-2**（日本語圏射程外） | 英語圏語史が主 | 日本語圏受容史 |
| 第5章 | 伏線のみ | Wiki・Discord の実務 |
| **meta-3**（遡行的確定） | Wikipedia 定義＝過去の整理、と1文触れてもよい | 後記の自己言及の本体 |

**挿入位置（推奨）**

序文 **L9 直後**（「CARIやAesthetics Wikiによる制度化」の直後）に新設 `### インターネット美学と制度化`（または `####`）。L11「各章はプラットフォームの…」の前。

**分量・トーン**

- **2〜3段落**上限
- 年表の羅列ではなく：**今日のカテゴリ語**／**語の古い用法との違い**／**制度化（本稿の意味＋Wikipedia 例）**の3点
- HBR 2013 は口語用法の1例として短く；Washington Post 2020 と Wiki/Wikipedia 2022 が主役

**手順**

1. 調査ノート §9 チェックリストに沿って `序文取込_ed6_インターネット美学と制度化_文案.md` を作成  
2. ユーザー承認 → [`草稿.md`](./草稿.md) 序文に反映  
3. [`第1章_土壌.md`](manuscript/第1章_土壌.md) 等の分割稿は序文があれば同期要否を判断  
4. 本ファイル・[`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 更新  

**正本**：[`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md)

**ステータス**：☑ 完了（2026-07-01）。序文に独立節「### 「インターネット美学」という言葉の来歴」として反映（口語用法との層の違い→2020 Washington Post→2022制度化→Wikipedia AfD/日本語版→EBSCO）。文案は`archive/反映済み文案/序文取込_ed6meta1_文案.md`。あわせて序文冒頭に新設節「### 「インターネット美学」とは何か」（日本語版Wikipedia・アニヲタWiki・美学ウィキの3定義踏査、美学／美学ミーム／インターネット美学の用語3層整理）を追加し、旧「### aesthetic という語」節は第5章と重複するため削除。「### アーキテクチャと各章」の章番号ずれ（第2〜7章の言及が実際の章立てと1つずつずれていた）も修正。

**後続**：~~ed-6 で穴埋めした結果、序文が長くなり入口が重い——**ed-7**（圧縮・再構成）で対応。~~ → **ed-7** ☑（2026-08）

### ed-7. 序文の圧縮・読者向け再構成

**背景（ユーザー指摘・2026-08）**  
ed-6・meta-1 反映後、序文が長く入口が重い——**削る／移す／統合する**（新情報の追加はしない）。

**草稿反映メモ（2026-08・ユーザー判断で一区切り）**

| 項目 | 結果 |
|---|---|
| **構成** | 6 `###` → **3 `###`**（L3–L41）：「インターネット美学」とは何か／充填・フォークソノミー・横断性／系譜の空白と本稿の射程 |
| **削除** | `### 制度化`（定義は第5章 `## 逆転が固まるまで` 初出）、`### 「インターネット美学」という言葉の来歴`、`### アーキテクチャと各章`（章概観・ed-2 射程文） |
| **充填節** | 短縮（Frutiger Aero＋フォークソノミー2段落。横断性の独立段落は統合） |
| **末尾** | 執筆動機ツイート2件 → 問い3つ → 第1章への繋ぎ文 |
| **任意・未実施** | 分割稿 [`manuscript/序文_改稿.md`](manuscript/序文_改稿.md) 同期／**fractal-1-meta** 序文パス／節名「系譜の空白と本稿の射程」の見直し |

**ステータス**：☑ 完了（2026-08）。計画時の「半分・1500字」目安は未厳密計測。**こんなもんでよい**——ユーザー判断。

---

## 章再編・aesthetic 節（aesthetic-reorg-* / aesthetic-rev-*）——**完了（2026-06-22）**

reorg-0/1/2 ☑／aesthetic-rev-1 ☑（草稿 L687–870）／aesthetic-rev-2 ☑／ch3-ch6-balance ☑。ed-6 △（L14・L38・L22 反映済。任意：L11/L22 signpost）。

| 正本 | 内容 |
|---|---|
| [`docs/第2章_aesthetic章分離_考察.md`](docs/第2章_aesthetic章分離_考察.md) | reorg 考察 |
| [`docs/第3章_aesthetic_rev1_考察.md`](docs/第3章_aesthetic_rev1_考察.md) | rev-1 考察・§21 プラン |
| [`aesthetic_文法分析メモ.md`](notes/aesthetic_文法分析メモ.md) | 文法分析 |
| [`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) | 制度化調査 |
| [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) | reorg/rev ログ（2026-06-19–22） |

分割稿 [`第3章_aestheticという語.md`](manuscript/第3章_aestheticという語.md) は**手動同期（ユーザー）**。

## 匿名キュレーション・normcore・Are.na（inv-khole-* / inv-cari-arena）

**背景（2026-06-19 開始、2026-06-26 計画確定）**  
[`khole-arena-archillect-researtch.md`](notes/khole-arena-archillect-researtch.md) は、K-HOLE／Are.na／Archillect／VVORK／rare.jpg 等の**画像キュレーション・ポストインターネット圏**をまとめた調査。aesthetic 節の reorg／rev とは**独立したパイプライン**。

2026-06-26 の検討で、挿入位置が確定し、normcore／サフィックス／Are.na の第6章挿入計画と、画像bot（VVORK / Archillect / rare.jpg）の章別分担計画が文書化された。CARI–Are.na 調査を先行させ、その結果を踏まえて文案を作成する順序とした。

**調査ノートの主要ブロックと確定した行先**

| ブロック | 内容 | 行先（確定） | 計画ファイル |
|---|---|---|---|
| **VVORK** | 無言のキュレーション、DIS と同一シーン | **第4章** DIS 節延長（L733〜L762） | [`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md) |
| **K-HOLE／normcore／Are.na** | サフィックス生産性、normcore 充填、K-HOLE→DIS→Are.na 接続 | **第6章** 冒頭挿入（L1075 後） | [`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md) |
| **Archillect／rare.jpg** | VVORK の Twitter 移植、著者性の消去 | **第6章** normcore 挿入の近くで短く言及 | [`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md) |
| **CARI の Are.na 活用** | プラットフォーム論の補完 | **第8章** L1484〜（inv-cari-arena ☑。**実行可能**） | [`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md)＋[`Arena設計思想調査ノート.md`](notes/Arena設計思想調査ノート.md) |
| **Giolo & Berghman** | aggregation＝internet aesthetics | 第6章 or 第8章に1文で引用可。単独の節は不要 | — |
| **§11 日本語圏** | カオスラウンジ、パクツイ等 | **射程外**（ed-2）。本文に入れない | — |

---

### inv-khole-0. 挿入位置の測定 ☑

**ステータス**：☑ 完了（2026-06-26）。計画ファイル2件が成果物を代替。

**成果物**：
- [`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md)：normcore＋サフィックス＋Are.na の挿入計画。調査状況総括表・未調査セクション付き
- [`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md)：VVORK / Archillect / rare.jpg の章別分担計画

**確定事項**：
- 第4章に VVORK を仕込み（DIS 節延長・1段落）、第6章で Archillect/rare.jpg を軽く回収（1〜2文）
- 第6章冒頭に normcore＋サフィックス＋K-HOLE→DIS→Are.na 接続を挿入
- Are.na→CARI は**「プラットフォーム共有＋設計思想の構造的親和」**として書く（inv-cari-arena ☑ で確定）
- 第8章 CARI 節への Are.na 追記は**実行可能**（三段階知識生産フローが新材料）

---

### inv-cari-arena. CARI の Are.na 活用——追加調査——**完了（2026-06-27）**

☑ [`Arena設計思想調査ノート.md`](notes/Arena設計思想調査ノート.md)（全11節）。一次資料ベースで Are.na 設計思想・CARI との関係・Discord 構造を整理。

**調査結果の要点**

| 目的 | 結論 |
|---|---|
| CARI が Are.na を**なぜ・どう**使うか | ☑ 確定。Collins「CARI work is based here on Are.na」。各 aesthetic に対応チャンネル。初期アイデア出し・協働研究の場 |
| Are.na を**いつ**使い始めたか | ▲ 正確な開始時期の一次資料なし。文案で断定を避ける書き方で対処可 |
| K-HOLE との**人脈的直接接点** | ☑ 確定：**なし**。Broskoski が Collins を「最もおもしろいアカウント」と名指し（Upstatement インタビュー）するが、K-HOLE メンバーとの直接接点ではなく「ユーザーとしての注目」 |
| 「人脈線」か「プラットフォーム共有」か | ☑ **プラットフォーム共有＋設計思想の構造的親和**。K-HOLE メンバーが共同創設した Are.na を CARI が研究基盤として活用 |

**新知見**（計画への影響）

- **三段階知識生産フロー**：Discord（議論・命名投票）→ Are.na（視覚コーパス保存）→ cari.institute（確定テキスト公開）。第8章プラットフォーム論の新材料
- **Are.na の設計哲学**：広告なし・アルゴリズムなし・「考えるための道具」。CARI の研究倫理との整合（§7 の4点）
- **Discord の Maintenance Effort**（2021–2024）：チャンネル説明文 → Website への知識生産フロー
- **「いいね」不在の設計史**：創設（2014）から一貫。思想的選択

**後続タスクへの影響**

| ID | 影響 |
|---|---|
| **inv-khole-1a** | 影響なし。着手可能 |
| **inv-khole-1b** | Are.na→CARI の書き方確定。Are.na の設計哲学を1文で特徴づけ可。未調査C ☑（サフィックス系譜比較調査ノート）。**着手可能** |
| **inv-khole-1c** | **実行可能**と判断。三段階フロー＋プラットフォーム分担表が第8章の新記述材料 |

---

### inv-khole-1a. 文案：第4章 VVORK 段落

**前提**：inv-cari-arena ☑。**着手可能**。

**内容**：Steyerl 節直後・distroid 直前に `### VVORK と「無言のキュレーション」`（6段落）を挿入。VVORK「無言のキュレーション」＋ギャラリー形式借用。DIS との形式対比。2010 MULTIPLEX 人脈（Dena Yago／Broskoski／Zucconi）。The Jogging 形式比較。Nukeme「ゴミ画像」＋八木沢 vvork→DIS。poor image↔ゴミ画像↔DIS 横断比較。Are.na 仕込み（第8章予告）。K-HOLE／Are.na 初出。

**文案ファイル**：[`archive/反映済み文案/第4章取込_VVORK_文案.md`](./archive/反映済み文案/第4章取込_VVORK_文案.md)

**ステータス**：☑ 完了（2026-06-29）。草稿 L734–746 反映。

---

### inv-khole-1b. 文案：第6章 normcore＋サフィックス＋Are.na＋Archillect/rare.jpg

**前提**：inv-cari-arena ☑。未調査C ☑（[`サフィックス系譜比較調査ノート.md`](notes/サフィックス系譜比較調査ノート.md)）。**着手可能**。

**内容**：第6章冒頭（L1075 後、`## vaporwave の政治的受容` L1077 の前）に数段落を挿入。
1. サフィックスの生産性（-core / -wave / -punk）＝言語的アーキテクチャ
2. normcore＝コンセプトと受容のずれ（充填の事例、distroid との対比）
3. K-HOLE → DIS Magazine → Are.na の接続（人脈線）＋ Are.na の特徴づけ（1〜2文）
4. Archillect / rare.jpg を短節（8-15行）で回収（VVORK の Twitter 移植、bot／匿名人力の二分岐、著者性の消去）

**ブロック1 で使う具体的素材**（[`サフィックス系譜比較調査ノート.md`](notes/サフィックス系譜比較調査ノート.md) より）：
- 三系譜の命名発生様式の違い：-punk＝作家個人→メディア→コミュニティ（上→下）、-wave＝ブロガー→コミュニティ→アーティスト（複雑な相互作用）、-core＝コミュニティ内部→メディア→プラットフォーム（下→上）
- chillwave（2009年・Hipster Runoff）が最初のインターネットマイクロジャンル -wave 語。vaporwave はその「皮肉的変種」
- fashioncore（2002年・Eighteen Visions）が -core のビジュアル美学への最初の転用（侮辱語として発生）
- 意味論的対比：-core＝「核・帰属」、-wave＝「ムード・漂流」。音楽系に -wave、ビジュアルライフスタイル系に -core が優勢になる傾向
- 「意味の希薄化」が三系譜に共通→corecore（2020年）はメタ批評的反転
- サフィックスが存続する理由：「二音節でスタンス・方法・ミリューを包括できるため、参加型文化における命名コストを下げる」

**ブロック3 で使う具体的素材**（[`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md) §3 の素材表から選択）：
- del.icio.us の死 → Are.na 創設（プラットフォーム死のテーマとの接続）
- 「考えるための道具」（最短の特徴づけ）
- 「いいね」不在 or チャンネル＝「まだ形になっていない思考領域」（具体性）
- 第8章（inv-khole-1c）への**予告**にとどめ、CARI との関係の詳細はここでは書かない

**未調査依存**（[`docs/第6章_normcore追加_計画.md`](docs/第6章_normcore追加_計画.md) §未調査 参照）：
- ~~C. サフィックスの系譜（優先度：中〜高）~~ → ☑ [`サフィックス系譜比較調査ノート.md`](notes/サフィックス系譜比較調査ノート.md)（2026-06-28）
- A. normcore 受容の詳細（優先度：低）——文案の depth 次第

**文案ファイル（案）**：[`archive/反映済み文案/第6章_normcore追加_文案.md`](./archive/反映済み文案/第6章_normcore追加_文案.md)

**ステータス**：☑ **完了**（2026-08-13 に草稿現物で検証・クローズ）。ブロック1〜4すべて草稿 **L1395–L1439** に現存——サフィックス来歴（L1395–1397）、`### normcore——冗談から「態度」へ`（L1399–1415）、`### K-HOLE と DIS——形式を借りる批評`（L1417–1425）、`### Are.na——「集めて並べる」がインフラになる`（L1427–1431）、Archillect（L1437）・`@rare_jpg`（L1439）。第1章の indie sleaze → soft grunge 追記も **L227** に現存。
**残1件**：第7章の corecore／yabujincore 追記のみ未確認（1文）。**確定タスクで10分**（下記 §確定タスク）。

---

### inv-khole-1c. 文案：第8章 CARI の Are.na 追記

**前提**：inv-cari-arena ☑。**着手可能**。

**内容**：草稿 **L1497 直後**に1段落を挿入。Facebook → Discord → cari.institute という時系列的遷移と**並行して**、Are.na が視覚資料の研究基盤として機能していることを書く。Are.na は遷移の一ステップではなく**並行する研究レイヤー**。

**記述構造**（[`docs/画像bot挿入_計画.md`](docs/画像bot挿入_計画.md) 第8章セクション参照）：
1. Are.na の性格を短く受ける（第6章 inv-khole-1b で予告済み。繰り返さない）
2. Collins「CARI work is based here on Are.na」＋各 aesthetic に対応チャンネル
3. 三段階知識生産フロー：Discord → Are.na → cari.institute
4. 機能分担：Discord＝動的・会話的、Are.na＝静的・参照的・公開、cari.institute＝規範的

**重複チェック**：L1488 Discord 創設日・L1497 cari.institute の性格は**既出**。繰り返さない。

**分量**：1段落（5〜8行）

**文案ファイル（案）**：[`archive/反映済み文案/第8章取込_CARI_Arena_文案.md`](./archive/反映済み文案/第8章取込_CARI_Arena_文案.md)

**ステータス**：☑ **完了**（2026-06-29 反映／2026-08-13 に草稿現物で検証・クローズ）。草稿 **L1914–L1922** に `### 視覚資料の基盤としての Are.na` 節が現存。三段階知識生産フロー（Discord＝定義を議論し命名を投票で決める動的な場／Are.na＝美学ごとに束ねる視覚資料／cari.institute＝公開）まで記述済み。

---

**方針（共通）**：
- 調査ノートは完成度高。正文は**短い節または段落**単位
- 日本語圏 §11 は原則**本文に入れない**
- 新規ファクトはノート内 URL 範囲内
- 草稿に調査ノート § 参照は入れない（公開 URL のみ）

---

## メタ・著者性（meta-*）

正本：[`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 続8（編集方針確認）。**inv-* 等の正文作業の後**に着手。meta-2 は草稿**末尾**に置き、他タスクより後回し。

| ID | 内容 | 状態 | 行先 | 備考 |
|---|---|---|---|---|
| **meta-1** | 執筆動機ツイート追記 | ☑ | 序文（2026-07-01反映） | 捨て垢（sute_aca、2026-05-27）・布施琳太郎（2026-03-17）のツイート2件を要約統合。「系譜の空白と本稿の射程」節に接地 |
| **meta-2** | 振り返りパート新設 | ☐ | [`草稿.md`](./草稿.md) **末尾**（`## ＜後記＞` の後） | 11万字規模の定期的振り返り。優先度**低・最後**。節構成・挿入位置は文案で決める |
| **meta-3** | 遡行的確定——本稿の自己言及（後記追記） | ☑ **クローズ 2026-08-13** | [`草稿.md`](./草稿.md) L2019・L2025・L2033 | 8-reorg-1〜3 の後記改稿で実装済み。下記詳細節に検証ログ |

### meta-1. 執筆動機ツイート

**背景**  
後記には匿名性の美学・植リンク・歴史化 complicity など自己言及が集中している（ed-4・rev-9 続）。執筆の**直接のきっかけ**となったツイートを1〜2文で接地させ、メタ段落の密集感を和らげる。

**手順**

1. 動機ツイートの URL・日付・引用文を確定  
2. 文案（1段落上限）→ 序文 or 後記のどちらかに反映（後記 L1127 付近の自己言及群と接続しやすい）  
3. 分割稿・推敲メモ更新  

**依存**：なし（単独可）

**ステータス**：☑ 完了（2026-07-01）。ユーザーから2件のツイートを提供：捨て垢（sute_aca、2026-05-27・CARIとvaporwaveサブレディットの関係を指摘）、布施琳太郎（2026-03-17・liminal space等が2010年代前半Tumblr美学の焼き直しに見えるという指摘）。どちらも要約形（全文引用なし、リンクのみ）で「系譜の空白と本稿の射程」節に統合。後記ではなく序文への統合をユーザーが選択（本稿の二本柱＝vaporwave/CARI系譜とTumblr/ポストインターネットアート系譜と対応するため）。公開時はリンク箇所に実際のツイート埋め込みを差し込む想定。文案は`archive/反映済み文案/序文取込_ed6meta1_文案.md`。

### meta-2. 振り返りパート新設

**背景**  
続8 で「長大な草稿では定期的な振り返り・多重記述は必要」と編集方針を確認。現状、第2章 seapunk 節などに章内振り返りはあるが、**全体を俯瞰する振り返り節**は未整備。

**方針**

| 項目 | 方針 |
|---|---|
| 行先 | 草稿**最末尾**（後記の後）。新設 `##` 節 |
| 優先 | **低**。meta-1 等の後 |
| 分量 | 文案で決定（短い総括から着手可） |
| トーン | クロニクル全体の読み返し。ed-4 の「わたしにはわからない」と重複しないよう住み分け |

**手順**

1. 振り返る論点リスト（章横断の糸）を文案に列挙  
2. 文案 → 草稿末尾に反映  
3. 分割稿に後記＋振り返り節を追加するか、後記ファイルに統合するか判断  

**依存**：なし（単独可。**最後**に着手推奨）

### meta-3. 遡行的確定——本稿が行っていることの自己言及

**背景（ユーザー論点・2026-06-17）**  
第5章 `## Frutiger Aeroという問い`（草稿 L1071）には、次の一文がある。

> Frutiger Aeroは遡行的確定の最も明快な例のひとつだ。誰も知らなかった美学に名前が与えられ、定義され、それによって過去が整理される。

本稿は CARI・Aesthetics Wiki・命名の時代を**記述**しているが、同時に**遡行的確定そのものを実行している**可能性がある。過去の単純化、ナラティブの構築、「見方」の誕生や発明——美学のラベル付けと時系列の綴りは、まさしくそのような営みだ。後記でこの論点を少し検討し、追記したい。

**「遡行的確定」とは何か（本稿内の定義）**

| 層 | 内容 | 草稿上の位置 |
|---|---|---|
| **現象として** | 後から付けられた名前・分類が、過去の断片を「あの美学のひとつ」としてまとめ直す | 序文 L23、第5章 L1067（OPN「最初のvaporwave」）、L1071（Frutiger Aero） |
| **三過程モデル**（推敲メモ） | ラベルの仮予約 → コミュニティによる充填 → **遡行的確定**で事後的に実体化 | [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 層4・続8 |
| **本稿への跳ね返し** | クロニクルが witch house→vaporwave→CARI と**線を引く**こと自体が、過去の整理・ナラティブ構築である | 後記 L1244（ed-4：「線を引いている」）の**理論的補強** |

**ed-4・既出後記との住み分け**

| 既出 | meta-3 で書くこと | 書かないこと |
|---|---|---|
| **ed-4**（L1244） | 歴史化＝制度化、Cook 事例、「線を引いている」 | 同じ比喩の繰り返し |
| **匿名性 C3**（L1242） | 「名づけたこと自体が加担」 | 匿名性の再説明 |
| **L1236**「起きたことの歴史」 | **記録＝中立な鏡ではない**という問いかけ | 「記録は嘘だ」という断定 |
| **meta-3 の核** | 遡行的確定は**観測対象でもあり本稿の方法でもある**。Frutiger Aero の例を**手がかり**に、見方の発明・過去の単純化を自覚する | 学術総論化、Wittgenstein 等の長い理論展開 |
| **inv-vernacular-photo**（上記・第4章その他） | vernacular photography が後から収集・分類されてジャンル化した経緯を、遡行的確定の**先行例**として1文だけ添えられるなら合流可 | 4つの糸（vernacular web／匿名性／poor image／non-place）の本格的な理論展開はここではしない |

**論点メモ（後記で扱う候補）**

1. **二重性**：Frutiger Aero は2017年に造語されたが、指すビジュアルは2005年頃からあった（序文 L23）。本稿も2020年代の語彙で2000年代の断片を束ねている。
2. **単純化**：時系列・章立て・「命名の時代」「制度化」は、複雑な並行を一本の線にした**見方の発明**でもある。
3. **正直な complicity**：ed-4 の「線を引いている」を、遡行的確定という本稿の**分析概念**で言い直す。謝罪ではなく方法の自覚。
4. **締めとの接続**：「十年後にどう読まれるかわからない」（L1244）へ自然につなぐ。

**挿入位置（推奨）**

| 候補 | 利点 |
|---|---|
| **L1242〜L1244 のあいだ**（匿名性 C3 の後、ed-4 の前） | 名づけ・来歴開示 → **遡行的確定** → 歴史化（Cook）の順で理論が積み上がる |
| **L1244 の直後**（ed-4 段落の拡張） | 既存「線を引いている」を受けて1段落追加。重複注意 |

**分量・トーン**

- **1段落**（長くても2段落）上限
- 説教・謝罪ではなく、ed-4 と同型の**ループの自覚**
- Frutiger Aero の一文を**短く引用または言い換え**して手がかりにする（第5章の再掲は最小限）

**手順**

1. 上記論点から後記用文案を作成（`後記取込_meta3_遡行的確定_文案.md` 等）  
2. ユーザー承認 → 草稿 `## ＜後記＞` に反映  
3. 分割稿・[`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 更新  

**正本・参照**

- 草稿 L23（序文・遡行的確定の初出）、L1067–L1071（第5章 Frutiger Aero 節）
- [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) 層4・続8（三過程モデル・本稿の独自性）
- [`後記取込_制度化ループ_文案.md`](./archive/反映済み文案/後記取込_制度化ループ_文案.md)（ed-4・住み分け用）

**ステータス**：☑ **クローズ**（2026-08-13）。**8-reorg-1〜3 の後記改稿で、meta-3 の核が本文に実装済み**と判断。草稿の現物で確認した3箇所——

- **L2019**「ただし、この結節点も、さきほどの見取り図と同じく、**本稿が持ち込んだ図式にすぎない**。」（＝見方の発明の自覚）
- **L2025**「第1章で見たように、**本稿もすでに indie sleaze を、遡及的に名づけられた語として記録している**。」（＝遡行的確定を本稿が実行していることの明示。上表「本稿への跳ね返し」そのもの）
- **L2033**「本稿もまた、ここまで過去のイメージを並べて「いま」を読み解こうとしてきた。「**lo-fi」と「HD」の図式も、「匿名性の美学」という名づけも、その結果として持ち込んだ道具立てだ**。」（＝上表「meta-3 の核」に対応）

分量・トーンの条件（1段落・説教や謝罪ではなくループの自覚）も満たしている。Frutiger Aero を手がかりにする案は**採らず**、RA記事の indie sleaze 例を手がかりにする形で実装された。**独立タスクとしては起こさない**。

---

## 結論部改稿（concl-*）

正本：[`CARI_調査ノート.md`](notes/CARI_調査ノート.md) §2（Guardian 2016・Leigh Alexander）、§7 執筆メモ 2d。**cari-draft 後推奨**（同一記事の別端。rev-7 の fashwave 記事とは別）。

| ID | 内容 | 状態 | 文案（案） |
|---|---|---|---|
| concl-1 | Guardian 2016 結論の**時代診断**問いかけ（ユーザー改稿・案A） | ☑ | [`第5章取込_結論_Guardian問いかけ_文案.md`](./archive/反映済み文案/第5章取込_結論_Guardian問いかけ_文案.md) |
| concl-2 | 末尾——HTML／ブラウザ後方互換・アーカイブ危機・ベンダーロックイン | ☐ | 下記詳細節 |

### concl-2. 末尾——技術的条件（HTML後方互換・アーカイブ危機・ベンダーロックイン）

**背景（ユーザー指示・2026-06-17）**  
本稿はプラットフォームのアーキテクチャを通史の軸にしているが、**技術基盤そのもの**——HTML とブラウザの高い後方互換性、アーカイブ危機、ベンダーロックイン——については本文各所に散在するのみで、**最後に一度だけ軽くまとめて触れたい**。

**論点の三層（文案の骨格）**

| 論点 | 要点 | 草稿上の既出フック（再掲最小限） |
|---|---|---|
| **HTML・ブラウザの後方互換** | ウェブの**ファイル形式**（HTML/CSS）は長期にわたり高い後方互換を持つ。1990年代のヴァナキュラーウェブも、環境を再構成すれば**いまのブラウザで読める**ことがある | 第1章 GeoCities・Olia Lialina／One Terabyte of Kilobyte Age（当時のブラウザ環境で再構成）、MySpace の HTML/CSS カスタム |
| **アーカイブ危機** | 互換性があるのは**ファイル**であって**プラットフォーム上の生活**ではない。GeoCities 閉鎖、MySpace 音源喪失、リンクロット、Wayback の欠落——美学の断片は**消えうる** | 第1章 L43–49・L77、第4章 Wayback 依存、後記 L1240「植リンク」 |
| **ベンダーロックイン** | 美学は Tumblr・Discord・TikTok・Spotify 等の**ベンダー所有の場**に依存する。DMCA 一斉削除、サーバー移行事故、API・アルゴリズム変更で流通の仕方が変わる | 第1章 mp3ブログ DMCA（L63）、序文のプラットフォーム連鎖、第5章 Discord 制度化、Cook プレイリスト（ed-4） |

**含意（1段落で言えること）**  
保存・分類への欲望（CARI、Wiki、本クロニクル）は、アーカイブ危機への**応答**でもある。しかし百科や wiki に固定しても、**元データがプラットフォーム側に閉じ込められたまま**では根本は解けない。HTML の長寿とプラットフォームの短命の**ずれ**が、インターネット美学の歴史を書く条件でもある。

**`concl-1`・後記との住み分け**

| 既出 | concl-2 で書くこと | 書かないこと |
|---|---|---|
| **concl-1**（L1226） | Guardian 十年問いの**技術的裏側**を1文で受ける余地 | Guardian の再引用 |
| **後記 L1240**（植リンク） | リンクとアーカイブの**構造問題**へ接続 | 植林活動の再説明 |
| **ed-4**（L1244） | 歴史化＝制度化と**データの単一所有者**問題は別軸 | Cook 事例の繰り返し |
| **meta-2**（振り返り） | 著者の執筆振り返り | 技術論の本格展開 |

**挿入位置（推奨）**

| 候補 | 利点 |
|---|---|
| **`## クロニクルの終わりにあたって` 末尾**（L1226 の後、`---` の前） | concl-1（Guardian）の直後。時代問い→**この記録が立つ土台**の順 |
| **後記 L1244 の直後**（最終文の前） | 植リンク・歴史化のあと、**技術的条件**で締める |
| **後記の後・新設 `##` 節**（meta-2 と同居可） | 本論とメタを分離。分量が増えるならここ |

**推奨**：**L1226 直後**（concl-1 段落の続きとして **1段落**）。後記は著者性・complicity のまま。

**分量・トーン**

- **1段落**上限（長くても2文組みの短い2段落）
- 技術解説・政策論・総括化にしない。**軽く触れる**
- 新規ファクトの大量追加は不要——既出 URL への言及で足りる（Doctorow 2019、GeoCities、MySpace 事故は第1章済）

**手順**

1. 上記三層から文案を作成（`結論取込_concl2_技術条件_文案.md` 等）  
2. ユーザー承認 → [`草稿.md`](./草稿.md) 反映  
3. 分割稿・推敲メモ更新  

**正本・参照（既出）**

- 草稿 第1章 GeoCities（L35–49）、MySpace（L73–77）、mp3ブログ DMCA（L63）
- 草稿 序文 L9–11（プラットフォーム連鎖）、後記 L1240（植リンク）
- Cory Doctorow（MySpace 事故後）：https://boingboing.net/2019/03/17/facebook-is-next.html

**ステータス**：☐ 計画先行。文案 → 承認 → 末尾反映。**優先度低**（meta-1／meta-3／ed-6 の後でも可）。

### concl-1. Guardian 時代診断問い——**完了（2026-06-11）**

☑ [`第5章取込_結論_Guardian問いかけ_文案.md`](./archive/反映済み文案/第5章取込_結論_Guardian問いかけ_文案.md) → クロニクル末尾 L1018 直後。

## 6. Seapunk 詳細調査ノート——**完了（2026-06-02）**

6a–6f・§9-man・§9 ☑。残品質チェックは索引 §Seapunk 後続（6b/6c/6d 残）。

| 正本 | 内容 |
|---|---|
| [`docs/Seapunk調査_取り込み計画.md`](docs/Seapunk調査_取り込み計画.md) | 取込計画 |
| [`archive/Seapunk取込文案/`](./archive/Seapunk取込文案/) | 反映済み文案 |
| [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) | 6b–§9 ログ |

§9 aesthetic 包含関係は **aesthetic-rev-1**（第3章）で上書き済。

## 完了済み（詳細は推敲メモ）

| フェーズ | 完了日 | ログ |
|---|---|---|
| 1 ブロック F | 2025-05-29 | 推敲メモ 続8 |
| 2 三枠境界論 | 2025-05-31 | 推敲メモ 続10〜11・序文改稿 |
| 3 ドキュメント整理① | 2025-05-31 | 推敲メモ 続14 |
| 4 ファクト補強 #11〜22 | 2025-05-31 | ファクト補強調査・推敲メモ 続12〜13 |
| 5 ドキュメント整理② | 2025-05-31 | 第3〜5章分割稿・README |
| §8-1 序文・aesthetic 統合稿 | 2026-06-01 | 推敲メモ 続17・[`序文_改稿.md`](manuscript/序文_改稿.md) |
| §8-2 Tumblr For You | 2026-06-01 | [`§8-2_Tumblr_ForYou_調査メモ.md`](notes/§8-2_Tumblr_ForYou_調査メモ.md)・推敲メモ 続18 |
| §8-3 KYM Wayback 訂正 | 2026-06-01 | 序文_改稿・第2章分割稿・覚書 L129 |

---

## 明晰さレビュー（2026-06-25）

正本：[`docs/草稿_明晰さレビュー.md`](docs/草稿_明晰さレビュー.md)

序文＋全8章＋後記を通読し、わかりやすさを多面的に評価。章ごとの指摘と全体に共通する課題を記録。

**全体に共通する課題（6点・2026-08-18に全件検証・クローズ）**

| # | 課題 | 検証結果 |
|---|---|---|
| 1 | **「充填」の定義問題**——初出時に明確な定義がない | ☑ 解消（ed-7で序文に定義節を新設） |
| 2 | **章番号の不一致と誤記**——distroid章番号、「第5章以降」、序文の第7章欠落 | ☑ 解消（全箇所grep確認済み） |
| 3 | **比重の偏り**——seapunk・Lopatin-Cook年表など本筋外の詳述 | ☑ 解消／対応不要（seapunkは明示的な断り書きで正当化。Lopatin-Cookはコラム化） |
| 4 | **前章が投げた問いの未回収**——「軽さと深み」等 | ☑ 解消（該当する第6章末の問い自体が構造変更で現存しない） |
| 5 | **想定読者のレベルの揺れ**——専門用語と平易な記述の同居 | △ 軽微に残存（barcamp等、実害小さいと判断） |
| 6 | **一人称的コメントの混在**——文体の不統一 | ☑ 解消（該当箇所は現存せず） |

**誤字・誤記**（行番号は2026-06-25時点。2026-08-13に全6件を grep 再検証）

| 当時の行 | 内容 | 状態 |
|---|---|---|
| L467 | 「この記事がで公開されたときには」——脱字 | ☑ 修正済（該当なし） |
| L639 | 「すこしづつ」→「すこしずつ」 | ☑ 修正済（該当なし） |
| L741 | 「複雑なプロモーションでによる」——誤字 | ☑ 修正済（該当なし） |
| L1029 | 「第5章以降にゆずる」→「第6章以降」 | ☑ 修正済（該当なし） |
| L1494 → **現 L1915** | 「特に2016年以降に2016年4月に」——重複 | ☑ **修正済（2026-08-18・fractal-8）** |
| L1495 → **現 L1916** | 「理由にある可能性がある」→「理由である可能性がある」 | ☑ **修正済（2026-08-18・fractal-8）** |

**IndieWebとNeocities節の内容不足（2026-08-18・fractal-8で発見・応急対応）**

第8章「IndieWebとNeocities：対位法として」節は、見出しに「IndieWeb」とあるにもかかわらず本文が終始Neocitiesの話のみで、IndieWebへの言及が一切なかった（明晰さレビュー課題と一致）。応急対応として見出しを「## Neocities：対位法として」に変更し、見出しと内容の不一致は解消した。

ただし本来の構想は、CARI/Aesthetics Wikiの制度化と対をなす「対位法」として、IndieWebとNeocitiesという2つの非制度的な個人ウェブの動きを並べることだった可能性が高い。調査ノート[`notes/インディーウェブの歴史年表.md`](../notes/インディーウェブの歴史年表.md)（366行）が既に存在するため、IndieWebの段落を新たに書き起こして節を本来の構想に戻すかどうかは、筆者判断を要する（新規執筆であり推敲の範囲を超えるため、fractal-8では実施せず）。

**明晰さレビュー・全章検証 ☑ 完了（2026-08-18）**

2026-06-25時点の指摘を、序文＋全8章にわたって現物の草稿と照合し、章ごとに検証した（既存指摘の再検証というアプローチ。新規の通読レビューは行っていない）。結果、**大半がfractal-1〜8の推敲パスや各種reorg作業で既に構造ごと解消されていた**。

| 章 | 指摘 | 検証結果 |
|---|---|---|
| 序文 | 小見出し配置、充填・フォークソノミーの初出定義ずれ、各章案内で第7章欠落 | ☑ 解消。ed-7で該当節（旧「### 制度化」「### アーキテクチャと各章」）を削除し3節に再構成。「充填」「フォークソノミー」とも初出時に定義済み |
| 第1章 | mp3ブログ節の唐突さ、ポストインターネットアート定義の後回し、Megazord節の比重、二つの流れの提示順 | ☑ 解消。橋渡し文の追加、定義の即時提示、「二つの流れ」枠組みへの明示的接続、章前半での早期導入をそれぞれ確認 |
| 第1章 | 日本語圏受容節の接続の弱さ、barcamp語の説明省略 | △ 軽微に残存。実害小さいと判断し対応不要 |
| 第2章 | 20jfg節の位置、L234主述のねじれ、L288一人称コメント、distroid章番号不一致 | ☑ 解消。fractal-2の再構成で自然な直線的順序に、文法・文体上の問題も現存せず、distroidは全箇所で「第4章」に統一 |
| 第3章 | seapunk節の比重、「充填」初出定義、憑在論段落の情報過密 | ☑ 解消。節冒頭に一次資料の厚みを理由とする断り書きを追加、序文で「充填」定義済み、fractal-3で段落を3分割 |
| 第3章 | seapunk死と遺産→DMY Magazineへの時系列遡行 | ☑ 検討済み・現状維持。fractal-3で再検討し、Adam Harperの伏線を優先する構成上の判断として意図的に保持 |
| 第4章 | Daniel Lopatin/A. G. Cook・IDL補遺節、L701主語混乱 | ☑ 解消。両節とも「### コラム：」形式に変更、主語も段落ごとに明確化 |
| **第4章** | **第3章末尾との記述の重複**（Adam Harper/Charlie Jonesの要約が章境界をまたいで反復） | ☐ **残存**。著者確認の結果、対応不要と判断（2026-08-18） |
| **第4章** | **末尾「アーキテクチャ：lo-fiとHD」節がプラットフォーム条件に触れず短い**（他章の同名節と比較） | ☐ **残存**。著者確認の結果、対応不要と判断（2026-08-18） |
| 第5章 | L1029誤記、「物象化」の術語含意、「同じひとつのこと」の指示語 | ☑ 解消／軽微に残存。誤記は修正済み、他2件は文脈から意味を読み取れる範囲と判断 |
| 第5章 | 章末「振り返り」の冗長性（「三つの段階」「プラットフォームと速度のずれ」との反復） | ☑ 検討済み・現状維持。fractal-5で振り返り節の要約機能として意図的な反復と判断 |
| 第6章 | vaporwave政治化と章題の関係、Lara López Millán参照過多（9回）、結語の軽さ/深み対比 | ☑ 解消。章題自体が「名前があとから来る」に変更されテーマ整合、参照は2回に整理、結語も「## 2020年へ」に置き換え |
| 第6章 | 冒頭文のねじれ、「推敲した」の比喩 | △ 軽微に残存。実害小さいと判断し対応不要 |
| 第7章 | Rafman-cursed images間の空白、Augé non-place参照の曖昧さ、L1297段落の論点過多 | ☑ 解消。系譜の限界を明示的に留保する記述、参照元（Aesthetics Wiki）の明記、単一結論への一貫した論証を確認 |
| 第7章 | QAnon言及の唐突さ、hyperpop節の時間軸逸脱、第6章末の問い未回収 | ☑ 検討済み・現状維持。fractal-7の章レベル点検で射程宣言・構成上の意図を確認済み。「軽さ/深み」の問い自体は第6章の構造変更で現存しない |
| 第8章 | IndieWeb節タイトル不一致、誤字2件 | ☑ 解消（2026-08-18・fractal-8で対応） |
| 第8章 | 系譜の重なり節の固有名詞密集、後記の二役割同居 | ☑ 解消。fractal-8で密度分割2件を実施、FairyPage批評と後記のメタ的記述も別セクションに整理済み |
| **第8章** | **「遡行的確定」が造語か既存学術用語か注釈がない** | ☐ **残存**。著者確認：意図的な造語だが、注釈は不要と判断（2026-08-18） |

**結論**：未解消3件はいずれも著者判断で対応不要とし、明晰さレビューは全項目**クローズ**。`docs/草稿_明晰さレビュー.md`は2026-06-25時点のスナップショットとして残すが、以後の参照対象からは外す。

---

## クイックリファレンス

> **⚠️ この表は状態を持たない。** 以前は本表・§タスク索引・各詳細節・§アクティブ・パイプラインの**4箇所に同じIDの状態が重複記載**され、更新が表だけに入った結果、meg-*／inv-khole-1b/1c／fractal-3 が「完了しているのに☐のまま」放置されていた（2026-08-13 に検証してクローズ）。**状態は §タスク索引 と各詳細節の2箇所のみに書く。**

| 段階 | 次の1手 |
|---|---|
| **今** | §確定タスク（MySpace年号・章番号詳細確認・第3章アーキテクチャ節・corecore・inv-hypnagogic 文案・IndieWeb節の扱い） |
| **その次** | 未定（筆者判断。fractal-1-meta／cons-2／その他低優先タスクから選択） |
| **クローズ済み（2026-08-18）** | **明晰さレビュー全章検証** ☑（全体課題6点＋章別28件、詳細は§明晰さレビュー） |
| **8月末〆でスコープ外の候補** | cons-2／inv-swan／inv-tabor／inv-vektroid／inv-vernacular-photo／rev-4／rev-12／meta-2／concl-2／fractal-1-meta（**未決**——切るかどうかは筆者判断） |
| **クローズ済み（2026-08-13 検証）** | fractal-3 ☑／meg-1〜3 ☑／inv-khole-1b ☑／inv-khole-1c ☑／6b残 ☑／明晰さレビュー誤字4件 ☑／crw-1 ☑／meta-3 ☑ |

**索引の正本**：§タスク索引（本ファイル上部）

---

## 参照ファイル

| ファイル | 役割 |
|---|---|
| [`草稿.md`](./草稿.md) | 正本 |
| [`docs/草稿_推敲メモ.md`](docs/草稿_推敲メモ.md) | 改稿ログ（完了フェーズの詳細） |
| [`docs/草稿_ファクト補強調査.md`](docs/草稿_ファクト補強調査.md) | ファクト候補 #6〜22 |
| [`Seapunk 詳細調査ノート.md`](notes/Seapunk 詳細調査ノート.md) | Seapunk 横断調査の正本 |
| [`docs/Seapunk調査_取り込み計画.md`](docs/Seapunk調査_取り込み計画.md) | 6a 成果物——行単位の取込タスク |
| [`序文_改稿.md`](manuscript/序文_改稿.md) | §9 保留論点・KYM Wayback 年表 |
| [`§8-2_Tumblr_ForYou_調査メモ.md`](notes/§8-2_Tumblr_ForYou_調査メモ.md) | Tumblr アルゴリズム年表 |
| [`FrankJavCee文字起こし.md`](./sources/transcripts/FrankJavCee文字起こし.md) | §9 FrankJavCee 分析の正本 |
| [`tumblrwave_speakers.srt`](./sources/transcripts/tumblrwave_speakers.srt) | H∆SHTAG$ ep5 話者確定字幕（6c-2 正本） |
| [`blogpop_speakers.srt`](./sources/transcripts/blogpop_speakers.srt) | H∆SHTAG$ ep6 話者確定字幕（S1 横断参照） |
| [`aestheticに関する手動調査.md`](notes/aestheticに関する手動調査.md) | aesthetic 語法・Floral Shoppe コメント年代・X 検索ログ（2026-06-02） |
| [`archive/Seapunk取込文案/Seapunk取込_6d-review_文案.md`](./archive/Seapunk取込文案/Seapunk取込_6d-review_文案.md) | 6d-review 反映用本文（アーカイブ） |
| [`docs/6d-review_aesthetic論点整理.md`](docs/6d-review_aesthetic論点整理.md) | aesthetic 零れ落ち・層A–E |
| [`docs/6d-review_第2章構成案.md`](docs/6d-review_第2章構成案.md) | #### 案・フェーズ分割 |
| [`witchhouse-chillwave調査メモ.md`](notes/witchhouse-chillwave調査メモ.md) | witch house／chillwave 調査 |
| [`docs/草稿_レビュー論点メモ.md`](docs/草稿_レビュー論点メモ.md) | レビュー論点の正本・rev-* ロードマップ |
| [`musicplusghost.md`](./sources/transcripts/musicplusghost.md) | FEECO *MUSIC + GHOST* 全文テキスト（src-1 正本） |
| [`supersuper.md`](notes/supersuper.md) | SuperSuper! 号別調査・PC Music 前史（src-2 正本） |
| [`HipposInTanks_調査ノート.md`](notes/HipposInTanks_調査ノート.md) | HIT カタログ・vaporwave 前史（src-5 正本） |
| [`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](notes/MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md) | MP3ブログ・レーベル史・MySpace/Tumblr設計史（src-6 調査正本） |
| [`docs/src-6_仕分け.md`](docs/src-6_仕分け.md) | src-6a 成果物——節別仕分け・フェーズ6b–6f・委譲表 |
| [`vaporwave政治化_調査ノート.md`](notes/vaporwave政治化_調査ノート.md) | rev-7 正本（2016 fashwave・コミュニティ応答・Boriswave） |
| [`Vaporwave Is (Not) a Critique of Capitalism_Genre Work in An Online Music Scene.md`](./sources/papers/Vaporwave%20Is%20(Not)%20a%20Critique%20of%20Capitalism_Genre%20Work%20in%20An%20Online%20Music%20Scene.md) | Whelan & Nowak 2018 全文（@ccchristtt 引用含む） |
| [`Vaporwave_Politics_Protest_and_Identity.md`](./sources/papers/Vaporwave_Politics_Protest_and_Identity.md) | McLeod 2018 全文（PDF 抽出） |
| [`note_極右の世界のBGM.md`](./sources/transcripts/note_極右の世界のBGM.md) | ykic 二次・fashwave 年表（Vice 日付は14日に訂正） |
| [`CARI_調査ノート.md`](notes/CARI_調査ノート.md) | cari-inv／cari-draft 正本（Guardian・Facebook 制度化・Priz Tats） |
| [`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) | **ed-6**／**aesthetic-rev-2** 正本（語史・Wikipedia・制度化） |
| [`aesthetic_文法分析メモ.md`](notes/aesthetic_文法分析メモ.md) | **aesthetic-rev-1** 正本（三モード・質/種・二軸統合） |
| [`khole-arena-archillect-researtch.md`](notes/khole-arena-archillect-researtch.md) | **inv-khole-*** 正本（K-HOLE／Are.na／VVORK→Archillect。**aesthetic-reorg とは独立**） |
| [`Arena設計思想調査ノート.md`](notes/Arena設計思想調査ノート.md) | **inv-cari-arena** 成果物（Are.na 設計思想・CARI 研究基盤・Discord 三段階フロー。2026-06-27） |
| [`サフィックス系譜比較調査ノート.md`](notes/サフィックス系譜比較調査ノート.md) | **未調査C** 成果物（-core/-wave/-punk 三系譜の語源・増殖ロジック・横断比較。2026-06-28） |
| [`scene_subculture_notes.md`](notes/scene_subculture_notes.md) | Scene サブカルチャー・-core サフィックス詳細・Indie Sleaze 調査（2026-06-28）。fashioncore→scene→normcore 系譜、MySpace 共依存、Indie Sleaze 遡及的命名 |
| [`CARIの歴史.md`](notes/CARIの歴史.md) | CARI 公式年表の和訳 |
| 新蒸気波要点ガイド（佐藤秀彦編・DU BOOKS 2019） | 第3章 aesthetic 節（ばるぼら年表・大辞典）。**骨架的インタビュー**は **intro-kojiateki** |
| [`docs/草稿_明晰さレビュー.md`](docs/草稿_明晰さレビュー.md) | **明晰さレビュー**（2026-06-25・章別評価＋全体課題6点＋誤記一覧） |
| [`docs/編集方針.md`](docs/編集方針.md) | ed-1〜3 の根拠 |
| [`第2章_命名の時代.md`](manuscript/第2章_命名の時代.md) | 第2章分割稿（**ed-3 Phase 3・任意**） |

---

*更新：2026-07-24。**crw-1** ☑ 全区間点検完了（L1–L1843・**一時停止**）。**ban-cons-1** ☑ 草稿正本 grep 確認（L1320–1340 基準・L1576・L1789 整合・章間矛盾なし）。残は **cons-2**（tumblrタイムライン・分割稿・L1330 Instagram 任意）。*
*更新：2026-07-27。**crw-1** 進捗——**L158–L1000 検討済**（第1章後半〜第4章 `### 遡及的確定として` まで）。L1–L156 は 2026-07-23 反映済。次区間 **L1003–**（第5章 aesthetic）。行番号は [`草稿.md`](./草稿.md) 現行版（約1850行）基準。*
*更新：2026-08。**ed-7** ☑——序文 L3–L41（3節）に圧縮。制度化定義→第5章初出。章概観・来歴節削除。*
*更新：2026-08。**RBMA字幕** ☑・**ed-7** タスク化。*
*更新：2026-07-23。**crw-1** 追加——草稿全体の認知リズム推敲を**最優先**に設定（正本 [`cognitive-rhythm-writing/SKILL.md`](./cognitive-rhythm-writing/SKILL.md)）。**cons-2** はその次。*
*更新：2026-07-23。**7-reorg-0〜2** ☑（**1d・1e** 含む）——第7章「爆発」reorg 完了。[`docs/第7章_reorg_計画.md`](docs/第7章_reorg_計画.md)／[`第7章_reorg_文案.md`](./archive/反映済み文案/第7章_reorg_文案.md) を正本とし、[`草稿.md`](./草稿.md) L1362–1644 へ全文差替え（前史→COVID→爆発→制度化→D/W→cottagecore→TikTok→hyperpop/brat→Discord→章末アーキテクチャ）。**7-reorg-3／4** はユーザー判断でスコープ外。*
*更新：2026-07-17。**7-reorg-1d／1e** 進行中（[`第7章_reorg_文案.md`](./archive/反映済み文案/第7章_reorg_文案.md)＋[`liminal_制度化_Backrooms_言説メモ.md`](notes/liminal_制度化_Backrooms_言説メモ.md)）。`timeline.md`／`README.md`／`context-map.md` に liminal 制度化年表・新規メモを還流。完了後 **7-reorg-2**（草稿全文差し替え）。*
*更新：2026-07-07。**6-reorg-0〜5** ☑——第6章「名前があとから来る」の再構成が完了。（1）章冒頭に-wave/-coreサフィックスの求心力を追記、（2）normcoreの読み筋（-coreラベルが一般に広く知られた最初の事例／Aesthetics Wiki項目）を冒頭と結びの2箇所に明示、（3）匿名性の美学（Archillect/rare.jpg）から第7章liminal spaceへの伏線を1文追加、（4）`## 名付け親の分からない美学——dark academia と cottagecore` 統合節を新設し、旧`実体先行型`等の型語彙を廃止して具体的なタグ・投稿・日付ベースの記述に書き換え（第7章冒頭・クロニクル末の相互参照2箇所も同様に修正）、（5）`## vaporwave の政治的受容` 節全体を再構成（⑥-full。当初計画は接続文の追加のみだったが、章冒頭予告に節本体が応えていないという指摘を受けて追加）——fashwaveとsynthwaveの関係の誤り（Anglinが「オルタナ右翼の公式サウンドトラック」と呼んだのはsynthwave、BuzzFeedが"the sound of young white nationalism"としたのはfashwave）を訂正し、出典を明記、文体チェックを3周実施、ユーザーによる事実確認（Cybernazi投稿日、BuzzFeed Japan訳、Rave News引用、Anglinの肩書き=創設者、altcensored.comリンク3件の要否）を経て確定。文案は[`第6章_reorg_DA-cottagecore_文案.md`](./archive/反映済み文案/第6章_reorg_DA-cottagecore_文案.md)、経緯・妥当性評価は[`docs/第6章_reorg_計画.md`](docs/第6章_reorg_計画.md)。すべて`草稿.md`第6章に反映済み。次は**cons-2**（timeline／context-map還流。第6章分を追加）。*
*更新：2026-07-01。**ed-6** ☑・**meta-1** ☑——序文を全面改稿。新設節「### 「インターネット美学」とは何か」（冒頭。日本語版Wikipedia「インターネット・エスセティック」／アニヲタWiki（仮）／美学ウィキ（Scrapbox「美学ミーム」ページ、fairypage 2021年定義・Aesthetics Wikiの視覚的多様性ポリシー）の3定義を踏査。「複数の媒体を並行して同時に占めることが美学として成立する条件」という論点をAesthetics Wikiの特筆性ポリシーで裏付け。vaporwaveを「音楽ジャンルとして生まれ、のちに美学のひとつとなった」例として提示。用語を3層整理：美学＝個々の様式／美学ミーム＝命名を通じて美学を作り出す動き／インターネット美学＝美学の総体）。「### 系譜の空白と本稿の射程」に動機ツイート2件（捨て垢sute_aca 2026-05-27・布施琳太郎2026-03-17）を要約統合（meta-1）。新設節「### 「インターネット美学」という言葉の来歴」（ed-6。口語用法と今日的カテゴリ用法の層の違い→2020 Washington Post→2022年Aesthetics Wiki/Wikipedia制度化→2025 EBSCO）。「### アーキテクチャと各章」の章番号ずれ（第2〜7章の言及が実際の章立てと1つずつずれていた旧バグ）を修正。第5章と内容が重複する旧「### aesthetic という語」節は削除。「### 充填、フォークソノミー、横断性」は圧縮。あわせて`草稿.md`本体で「美学ミーム」の用法を監査（24箇所）し、個体扱いになっていた2箇所（L207「美学ミームの群れ」→「美学の群れ」、L1319「ひとつの美学ミームとして」→「ひとつの美学として」）を修正。序文は約3500字→約5650字。文案は`archive/反映済み文案/序文取込_ed6meta1_文案.md`。*

*更新：2026-06-29。**inv-khole-1c** ☑——第8章 `## CARI設立とプラットフォームの意味` 末尾（旧 L1569 直後）に Are.na 4段落（草稿 L1571–1577）を反映。Facebook→Discord 議論の場の移行と並行する視覚資料レイヤーとして Are.na を位置づけ（チャンネル構造・cari.institute 各ページとのリンク・三層分担 Discord/Are.na/cari.institute・Maintenance Effort 92中58・Broskoski による Collins アカウント言及）。典拠：Arena設計思想調査ノート.md §6・§10。Broskoski 発言出典は Upstatement インタビュー。次は ed-6 polish。*

*更新：2026-06-29。**inv-khole-1b** ☑——第6章 導入直後（`## vaporwave の政治的受容` の前）に `## ラベルが増えるとき——サフィックスと匿名のキュレーション`（6小節：サフィックスの生産性／normcore——冗談から「態度」へ／「態度」から「ファッション」へ／K-HOLE と DIS／Are.na／無言のキュレーションが Twitter に移るとき。L1103–1141）を反映。あわせて第1章 L155 に Indie Sleaze→Soft Grunge 追記、第7章 `### -core サフィックスの標準化`（L1383）を第6章後方参照に書き換え、L1421 yabujincore 段落末に corecore 対比を追記。一次資料補強：Interview オーラルヒストリー（Brad Troemel＝normcore を Duncan に伝えた人物＝第1章 The Jogging／89plus 委嘱／Estrada コミック）、designboom で 89plus 参加者（Steyerl・Trecartin・DIS Magazine・Brad Troemel 同席）確定。文案 → 反映済み。次は inv-khole-1c。*

*更新：2026-06-29。**inv-khole-1a** ☑——第4章 Steyerl 直後に `### VVORK と「無言のキュレーション」`（6段落、L734–746）反映。VVORK 形式＋MULTIPLEX 人脈＋The Jogging 比較＋nukeme「ゴミ画像」＋横断比較（poor image→DIS 伏線）＋Are.na 仕込み。K-HOLE/Are.na 初出。文案 → archive。次は inv-khole-1b。*
*更新：2026-06-29（早）。**inv-khole-1a** 草稿初反映（3段落版）。のち Steyerl 直後へ移動・6段落へ拡張。*
*更新：2026-06-28。**未調査C** ☑——[`サフィックス系譜比較調査ノート.md`](notes/サフィックス系譜比較調査ノート.md) 完成。-core/-wave/-punk 三系譜の語源・増殖ロジック・横断比較。inv-khole-1b の全前提解消。*
*更新：2026-06-27。**inv-cari-arena** ☑——Are.na 設計思想・CARI 研究基盤・Discord 三段階知識生産フロー調査完了。「プラットフォーム共有＋設計思想の構造的親和」で確定。inv-khole-1a/1b/1c 全て着手可能に。*
*更新：2026-06-22。**ed-3** ☑——seapunk 読み道 Phase 1–2 草稿反映完了。分割稿同期は任意。*
*更新：2026-06-19（続36）。**intro-kojiateki** 更新——引用 ☑、挿入位置を**第2章冒頭・新設節**（序文・L269案は却下）、エクスペリメンタル接点を明記。*
*更新：2026-06-19（続35）。**intro-kojiateki** 骨架的インタビュー挿話（序文／第2章導入・「その頃のインターネットの雰囲気」）タスク追加。*
*更新：2026-06-19（続34）。**inv-opn-cook** OPN×A. G. Cook コラボ（vaporwave 系譜と PC Music の交差）タスク追加。*
*更新：2026-06-19（続33）。**src-4b** ハイパーポップ追記（Spotify「Hyperpop」命名→brat summer）タスク追加。*
*更新：2026-06-19（続32）。**inv-khole-0/1** を **aesthetic-reorg から分離**（別調査・別パイプライン）。**meg-1〜3** Megazord URL／Gatekeeper コメント追補タスク追加。*
*更新：2026-06-19（続31）。**aesthetic-reorg-0〜2**／**aesthetic-rev-1/2** タスク群追加（第2章 aesthetic 節の独立章化考察→書き換え）。*
*更新：2026-06-17（続30）。**6b-reorg 後続** M.I.A.・Tim and Eric ☑（seapunk「死」節・激怒記事直後）。*
*更新：2026-06-17（続29）。**concl-2** タスク追加（末尾・HTML後方互換／アーカイブ危機／ベンダーロックイン）。*
*更新：2026-06-17（続28）。**ed-6** タスク追加（序文・インターネット美学と制度化の説明節）。調査ノート [`internet_aesthetic語と制度化_調査ノート.md`](notes/internet_aesthetic語と制度化_調査ノート.md) 新設。*
*更新：2026-06-17（続27）。**meta-3** タスク追加（遡行的確定・本稿の自己言及——後記追記）。*
*更新：2026-06-17（続25）。**inv-piajp** ☑ 文案＋草稿反映（第1章・『アイデア』366号／美術手帖2015/6）。*
*更新：2026-06-17（続17）。**inv-steyerl** ☑ 文案＋草稿反映（Post T.V. 節末 `####`）。*
*更新：2026-06-17（続16）。**inv-piajp** タスク追加（日本のポストインターネットアート受容——『アイデア』2014/9・美術手帖2015/6）。*
*更新：2026-06-17（続15）。**cari-inv** ☑ 完了判定（§8 残3件・PC Music 日付は任意）。次の1手＝**inv-frkwys**。*
*更新：2026-06-17。**ed-5** ☑（r/AestheticWiki）。**meta-1**／**meta-2** タスク化。rev-10 追記（Still Life/DREAM JOURNAL）反映。*
*更新：2026-06-11。**ed-2** ☑ 序文反映。**concl-1**・**ed-4** ☑。*
*更新：2026-06-22。手順書第1弾——完了タスク詳細をサマリー化（未完了 ### 節は維持）。*
