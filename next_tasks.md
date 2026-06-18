# 次のタスク

**正本**：[`草稿.md`](./草稿.md)  
**論点バックログ**：[`草稿_レビュー論点メモ.md`](./草稿_レビュー論点メモ.md)（2026-06-02 同期済）  
**編集方針**：[`編集方針.md`](./編集方針.md)（政治化・日本語圏射程・seapunk 読み道）

**次にやる1件**：**inv-vektroid**／**src-1**／**ed-3**／**ed-6**（並行可）。後回し：**meta-1**／**meta-2**

**使い方**

1. 下記 **§アクティブ・パイプライン** で依存関係を確認  
2. **§タスク索引** から ID を選び、該当セクション（rev／src／cari／concl／ed）の手順に従う  
3. 完了時に ☐→☑、[`草稿_推敲メモ.md`](./草稿_推敲メモ.md) に改稿ログ  

**作業の型**（3層を混同しない）

| 層 | 意味 | 例 |
|---|---|---|
| **調査** | ノートに事実を溜める。正文を止めない | `cari-inv`、`rev-7` 調査段階 |
| **文案** | 反映用段落を別ファイルに書く | `第2章取込_*_文案.md` |
| **反映** | [`草稿.md`](./草稿.md) へ貼り付け・分割稿同期 | rev-7 反映、cari-draft |

1. 調査ノート／[`草稿_ファクト補強調査.md`](./草稿_ファクト補強調査.md) から候補を選ぶ  
2. **文案ファイル**を作成  
3. 草稿に反映 → 目視照合  
4. 本ファイル・分割稿のステータスを更新  
5. 反映済み文案は [`archive/`](./archive/) へ  

---

## アクティブ・パイプライン（2026-06-02 時点）

**第2章・PC Music 系の土台づくり → 第5章 CARI 接続 → 結論**

```
rev-7（ed-1）政治化 ─────────────────────────┐
                                              ├→ rev-4 / rev-8 / rev-9（並行可）
src-2 SuperSuper! ──→ src-5 vaporwave前史（HIT）──→ src-4 ハイパーポップ ──┤
                                              ↓
                         cari-draft（第5章 1段落＋Facebook 補強）
                                              ↓
                         concl-1（Guardian 問い・クロニクル末尾）→ ed-4（後記・Cook／歴史化）

cari-inv ☑（§8 残3件は任意）──── 草稿反映のブロッカーではない
ed-3 seapunk 読み道整備 ────── 第2章・単独可（圧縮以外の案A〜E）
meta-1 執筆動機ツイート ────── 序文 or 後記・単独可
meta-2 振り返りパート新設 ──── 草稿**末尾**・単独可（優先度低・最後に）
meta-3 遡行的確定・本稿の自己言及 ─ 後記追記・単独可（meta-1 後推奨）
```

**Guardian 2016 は2種類**（混同注意）

| 記事 | タスク | 行先 |
|---|---|---|
| Leigh Alexander・Y2K aesthetic（2016-05-19） | cari-inv／cari-draft／concl-1 | 第5章 CARI・結論 |
| Michael Hann・fashwave（2016-12-14） | rev-7（ed-1） | 第2章 Harper 節後 |

---

## タスク索引（未完了）

凡例：☐ 未着手／進行中　☑ 完了　— 任意・低優先

### 最優先（今週）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **rev-7** | 2016 vaporwave 政治化（コミュニティの応答） | ☑ | — | [`vaporwave政治化_調査ノート.md`](./vaporwave政治化_調査ノート.md) → [`第2章取込_vaporwave政治化_文案.md`](./第2章取込_vaporwave政治化_文案.md) |
| **ed-1** | 編集方針 §1 政治化 | ☑ | rev-7 と同一 | 上記（2026-06-02 反映） |

### 第2章・外部ノート（rev-7 後 or 並行）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **src-2** | SuperSuper! Magazine 追記 | ☑ | rev-7 後推奨 | [`supersuper.md`](./supersuper.md) → [`第2章取込_SuperSuper_文案.md`](./第2章取込_SuperSuper_文案.md) |
| **src-5** | vaporwave前史見直し（Hippos In Tanks） | ☑ | **src-2 直後** | [`HipposInTanks_調査ノート.md`](./HipposInTanks_調査ノート.md) → [`第2章取込_vaporwave前史_文案.md`](./第2章取込_vaporwave前史_文案.md) |
| **src-6a** | MP3ブログ調査ノート——仕分け確定 | ☑ | §1–§19 確定済 | [`src-6_仕分け.md`](./src-6_仕分け.md) |
| **src-6b** | 第2章・前史（§2・§3・§6） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_mp3blog前史_文案.md`](./第2章取込_mp3blog前史_文案.md) |
| **src-6c** | 第1章・プラットフォーム（§1 mp3ブログ・§17 MySpace・§18 Tumblr補強） | ☑ | 草稿反映済（2026-06-16） | [`第1章取込_プラットフォーム_文案.md`](./第1章取込_プラットフォーム_文案.md) |
| **src-6d** | 第2章・命名系譜（§12–§13） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_命名系譜_文案.md`](./第2章取込_命名系譜_文案.md) |
| **src-6e** | 第2章・アーキテクチャ総括（§10） | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_アーキテクチャ総括_文案.md`](./第2章取込_アーキテクチャ総括_文案.md) |
| **src-6f** | 匿名性（§7）——rev-9 と統合 | ☑ | 草稿反映済（2026-06-16）。「匿名性の美学」主題化＋後記 callback | [`第2章取込_witchhouse匿名性_文案.md`](./第2章取込_witchhouse匿名性_文案.md) |
| **inv-vektroid** | Vektroid名義増殖——調査（src-6f 派生） | ☐ | 並行可。正文は書かない | 調査のみ → [`src-6_仕分け.md`](./src-6_仕分け.md) スレッドB |
| **inv-msv** | Mater Suspiria Vision / Cosmotropia de Xam / AAVV 調査 | ☑ | 並行可 | 調査＋草稿反映済（2026-06-17）。第2章に「Post T.V.」節を新設 → [`第2章取込_lofi映像Post-TV_文案.md`](./第2章取込_lofi映像Post-TV_文案.md)／§5.4 |
| **inv-swan** | Daniel Swan の軌跡（lo-fi→HD美学・PC Music・Ecco2k） | ☐ | 並行可。Post TV 文案で起点に言及済 | Lux Laze(2010)→DIS Mag 2012→Jam City/Dux Content/Lifesim→Ecco2k「GT-R」(2017)。下記詳細節 |
| **inv-dclub** | Night Slugs / Fade To Mind（deconstructed club・HD美学）と PC Music の応答 | ☑ | 並行可。草稿反映済（2026-06-17） | [`第2章取込_deconstructedclub_文案.md`](./第2章取込_deconstructedclub_文案.md)（PC Music 節の後に「並走」節）。下記詳細節 |
| **inv-steyerl** | Hito Steyerl「貧しいイメージの擁護（In Defense of the Poor Image）」節の追加 | ☑ | Post T.V. 節反映済（2026-06-17） | [`第2章取込_steyerl_文案.md`](./第2章取込_steyerl_文案.md)（Post T.V. 節末 `####`）。下記詳細節 |
| **inv-piajp** | 日本のポストインターネットアート受容——雑誌特集の簡単な紹介節 | ☑ | 草稿反映済（2026-06-17） | [`第1章取込_piajp_文案.md`](./第1章取込_piajp_文案.md)（第1章・Designing Tumblr 直後）。下記詳細節 |
| **inv-tabor** | Tabor Robak ネットワーク整理・BrandNewPaintJob.exe（Jon Rafman との共作） | ☐ | 並行可 | [taborrobak.com](https://www.taborrobak.com/) / 草稿 L318・L439・L598・L994 既出 |
| **inv-oesb** | OESB（Todd Ledford）× OPN「Time Decanted」MV 接点 | ☑ | 草稿反映済（2026-06-17） | [Vimeo](https://vimeo.com/7616034) / 草稿 L314 |
| **inv-frkwys** | FRKWYS Vol.7（RVNG Intl.）——Ferraro・OPN・Laurel Halo 同席の記録 | ☑ | 草稿反映済（2026-06-17） | [Discogs](https://www.discogs.com/ja/master/353721-Borden-Ferraro-Godin-Halo-Lopatin-FRKWYS-7-) / 2011年7月 |
| **src-4** | ハイパーポップの歴史（PC Music 2013–2016 厚み） | ☑ | src-2 後（src-5 と並行可） | [`ハイパーポップの歴史.md`](./ハイパーポップの歴史.md) → `第2章取込_ハイパーポップ_文案.md` |
| **src-1** | musicplusghost 洗い出し | ☐ | 並行可 | [`musicplusghost.md`](./musicplusghost.md) |
| **src-3** | r/witchhouse 歴史スレ参照 | ☑ | rev-9 と重複なし | `#### コミュニティの正史` 末尾1文+URL（2026-06-17 反映済） |
| **rev-8** | Eccojams vs Far Side Virtual | ☑ | 草稿反映済（2026-06-16） | [`第2章取込_FSV対比_文案.md`](./第2章取込_FSV対比_文案.md) |
| **rev-9** | witch house 匿名性 | ☑ | src-6f に統合済（2026-06-16） | [`第2章取込_witchhouse匿名性_文案.md`](./第2章取込_witchhouse匿名性_文案.md) |
| **rev-4** | ムードボード対比 | ☐ | 並行可 | `第1章取込_ムードボード対比_文案.md` |
| **ed-3** | seapunk 読み道整備（節頭地図等・圧縮以外） | ☐ | 並行可 | [`編集方針.md`](./編集方針.md) §3 |

### 第5章・CARI・結論（第2章土台の後）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **cari-inv** | CARI 調査（§8 要確認・Global Village 等） | ☑ | — | [`CARI_調査ノート.md`](./CARI_調査ノート.md)。2026-06-17 完了判定：DV-i ☑、Shenzhen Miracle ☑、GVC ☑。§8 残3件（Collins URL・トレーラー照合・Terrell Davis）は**任意** |
| **cari-draft** | CARI 草稿反映（Guardian・Neo-Y2K 1段落、Facebook 補強） | ☑ | **src-2＋src-4 後** | 同上 → `第5章取込_CARI_文案.md` |
| **concl-1** | Guardian 2016 結論の時代診断問いかけ（ユーザー改稿・案A） | ☑ | cari-draft ☑ | [`第5章取込_結論_Guardian問いかけ_文案.md`](./第5章取込_結論_Guardian問いかけ_文案.md) |
| **ed-2** | 日本語圏は射程外（1〜3文） | ☑ | 単独可 | [`序文取込_ed2_日本語圏射程_文案.md`](./序文取込_ed2_日本語圏射程_文案.md) |
| **ed-6** | 序文——「インターネット美学」と「制度化」の説明節 | ☐ | 単独可 | [`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) → 下記詳細節 |
| **ed-4** | 本稿の制度化・Cook 歴史化・著者の不确定性（後記） | ☑ | concl-1 と同批 | [`後記取込_制度化ループ_文案.md`](./後記取込_制度化ループ_文案.md) |
| **ed-5** | r/AestheticWiki 制度化追記（what aesthetic is this?） | ☑ | 単独可 | 第5章「分類する欲望」節（2026-06-17 反映済） |

### メタ・著者性（meta-*）

| ID | 内容 | 状態 | 依存 | 正本・文案 |
|---|---|---|---|---|
| **meta-1** | 執筆動機ツイート追記 | ☐ | 単独可 | 序文 or 後記。後記の自己言及群を具体化 |
| **meta-2** | 振り返りパート新設 | ☐ | 単独可。**優先度低・最後** | [`草稿.md`](./草稿.md) **末尾**（新 `##` 節）。11万字の定期的振り返り |
| **meta-3** | 遡行的確定——本稿が行っていることの自己言及（後記追記） | ☐ | 単独可。**meta-1 後推奨** | 下記詳細節。Frutiger Aero 節・ed-4 後記との接続 |

### 第4章・その他

| ID | 内容 | 状態 | 依存 | 備考 |
|---|---|---|---|---|
| **rev-10** | Jon Rafman 9 Eyes → liminal 前史 | ☑ | 草稿反映済（2026-06-16–17） | 第4章。9 Eyes＋Still Life/DREAM JOURNAL＋Ch2 協働接続 |
| **rev-12** | Caretaker × liminal／Backrooms | ☐ 先送り | rev-10 関連 | 第4章 |
| — | 8番出口と liminal space 美学 | 判断待ち | — | 第4章追加可否 |
| — | 第5章 Frutiger Aero 節との整合 | 任意 | cari-draft 後でも可 | 境界論・第2章フェーズ2 |
| — | 第4章 L640 TikTok/Discord 文案 B | 任意 | — | §8 残 |
| — | KYM 訂正ログ（ファクト補強調査） | 任意 | — | §8 残 |
| — | Google Trends（aesthetic） | 任意 | — | §9-man 追補 |
| — | ブロック F →「確定」 | 任意 | — | ファクト補強 §9 |

### Seapunk 後続・第2章残（任意）

| ID | 内容 | 状態 | 備考 |
|---|---|---|---|
| **6b-reorg 後続** | M.I.A.・Tim and Eric（激怒記事直後） | ☐ | 除外箱 L80 |
| **6b-reorg 後続** | H∆SHTAG$ ep5 厚み（seapunk 節） | — 任意 | aesthetic 6c-2 ☑ |
| **6c 残** | L254 接続文・年表順の整理 | ☐ | Cluster Mag 直後 |
| **6d-review 残** | 分量・時系列、seapunk 節との接続 | ☐ | witch house 節 |
| **6b 残** | 文案メタ混入チェック、VICE 年表著者明示 | ☐ | 完了済み節の品質確認 |

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
| **6a** | Seapunk 調査ノート——影響評価（統合しない） | ☑ | [`Seapunk調査_取り込み計画.md`](./Seapunk調査_取り込み計画.md)（6b〜6f 実行済） |
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
| **§9-man** | [`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md)——草稿反映 | ☑ | §9 文案に統合反映 |

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

正本：[`草稿_レビュー論点メモ.md`](./草稿_レビュー論点メモ.md) §13。§9・6d-review 完了後の改稿バックログ。

| ID | 内容 | 状態 | 文案（案） |
|---|---|---|---|
| rev-11 | L564 未完成文・L512 要検証 | ☑ | 推敲メモ 続39 |
| rev-1 | 第1章 Reblorg 節 | ☑ | `第1章取込_Reblorg_文案.md` |
| rev-2 | Internet Archaeology＋One Terabyte | ☑ | `第1章取込_GeoCities土壌_文案.md` |
| rev-3 | dump.fm／Jogging／流れ2 | ☑ | 上記に統合 |
| rev-4 | ムードボード対比 | ☐ | `第1章取込_ムードボード対比_文案.md` |
| rev-5 | Megazord 修正 | ☑ | `第1章取込_Megazord_文案.md` |
| rev-6 | aesthetic 大仰さ総括 | ☑ | `第2章取込_aesthetic大仰さ_文案.md` |
| rev-7 | 三読み＋2016 政治化 | ☑ | 文案・草稿反映（2026-06-02）。推敲メモ 続45 |
| rev-8 | Eccojams vs FSV | ☑ | [`第2章取込_FSV対比_文案.md`](./第2章取込_FSV対比_文案.md)（2026-06-16 反映済） |
| rev-9 | witch house 匿名性 | ☑ | src-6f に統合・反映済（2026-06-16）。[`第2章取込_witchhouse匿名性_文案.md`](./第2章取込_witchhouse匿名性_文案.md) |
| rev-10 | 9 Eyes → liminal | ☑ | 草稿・分割稿反映済（2026-06-16–17）。9 Eyes＋Still Life/DREAM JOURNAL＋Ch2 協働接続。文案なし（直書き） |
| rev-12 | Caretaker × liminal／Backrooms | ☐ 先送り | 上記「第4章 Caretaker×liminal」と同一 |

**推奨着手順（2026-06-17 以降）**：**inv-steyerl**／**inv-piajp** ☑ → inv-vektroid／src-1／ed-3（並行可）。**meta-1**／**meta-2** は後回し（meta-2 は草稿末尾・最後）

### rev-7 進捗——**完了（2026-06-02 拡張反映）**

| 段階 | 状態 | 成果物 |
|---|---|---|
| 調査 | ☑ | [`vaporwave政治化_調査ノート.md`](./vaporwave政治化_調査ノート.md) §4-(a) 含む。Guardian・BuzzFeed Wayback ☑。McLeod 2018 MD ☑ |
| 要確認（残） | 任意 | obakeweb／togetter、Boriswave（脚注向き）。r/vaporwave 声明・weaponized nostalgia は打ち切り ☒ |
| 文案 | ☑ | [`第2章取込_vaporwave政治化_文案.md`](./第2章取込_vaporwave政治化_文案.md)（2026-06-02 拡張版） |
| 草稿反映 | ☑ | DMY 節 **L426–452**：英語圏政治化＋@ccchristtt＋**日本語圏 2017–2019**（L449–452）。L454「話を戻そう。」→ distroid |
| 分割稿 | ☑ | [`第2章_命名の時代.md`](./第2章_命名の時代.md) DMY 節同期（2026-06-02） |

**調査ノートの核**：Parker・Ten S. ☑／@ccchristtt ☑（L447）／木澤・現代ビジネス・捨て垢／Local Visions・さやわか ☑（§4-(a)）／Boriswave 任意未反映。

**ed-2 との住み分け**：L449–452 は「英語圏批評語彙と 2016 政治化が日本語圏でいつ・どう結びつけられたか」の**受容の橋**（記録）。編集方針 §2 の「日本語圏独自系譜（カオスラウンジ・especia 等）は射程外」——**ed-2 ☑**（序文 L13 直後、2026-06-11）。

**rev-7 §6 残・確認用 URL**（2026-06-02 更新）

| 状態 | 確認したいこと | URL／ローカル正本 |
|---|---|---|
| ☑ | @ccchristtt ツイート（2017-11-27） | https://twitter.com/ccchristtt/status/934884934187212800 → §3-3 |
| ☑ | Whelan & Nowak 2018 | [`Vaporwave Is (Not) a Critique...md`](./Vaporwave%20Is%20(Not)%20a%20Critique%20of%20Capitalism_Genre%20Work%20in%20An%20Online%20Music%20Scene.md) |
| ☑ | Vice fashwave（Iadarola、2016-12-14） | https://www.vice.com/en/article/fashwave-neo-nazi-music/ |
| ☑ | McLeod 2018 PDF＋MD | [`Vaporwave_Politics_Protest_and_Identity.md`](./Vaporwave_Politics_Protest_and_Identity.md) |
| ☑ | ykic ノート転記 | [`note_極右の世界のBGM.md`](./note_極右の世界のBGM.md) |
| ☒ | r/vaporwave 声明 | **未発見**（URL 特定不可。Wayback でも公式声明なし） |
| ☒ | Sleep ∞ Over「weaponized nostalgia」 | Vice 2017-01 経由の THUMP 引用のみ。SoundCloud・全文検索でフレーズ未確認 |
| ☑ | 日本語圏 2019（木澤・現代ビジネス・ykic 等） | 草稿 L449–452／調査ノート §4-(a) |
| ☑ | Mal d'archive・Chocolat・仲山ひふみ（sensualempire） | 草稿 L449–451 |
| ☑ | Local Visions／捨て垢（@sute_aca_） | 草稿 L451 |
| ☐ | obakeweb／togetter | 調査ノート §6 |
| ☐ | Boriswave（任意） | New Statesman 2019-11 |

**確認済み（§6）**：Guardian・BuzzFeed fashwave、[Rave News](https://www.ravenews.ca/en/read/2016/february/09/)、[Vice 2017-01 trumpwave](https://www.vice.com/en/article/trumpwave-fashwave-far-right-appropriation-vaporwave-synthwave/)、[gendai.media](https://gendai.media/articles/-/59738)

---

## 外部調査ノート由来（src-*）

| ID | 内容 | 状態 | 文案（案） | 依存 |
|---|---|---|---|---|
| src-1 | musicplusghost 洗い出し | ☐ | `第2章取込_musicplusghost_文案.md` | 並行可 |
| src-2 | SuperSuper! Magazine 追記 | ☑ | [`第2章取込_SuperSuper_文案.md`](./第2章取込_SuperSuper_文案.md) | 草稿・分割稿反映済（2026-06-11） |
| src-5 | vaporwave前史見直し（Hippos In Tanks） | ☑ | [`第2章取込_vaporwave前史_文案.md`](./第2章取込_vaporwave前史_文案.md) | コア反映・分割稿同期（2026-06-11） |
| src-6a–f | MP3ブログ調査ノート——仕分けと段階取込 | ☑ | [`src-6_仕分け.md`](./src-6_仕分け.md) → 章別文案 | 6a–6f 完了（2026-06-16） |
| src-3 | r/witchhouse 歴史スレ参照 | ☑ | 草稿・分割稿反映済（2026-06-17）。`#### コミュニティの正史` 末尾に1文+URL | rev-9 と重複注意 |
| src-4 | ハイパーポップの歴史（PC Music 厚み） | ☑ | `第2章取込_ハイパーポップ_文案.md` | src-2 後（src-5 と並行可。cari-draft の前提） |

### src-1. musicplusghost.md——参考箇所の洗い出し

**背景**  
平山悠編『MUSIC + GHOST : FEECO Magazine extra issue』（憑在論・Ghost Box・英国郊区派）。草稿 `#### 憑在論と郷愁の言語`（L173）で ZINE 名と [atochietebura リンク](https://atochietebura.com/HD/h024.html) は**既出**。本タスクは全文（[`musicplusghost.md`](./musicplusghost.md)）から**追記に値する箇所を選別**する。

**洗い出し候補（優先度順）**

| 調査ノート § | 内容 | 草稿の行先候補 |
|---|---|---|
| 序文・Ch1 Twisted Memories | Ghost Box／郊区派 hauntology（Burial 偏重の補正） | 憑在論小節 L173 付近 |
| Ch2 Memory Digger | Jim Jupp（Ghost Box）インタビュー | 同上 or witch house 前史 |
| Ch5 Beyond the Dead Future | 90年代後半ビデオゲーム再読 | vaporwave 前史・Megazord 文脈 |
| Extra / Ch6 | 日本の憑在論受容・個人的郷愁の限界 | 憑在論小節（短い注記に留めるか判断） |

**手順**

1. [`musicplusghost.md`](./musicplusghost.md) を章単位で読み、上表に**採用／保留／射程外**を付ける  
2. 採用候補ごとに公開 URL・部分引用を文案に整理（正文は URL のみ）  
3. [`草稿.md`](./草稿.md) 反映 → 分割稿同期  

**注意**：FEECO 誌面の長文引用は避け、既出の MUSIC+GHOST 言及と**重複しない**範囲で足す。

---

### src-2. supersuper.md——SuperSuper! Magazine 追記——**完了（2026-06-11）**

**背景**  
[`supersuper.md`](./supersuper.md) は 2006 nu rave 創刊から 2012 slimepunk までの号別記録・PC Music 前史・witch-house.com タイムライン対応表を整理済み。2026-06-02 に初回反映（続50）後、2026-06-11 に構成改稿を完了した。

**草稿反映済み（正本行番号）**

| 節 | 草稿行 | 内容 |
|---|---|---|
| `## SuperSuper! Magazineという記録媒体` | L324–344 | Vol 1 #22、Vol 2 連続、slimepunk＋NYT 同時期、Dux Content 予告、MASSAGE 9 対比（メタ文維持） |
| `## seapunkの死と遺産` | L348–387 | `### seapunkの「死」`／`### seapunk と vaporwave` 小見出し化。激怒→擁護順。NYT「再び引き合い」削除→8か月前の時間のずれ。r/vaporwave を擁護記事直後へ。遺産節から MASSAGE 誌面構造長文を削除 |
| `## PC Musicという継承` | L534–548 | Polly Salmon＝GFOTY、Hannah Diamond（Loud and Quiet）、Roy／Novatel Allegro、SoundCloud ミックス URL |

**成果物**

- 文案：[`第2章取込_SuperSuper_文案.md`](./第2章取込_SuperSuper_文案.md)
- 分割稿：[`第2章_命名の時代.md`](./第2章_命名の時代.md)（2026-06-11 同期）
- 推敲ログ：[`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 続50・続51

**残作業（src-2 外）**

- [`草稿.md`](./草稿.md) `## vaporwaveという名前以前に`（GATEKEEPER／HIT 等）の節見直し・HIT カタログ補強 → **src-5**
- PC Music 節の Polly 時制・Dux Content 二重記述の圧縮 → 任意（src-4 と重複整理時）

---

### src-5. vaporwave前史見直し——Hippos In Tanks——**完了（2026-06-11）**

**背景**  
[`HipposInTanks_調査ノート.md`](./HipposInTanks_調査ノート.md) に基づき、草稿 `## vaporwaveという名前以前に` の GATEKEEPER／HIT ブロックを改稿した。

**反映済み（草稿 L239–249）**

| ブロック | 内容 |
|---|---|
| Giza（作品） | Merok EP、Thunder Horse MV（Web 公開）。HIT 不出 |
| HIT（レーベル） | 設立・Sony RED・Fact 2011、Fader／Impose 引用、Giza VHS を典型例として1回のみ |
| HIT カタログ | Games EP、Megazord アートワーク、Ford & Lopatin 改名 |
| 2008 ネットワーク | 20jazzfunkgreats、MySpace（witch house 節への前方参照） |

**成果物**

- 文案：[`第2章取込_vaporwave前史_文案.md`](./第2章取込_vaporwave前史_文案.md)
- 分割稿：[`第2章_命名の時代.md`](./第2章_命名の時代.md)（2026-06-11 同期）
- 推敲ログ：続52・続53

**他タスクへ譲渡（src-5 外）**

| 項目 | 譲渡先 |
|---|---|
| *Condo Pets*／*Far Side Virtual* | rev-8 |
| Arca *&&&&&*／Grimes *Darkbloom* | 第4章・src-4 |
| Yung Lean *Warlord* 無断リリース | 第4章 cloud rap 節 |
| Gatekeeper *Exo*／Nguzunguzu | src-6 §14 or 第4章（[`src-6_仕分け.md`](./src-6_仕分け.md) 委譲表） |

---

### src-6. MP3ブログ時代とエクスペリメンタル・シーン——段階取込

**正本（仕分け・フェーズ）**：[`src-6_仕分け.md`](./src-6_仕分け.md)  
**調査資料**：[`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](./MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md)

第1章〜第2章にまたがる19節＋スレッド3本。**1文案にまとめられない**ため Seapunk 6a 型で段階化。

| ID | 内容 | 状態 |
|---|---|---|
| **src-6a** | 仕分け確定（§1–§19、委譲表、スレッドA/B/C） | ☑ |
| **src-6b** | 第2章・前史 §2・§3・§6（Block A はおさらい化） | ☑ 草稿反映済 → [`第2章取込_mp3blog前史_文案.md`](./第2章取込_mp3blog前史_文案.md) |
| **src-6c** | 第1章・プラットフォーム §1 mp3ブログ／§17 MySpace／§18 Tumblr補強 | ☑ 草稿反映済 → [`第1章取込_プラットフォーム_文案.md`](./第1章取込_プラットフォーム_文案.md) |
| **src-6d** | 第2章・命名系譜 §12–§13 | ☑ 草稿反映済 → [`第2章取込_命名系譜_文案.md`](./第2章取込_命名系譜_文案.md) |
| **src-6e** | 第2章・アーキテクチャ §10 | ☑ 草稿反映済（2026-06-16） |
| **src-6f** | 匿名性 §7 → **rev-9** と統合 | ☑ 草稿反映済（2026-06-16） |

**役割分担（2026-06-15）**：§1 mp3ブログ**一般**は第1章の新設節（6c）へ移設。第2章 Block A（6b）は「第1章で見た mp3ブログ」の**おさらい**＋20jfg・Tri Angle に絞る。第1章は mp3ブログ節と MySpace 節を**別立て**。

**src-5 との重複**：§4 HIT・§16 *Young Chronos* は **射程外**（src-5 ☑）。§14 *Exo* は第4章 or 第1章 L91。詳細は仕分け表の委譲表。

**手順**（各フェーズ共通）

1. [`src-6_仕分け.md`](./src-6_仕分け.md) で対象節・行先・第1章 節構成案を確認  
2. 文案 `第*章取込_*_文案.md` を作成  
3. [`草稿.md`](./草稿.md) 反映 → 分割稿同期 → 推敲メモ  
4. 仕分け表の「文案／草稿反映」列と本ファイル索引を ☑ 更新  

**次の1手**：src-6 全フェーズ（6a–6f）完了（2026-06-16）。rev-9 も統合済。残る並行タスク＝rev-8（FSV）・inv-vektroid・src-1・src-3 など。

---

### inv-vektroid. Vektroidの名義増殖とシーン形成——調査（src-6f 派生）

**背景**  
[`src-6_仕分け.md`](./src-6_仕分け.md) スレッドBで浮上した仮説：Vektroid（Ramona Andra Xavier）が2011年に複数名義で短期間に大量リリースしたことが、外部から「複数アーティストによるシーン」のように映り、vaporwave の認知・定着を後押しした可能性。

**調査事項**

- Vektroid 2011 各名義のリリース時期・本数（Bandcamp・Discogs・Wayback）
- 当時のフォーラム等で「同一人物」と認識されていたかの記録
- Beer on the Rug カタログにおける名義の並び（src-6b §3 と関連）
- 既存 Seapunk／vaporwave政治化ノートへの関連記述

**ステータス**：調査のみ。**正文は書かない**。

**手順**

1. 調査結果をノートにまとめる（`Vektroid_調査ノート.md` または既存追記）  
2. 結果を [`src-6_仕分け.md`](./src-6_仕分け.md) スレッドB／6b（L254）へ還流  
3. 裏付けなしの場合は Vektroid 2名義併記への軽い接続のみ残す

---

### inv-msv. Mater Suspiria Vision（Cosmotropia de Xam）/ AAVV——調査

**背景**  
草稿 L239 は **Phantasma Disques**（Mater Suspiria Vision 関連）を witch house レーベルのひとつとして挙げている。その Mater Suspiria Vision のビジュアル担当が **Cosmotropia de Xam**（CDX）であり、ローマを拠点とする DVD-r / VHS レーベル **[AAVV](https://vimeo.com/aavv)**（[Discogs](https://www.discogs.com/ja/label/235050-AAVV)）から *Visual Ecstasy*（AAVV 003）をリリースしている。同レーベルには **Luke Wyatt**（Torn Hawk）の *Sad Stonewash — A Video Mulch*（AAVV 004）もある。Wyatt は VCR を物理的に破損させ再デジタル化する「Video Mulch」技法を用いており、手法はローファイだが、その立ち位置は witch house より vaporwave・ポストインターネットアート寄りに近い。音楽名義 Torn Hawk の作品（*UNION & RETURN* など）は HD 美学に接近する側面もあり、lo-fi 技法と HD 感覚の混在がある。AAVV での CDX との並置は偶発的な接触かもしれず、witch house と直接結びつけることには注意が必要。  

**参照 URL**  
- [AAVV Vimeo](https://vimeo.com/aavv)  
- [AAVV ウェブアーカイブ（2011年）](https://web.archive.org/web/20111005003242/http://www.aavv-videos.com/)  
- [AAVV Discogs レーベルページ](https://www.discogs.com/ja/label/235050-AAVV)  
- [Cosmotropia de Xam ブログ](https://cosmotropia-de-xam.blogspot.com/)  

**調査事項**

- Cosmotropia de Xam の活動概要と Mater Suspiria Vision との関係（制作クレジット確認）
- AAVV のレーベル性格——witch house ビジュアル系との接点、欧州側の物理メディア流通
- Luke Wyatt（Torn Hawk）の立ち位置：vaporwave・ポストインターネットアート寄り。「Video Mulch」技法（VHS ローファイ）と Torn Hawk 音楽の HD 美学的側面（*UNION & RETURN* など）の関係を整理
- Phantasma Disques と AAVV の関係（同一人物 or 別個のネットワーク）
- 草稿接続候補：Cosmotropia de Xam は L226「VHS の劣化・コラージュ」節 or L239 Phantasma Disques 付近。Luke Wyatt は草稿の lo-fi vs HD の軸（src-6e §15 由来）や vaporwave 前史との接続を検討。GATEKEEPER VHS（L310）との照合は限定的に

**ステータス**：☑ 調査＋草稿反映完了（2026-06-17）。[`witchhouse-chillwave調査メモ.md`](./witchhouse-chillwave調査メモ.md) §5.4 追記。**草稿反映済**：[`第2章取込_lofi映像Post-TV_文案.md`](./第2章取込_lofi映像Post-TV_文案.md) を `### 「Post T.V.」——lo-fi映像というシーン` として第2章 GATEKEEPER 節末・vaporwave 節の前に挿入（草稿.md・[`第2章_命名の時代.md`](./第2章_命名の時代.md) 同期済）。派生：inv-swan / inv-dclub。

**手順**

1. AAVV アーカイブ・Discogs・Cosmotropia ブログを確認し、[`witchhouse-chillwave調査メモ.md`](./witchhouse-chillwave調査メモ.md) §5.4 にまとめる
2. 草稿の既述箇所との重複・接続可能性を評価
3. 接続できる場合のみ文案を作成し、タスクを `src-` に格上げ

---

### inv-swan. Daniel Swan——lo-fi から HD 美学への軌跡

**背景**  
Daniel Swan は inv-msv で扱う「Post T.V. - Lo-Fi For The Eyes」（2010, ローマ国際映画祭）の参加者の一人。出発点は lo-fi 寄りで、2010年の短編映画『[Lux Laze](https://u-t-t-e-r.bandcamp.com/album/lux-laze)』は全編 VHS 撮影、サウンドトラックを **Jack Latham（Jam City）** が担当し、VHS＋コミック＋DVD-R のセット＋50本限定カセットという物理形態で自主リリースされた。その後 Swan は高精細・CGI 寄りの HD 美学へ転回し、PC Music 周辺の主要な映像作家になる。Post-TV 文案（[`第2章取込_lofi映像Post-TV_文案.md`](./第2章取込_lofi映像Post-TV_文案.md)）では「転回の起点」として軽く前振りするにとどめ、軌跡の本格的整理はここで行う。

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

### inv-dclub. Night Slugs / Fade To Mind——deconstructed club・HD 美学と PC Music の応答

**背景**  
草稿は **Night Slugs / Fade To Mind** 勢にたびたび触れるが、まとまった記述がない。両レーベルは HD 美学を引き継ぎつつ **deconstructed club** を推し進めた点で重要。**Jam City（Jack Latham）**『[Classical Curves](https://nightslugs.net/releases/nslp002-jam-city-classical-curves/)』（2012, Night Slugs）は deconstructed club の起点とされ（[Wikipedia](https://en.wikipedia.org/wiki/Classical_Curves)）、artifice・富・テクノロジーを主題にした高光沢のサウンドデザインを持つ。Fade To Mind 側では **Fatima Al Qadiri**（草稿に Vatican Vibes MV 等で既出）が関与する **Future Brown**（Fatima Al Qadiri / Nguzunguzu の Asma Maroof・Daniel Pineda / J-Cush）の「**Vernáculo」feat. Maluca** MV が、Pérez Art Museum Miami 委嘱の**架空の美容ブランド広告**（L'Oréal・Revlon の広告言語を流用した "capitalist surrealism"、カバーアートは **DIS Magazine**）として制作された（[The FADER](https://www.thefader.com/2014/12/17/watch-future-browns-dewy-vernaculo-video)）。これは PC Music 的なハイパー消費の美学に対する deconstructed club 側からの応答とも読める。

**論点**  
- PC Music（ハイパーポップ）と deconstructed club を「ハイパー消費・広告美学・HD 仕上げ」という共通基盤で並べ、応答関係として書けるか。書き方は検討中（独立節 or PC Music 節への補足）。
- Fatima Al Qadiri を介して既出ネットワーク（Vatican Vibes、Tabor Robak、Shanzhai Biennial、GCC、DIS Magazine）と接続。
- Daniel Swan（inv-swan）が Jam City の MV を手がけている点で両タスクは連結。

**参照 URL**  
- [Night Slugs NSLP002 – Classical Curves](https://nightslugs.net/releases/nslp002-jam-city-classical-curves/)
- [Future Brown「Vernáculo」MV（The FADER）](https://www.thefader.com/2014/12/17/watch-future-browns-dewy-vernaculo-video)
- [Future Brown インタビュー（The Quietus）](https://thequietus.com/interviews/future-brown-interview/)
- [Aesthetic: Future Brown（Crack Magazine）](https://crackmagazine.net/article/aesthetic/aesthetic-future-brown/)

**ステータス**：☑ 草稿反映完了（2026-06-17）。[`第2章取込_deconstructedclub_文案.md`](./第2章取込_deconstructedclub_文案.md) を `## deconstructed clubという並走` として PC Music 節の後・章末総括の前に挿入（`####` 4小節：Night Slugs / Future Brown / Daniel Swan / IDL 補遺）。草稿.md・[`第2章_命名の時代.md`](./第2章_命名の時代.md) 同期済。派生：inv-swan（Daniel Swan 軌跡の本格整理は別途）。

---

### inv-steyerl. Hito Steyerl「貧しいイメージの擁護」——節の追加

**背景**  
Hito Steyerl の論考 **「In Defense of the Poor Image」**（2009年、*e-flux journal* #10）は、低解像度・劣化した画像の流通をめぐる批評的テキストとして、本稿が扱う lo-fi 映像／Post T.V. シーン（2010）や、章末総括の lo-fi／高精細の対比と強く接続する。[`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](./MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md) §15 には、同ノートのポストインターネット文脈のひとつとして既に言及があり、Gatekeeper／Robak の「高精細な方向」への傾倒は poor image 論へのある種の応答としても読める、とメモされている。

**論点（節で扱う候補）**

- **poor image（貧しい映像）**：コピー・再圧縮・流通のたびに劣化するネット上の画像。価値の所在が「原作」から「流通・共有の軌跡」へ移る。
- **Post T.V.（2010）との時間的近接**：Steyerl の論考（2009）が lo-fi 映像ブームの制度的認知（Post T.V.）の直前にあり、批評言語としての接続が可能。
- **lo-fi と高精細の対比**：本章の GATEKEEPER／distroid／PC Music 側の「磨き上げ」と、貧しい映像の擁護との緊張関係（応答としての HD 路線）。
- **本稿の射程**：美術史の総論ではなく、第2章のインターネット美学の文脈に必要な範囲で短く紹介する。

**挿入位置（要検討・文案で決定）**

| 候補 | 利点 |
|---|---|
| `### 「Post T.V.」` 節の直後 | lo-fi 映像シーンの理論的アンカーとして自然。Post T.V.（2010）と Steyerl（2009）の時間的近接を活かせる |
| `## アーキテクチャ：この時代の問い` 内（lo-fi／高精細段落の前後） | 章末総括の理論的補強。poor image と高精細路線の対比を明示できる |
| 第1章「ポストインターネットアートという土壌」への短い言及 | 前史として先取り。第2章 Post T.V. への後方参照が必要 |

**参照 URL**

- [In Defense of the Poor Image（e-flux journal #10, November 2009）](https://www.e-flux.com/journal/10/61362/in-defense-of-the-poor-image/)
- 調査メモ：[`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](./MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md) §14・§15

**挿入位置（確定）**

Post T.V. 節末、`#### lo-fi映像という共通の質感` の直後に `#### Hito Steyerl「貧しいイメージの擁護」` を追加（草稿 L375 後）。

**文案・反映**

| 段階 | 状態 | 成果物 |
|---|---|---|
| 文案 | ☑ | [`第2章取込_steyerl_文案.md`](./第2章取込_steyerl_文案.md)（2026-06-17） |
| 草稿反映 | ☑ | Post T.V. 節末 `####` 3段落 |
| 分割稿 | ☑ | [`第2章_命名の時代.md`](./第2章_命名の時代.md) 同期 |

**ステータス**：☑ 文案＋草稿反映済（2026-06-17）。

---

### inv-piajp. 日本のポストインターネットアート受容——雑誌特集の簡単な紹介節

**背景**  
第1章「ポストインターネットアートという土壌」では、2012年の『[Designing Tumblr](https://bnn.co.jp/products/9784861008306)』（古屋蔵人・**高岡謙太郎** 編）が、Jon Rafman や Ryder Ripps らを日本語圏に紹介した記録として既出（草稿 L143）。第2章では佐藤秀彦編『[新蒸気波要点ガイド](https://diskunion.net/dubooks/ct/detail/DUBK237)』所収の**ばるぼら**「Vaporwave年表」「蒸気波大辞典」が aesthetic 語彙の整理として参照されている。Megazord 節では MASSAGE 9（高岡謙太郎 編）も触れている。  
これらと同じ人脈が、やや後の雑誌特集でもポストインターネットアートの受容を担っており、**英語圏の動向が日本語圏でいつ・どう記録されたか**を短く示す節として追加する。編集方針 §2・**ed-2**（日本語圏独自系譜は射程外）との住み分けは、rev-7 L449–452 の「受容の橋」と同型：**日本語圏の独立系譜を追うのではなく、同時代の紹介・対応の記録として触れる**。

**対象資料（2誌）**

| 誌名 | 年月 | 内容 | 関係者 |
|---|---|---|---|
| **『アイデア』** | 2014年9月号 | ポストインターネットアート特集（全体の企画・監修） | **高岡謙太郎**・**ばるぼら** |
| **『美術手帖』** | 2015年6月号 | 特集「ポスト・インターネット用語20」（構成・文） | **高岡謙太郎**・**水野勝仁** |

**各誌の役割（節で書く要点）**

- **『アイデア』2014/9**：草稿でまだ触れていないポストインターネットアーティストの作品が見られる。日本語圏インターネットの受容や、英語圏と**同時代**での対応がわかる資料。
- **『美術手帖』2015/6**：特集としてポストインターネットの簡単な紹介がなされている。「ポスト・インターネット用語20」という構成で、用語・概念の入門的整理が行われている。
- **人脈の連続**：高岡謙太郎（Designing Tumblr 編・MASSAGE 9 編）、ばるぼら（新蒸気波要点ガイド）、水野勝仁（美術手帖）——草稿既出の受容ルートと重なる。

**挿入位置（推奨）**

| 候補 | 利点 |
|---|---|
| **第1章** `## ポストインターネットアートという土壌` 内、Designing Tumblr 段落（L143）の直後 | 日本語圏への輸入の時系列が自然（2012 書籍 → 2014 アイデア → 2015 美術手帖）。章の主題と一致 |
| New Aesthetic 節の前後 | 2014–2015 の雑誌と New Aesthetic（2012）の時間的近接を活かせるが、主題はややずれる |

**論点（節で扱う候補・短く）**

- 2012–2015 にかけて、書籍・雑誌を通じた**断片的だが連続した**日本語圏の受容
- アイデア特集：作品紹介＋同時代の日本語圏の視点（詳細の作家列挙は必要最小限）
- 美術手帖特集：用語20による入門的整理（全20語の列挙は不要、特集の性格だけ示す）
- Designing Tumblr・新蒸気波要点ガイドとの**同一ネットワーク**としての位置づけ（重複説明は避ける）

**調査・文案で確認すること**

- 各号の目次・特集タイトル・掲載作家名の一次確認（手元資料 or 図書館 DB）
- アイデア号で草稿未登場の作家のうち、節で1〜2例だけ触れるか
- 節の分量（`###` 1本か、Designing Tumblr 段落への追記1〜2文＋`###` か）
- ed-2 宣言との矛盾がないか（「記録として触れる」に留める）

**ステータス**：☑ 文案＋草稿反映済（2026-06-17）。

| 段階 | 状態 | 成果物 |
|---|---|---|
| 文案 | ☑ | [`第1章取込_piajp_文案.md`](./第1章取込_piajp_文案.md)（2026-06-17） |
| 草稿反映 | ☑ | 第1章 Designing Tumblr 直後、3段落＋ed-2 住み分け1段落 |
| 分割稿 | ☑ | [`第1章_土壌.md`](./第1章_土壌.md) 同期 |

---

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

### inv-oesb. OESB（Todd Ledford）× OPN「Time Decanted」MV——接点調査

**背景**  
草稿 L314 は **Olde English Spelling Bee（OESB）** を Tri Angle・HIT と並ぶ実験音楽横断レーベルとして言及しているが、OESB 自体の具体的な記述はない。OESB ファウンダーの **Todd Ledford** が OPN の「**Time Decanted**」MV を監督しており（[Vimeo](https://vimeo.com/7616034)）、OPN とレーベル側の人物が映像で直接交わった記録になっている。OPN 作品は OESB からリリースされていないため音源面の接続ではないが、同じ圏の人物が映像で協働した事実として機能する。

**調査事項**

- 「Time Decanted」の制作年・リリース文脈の確認（Vimeo 投稿日・OPN アルバム文脈）
- Todd Ledford / OESB の活動概要（レーベル設立時期・主要リリース）
- 草稿 L314 OESB 言及箇所への接続可能性（1文追加 or 注記レベル）

**正本 URL**  
- [「Time Decanted」Vimeo](https://vimeo.com/7616034)

**ステータス**：☑ 完了（2026-06-17）。草稿 L314 の OESB 言及直後・分割稿に1文追記。

---

### inv-frkwys. FRKWYS Vol.7（RVNG Intl.）——同席の記録

**背景**  
2011年7月17日に **RVNG Intl.** からリリースされた *[FRKWYS Vol. 7](https://www.discogs.com/ja/master/353721-Borden-Ferraro-Godin-Halo-Lopatin-FRKWYS-7-)* は、**David Borden**（Mother Mallard's Portable Masterpiece Co.）、**James Ferraro**、Samuel Godin、**Laurel Halo**、**Daniel Lopatin**（OPN）の5人によるセッション録音盤。2010年8月にブルックリン DUMBO の Atlantic Sound Studios で録音。企画は Lopatin と RVNG が Borden のミニマリスト・シンセ作品への共鳴から立ち上げ、Ferraro・Halo らを加えた。トラック名は "People of the Wind"・"**Internet Gospel**" など。  

草稿 L314 末尾で「Laurel Halo や James Ferraro らの作品が音楽批評の場で注目を集めるようになった」と記しており、まさにその同じ年（2011年）に Ferraro・OPN・Laurel Halo が同じスタジオにいたという具体例になる。RVNG Intl. は現時点で草稿未登場。FRKWYS シリーズのコンセプトは「世代をまたいだ協働（intergenerational collaboration）」——Borden の 1970年代シンセ・ミニマリズムと 2010年代のネット音楽世代の接続という構図でもある。

**参照 URL**  
- [Discogs](https://www.discogs.com/ja/master/353721-Borden-Ferraro-Godin-Halo-Lopatin-FRKWYS-7-)  
- [Pitchfork リリースノート](https://pitchfork.com/news/42880-new-release-borden-ferraro-godin-halo-lopatin-frkwys-vol-7/)  

**調査事項**

- RVNG Intl. のレーベル性格・設立時期（FRKWYS シリーズの位置づけ含む）
- Borden（Mother Mallard）→ Lopatin/Ferraro という系譜の草稿文脈での意味
- 草稿接続候補：L314 Laurel Halo / Ferraro 言及の直後 or HIT 節のコンテキスト補強として1〜2文
- "Internet Gospel" というトラック名の文脈的意味（任意）

**ステータス**：☑ 完了（2026-06-17）。草稿 L314 末尾・分割稿に2文追記。

---

### src-3. r/witchhouse——「Witch House Music History」参照追記

**背景**  
[r/witchhouse のスレッド「Witch House Music History」](https://www.reddit.com/r/witchhouse/comments/1pe4re5/witch_house_music_history/?tl=ja)（日本語訳表示可）は、コミュニティによる witch house 音楽史の整理として詳しい。草稿の `### witch house` 小節（6d-review 反映済み）や `## witch-house.com` には、現時点で当該スレッドへの言及はない。

**追記方針（案）**

- 本文に長文要約は入れず、**「詳しい歴史はこのサブレディットのスレッドが参照になる」**程度の1文＋URL
- 行先候補：`### witch house` 末尾、`## witch-house.com` 冒頭、または脚注／後記の参照リスト
- **rev-9**（witch house 匿名性）・**src-1**（musicplusghost Ch2）と重複しないよう、参照先としての位置づけに留める

**手順**

1. スレッド本文を読み、草稿既述事項との重複を確認  
2. 文案 `第2章取込_witchhouse歴史参照_文案.md`（1段落以内）  
3. [`草稿.md`](./草稿.md) 反映 → 分割稿同期  

**正本 URL**：[https://www.reddit.com/r/witchhouse/comments/1pe4re5/witch_house_music_history/?tl=ja](https://www.reddit.com/r/witchhouse/comments/1pe4re5/witch_house_music_history/?tl=ja)

---

### src-4. ハイパーポップの歴史——PC Music 節の厚み

**背景**  
[`ハイパーポップの歴史.md`](./ハイパーポップの歴史.md) は PC Music 創設（2013）から SOPHIE／QT（2014–2015）、Charli『Vroom Vroom』（2016年2月）まで整理済み。草稿 `## PC Musicという継承`（L456–464）は要約1段落。第4章 L722 付近にも hyperpop 叙述あり——**重複を避け、章ごとに役割分担**する。

**Guardian 2016（Leigh Alexander）との接続**  
同記事は SOPHIE & QT を Neo-Y2K 音楽例として言及（[`CARI_調査ノート.md`](./CARI_調査ノート.md) §2）。第2章で PC Music／QT の層を厚くしてから **cari-draft** で「Collins 経由のメディア並置」を1文足すと、第5章で PC Music を再説明しなくて済む。

**追記候補（優先度順）**

| ハイパーポップ § | 内容 | 草稿の行先 |
|---|---|---|
| §1–2 | PC Music 創設、SOPHIE「Bipp」、Cook との接点 | `## PC Musicという継承` L456 付近 |
| §2 | QT「Hey QT」（2014-08）、Y2K ポップの誇張 | 同上（Guardian 2016 の前提） |
| §4 | Charli XCX『Vroom Vroom』（2016-02） | 同上 or 1文のみ（cari-draft へ委譲可） |
| §8 以降 | 2020– COVID、TikTok、Dismiss Yourself | **第4章 L722 と重複確認**。追記不要ならスキップ |

**手順**

1. src-2 反映後、上表の**採用行**を確定（第4章既述との重複表を文案に書く）  
2. 文案 `第2章取込_ハイパーポップ_文案.md`（**1〜2段落上限**）  
3. [`草稿.md`](./草稿.md) L456 付近に反映 → 分割稿同期  

**注意**：ハイパーポップ全史の取り込みは射程外。2013–2016 の **PC Music／Neo-Y2K 接続**に限定。

---

## CARI（cari-*）

調査（cari-inv）と草稿反映（cari-draft）を**分離**する。調査ノート §8 の未確認は cari-draft の必須条件ではない（断定を避ける書き方で対応済み）。

| ID | 内容 | 状態 | 成果物 |
|---|---|---|---|
| cari-inv | 調査 | ☑ | [`CARI_調査ノート.md`](./CARI_調査ノート.md)。2026-06-17 完了判定。§8 残3件は任意 |
| cari-draft | 草稿反映 | ☑ | `第5章取込_CARI_文案.md` → 第5章 L780–807 付近 |

### cari-inv. 調査——**完了（2026-06-17）**

**完了判定**：cari-draft ☑ 済み。草稿第5章 CARI 節（L978–992 付近）に Guardian・Facebook・Neo-Y2K・Priz Tats／DV-i・GVC が反映済み。正文を止める未確認事項はない。

**§8 確認済み**
- Christmas 2.0 DV-i トラック名「Shenzhen Miracle」☑
- DV-i ＝ Valerie Caputo ☑
- Global Village Coffeehouse ☑
- Priz Tats 拠点（Chicago）☑ 一部
- Valeris Media ☑

**任意残（必要なら後日）**
- Collins ギャラリー URL・トレーラー映像フレーム照合
- Collins と Terrell Davis の関係（Guardian「Facebook グループメンバー」で足りる）
- PC Music 設立日 △（Wikipedia infobox 6/25 vs 本文 6月 vs Cook 8月——草稿は infobox 準拠で固定済み）

**正文は書かない**。上記任意残はノート更新のみ。

### cari-draft. 草稿反映

**依存**：**src-2 → src-4 完了後**（Guardian の SOPHIE & QT・vaporwave 隙間論を第5章だけで説明しないため）

**分量**：第5章 **1段落追記**＋既述（L803–807）への**Facebook 制度化**の短い補強が上限（[`CARI_調査ノート.md`](./CARI_調査ノート.md) §7）

| ブロック | 内容 | src-2/4 後か | 単独可か |
|---|---|---|---|
| A | Guardian 2016：vaporwave 隙間論、Neo-Y2K、Aurora Memoria／Priz Tats | 推奨 | △（PC Music 文が浮く） |
| B | Facebook 制度化（McBling 投票、Frutiger Aero グループ） | — | ○ |
| C | Christmas 2.0／DV-i | 第2章 PC Music 末尾に入れる場合は cari-draft から除外 | 要判断 |

**手順**

1. 文案 `第5章取込_CARI_文案.md`（反映用＋執筆メモ。ブロック A/B の採否を明記）  
2. [`草稿.md`](./草稿.md) `## CARIの起源`〜`## McBling と Frutiger Aero` に反映  
3. L839「Discordが承認プロセス」は Aesthetics Wiki（2020）限定の但し書きを検討（§9 参照）  
4. 分割稿・推敲メモ更新  

**正本**：[`CARI_調査ノート.md`](./CARI_調査ノート.md) §2・§6・§7・§9

---

## 編集方針由来（ed-*）

正本：[`編集方針.md`](./編集方針.md)

| ID | 編集方針 | 対応タスク | 状態 | 行先 |
|---|---|---|---|---|
| ed-1 | §1 政治化（コミュニティの応答） | **rev-7** と同一 | ☑ | 第2章 DMY 節 L426–452（英語圏＋受容の橋。2026-06-02） |
| ed-2 | §2 日本語圏は射程外 | 単独 | ☑ | 序文 L13 直後（2026-06-11） |
| ed-3 | §3 seapunk 読み道整備 | 単独 | ☐ | 第2章 seapunk 節（節頭地図・#### ラベル等。全文圧縮以外） |
| ed-4 | §4 本稿の制度化への寄与（メタ自己言及） | 単独 | ☑ | `## ＜後記＞` L1028 直後（2026-06-11） |
| ed-5 | r/AestheticWiki 制度化追記 | 単独 | ☑ | 第5章「分類する欲望」節 L1109 付近（2026-06-17） |
| ed-6 | 序文——「インターネット美学」と「制度化」の説明節 | 単独 | ☐ | 序文 L9 直後（新 `###`）。下記詳細節 |

**優先度（編集方針記載順）**：ed-1 → ed-2 → **ed-6** → ed-3 → ed-4 → ed-5。ed-1 は rev-7 と一体。ed-2／**ed-6**／3／4／5 はパイプラインと並行可。**ed-6** は序盤用語の穴埋め——読者が第5章「制度化」に到達する前の伏線。

### ed-4. 本稿自身の制度化への寄与——後記メタ段落

**背景（2026-06-11）**  
第5章・後記は CARI／Aesthetics Wiki／Discord による**制度化**を記述している。**歴史を書く行為**も同型の制度化である。ユーザー指示（2026-06-11）：A.G. Cook の Hyperpop プレイリスト**歴史化**とコミュニティ反発を触れ、「歴史化は制度化の最たるものであり、ときにはムーブメントを殺す」——**この文章が十年後にどう読まれるか、わたしにはわからない**、を後記に入れる。

**比喩（一次資料）**  
2019年11月、A.G. Cook が Spotify「Hyperpop」プレイリストのセレクトに J Dilla・Kate Bush を追加し、ジャンル定義に混乱をもたらした（コミュニティの反発）。いま鳴っている hyperpop ではなく**歴史的視座のカノン**を差し込んだことが、制度化の痛みを可視化した事例。

**`concl-1` との住み分け（2026-06-11 確定）**

| タスク | 行先 | 視点 |
|---|---|---|
| **concl-1** | `## クロニクルの終わりにあたって` 末尾 | 外向き：Guardian 2016 の十年問い。美学一般 |
| **ed-4** | `## ＜後記＞` L1028 直後 | 内向き：Cook 事例、本稿＝歴史化、著者の不确定性 |

**既存後記との接続**

| 既出 | ed-4 との関係 |
|---|---|
| FairyPage「モンスターを作った」（L1024） | Wiki 創設者の自省 → **書き手側**の complicity へ拡張 |
| 「答えは書かない。ここに記録したのは、起きたことの歴史だ」（L1028） | **直後**に ed-4。記録＝歴史化の一段 |
| L1030 vaporwave→wiki 締め | ed-4 の**直後**に維持（重複時は ed-4 短縮案） |
| `concl-1` | Guardian 十年問いはクロニクルで済。ed-4 では接続1文まで |
| `ed-2`（日本語圏射程外） | 後記段落順は文案で調整 |

**追記方針**

| 項目 | 方針 |
|---|---|
| 行先 | [`草稿.md`](./草稿.md) `## ＜後記＞` L1028 直後、L1030 直前 |
| トーン | 説教・謝罪ではなくループの自覚。一人称「わたしにはわからない」 |
| 分量 | 1段落上限 |
| 出典 | [Dazed hyperpop 論争](https://www.dazeddigital.com/music/article/55293/1/the-rise-and-fall-of-hyperpop-the-internets-most-confusing-music-genre)（[`ハイパーポップの歴史.md`](./ハイパーポップの歴史.md) §7） |
| 文案 | [`後記取込_制度化ループ_文案.md`](./後記取込_制度化ループ_文案.md) ☑ 作成済 |

**手順**

1. concl-1 反映（クロニクル末尾）  
2. ed-4 反映（後記）  
3. 分割稿・推敲メモ更新  

**依存**：concl-1 と**同批**反映推奨（後記段落順の一体確認）

### ed-6. 序文——「インターネット美学」と「制度化」の説明節

**背景（ユーザー指示・2026-06-17）**  
草稿は序文 L9・第5章題で「**制度化**」を使うが、読者向けの定義節がない。同様に「**インターネット美学**」カテゴリの来歴も序盤で説明されていない。序盤に説明節を設けたい。

**調査の結論（暫定）**  
[`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) に整理済。

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
3. [`第1章_土壌.md`](./第1章_土壌.md) 等の分割稿は序文があれば同期要否を判断  
4. 本ファイル・[`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 更新  

**正本**：[`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md)

**ステータス**：☐ 調査ノート ☑。文案作成 → 承認 → 序文反映。

---

## メタ・著者性（meta-*）

正本：[`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 続8（編集方針確認）。**ed-3・inv-* 等の正文作業の後**に着手。meta-2 は草稿**末尾**に置き、他タスクより後回し。

| ID | 内容 | 状態 | 行先 | 備考 |
|---|---|---|---|---|
| **meta-1** | 執筆動機ツイート追記 | ☐ | 序文 or 後記 | 本稿を書き始めた直接の動機となったツイート（URL 要確認）。後記の抽象的な自己言及を具体化 |
| **meta-2** | 振り返りパート新設 | ☐ | [`草稿.md`](./草稿.md) **末尾**（`## ＜後記＞` の後） | 11万字規模の定期的振り返り。優先度**低・最後**。節構成・挿入位置は文案で決める |
| **meta-3** | 遡行的確定——本稿の自己言及（後記追記） | ☐ | [`草稿.md`](./草稿.md) `## ＜後記＞` 内 | 下記詳細節。ed-4・匿名性 C3 との住み分け |

### meta-1. 執筆動機ツイート

**背景**  
後記には匿名性の美学・植リンク・歴史化 complicity など自己言及が集中している（ed-4・rev-9 続）。執筆の**直接のきっかけ**となったツイートを1〜2文で接地させ、メタ段落の密集感を和らげる。

**手順**

1. 動機ツイートの URL・日付・引用文を確定  
2. 文案（1段落上限）→ 序文 or 後記のどちらかに反映（後記 L1127 付近の自己言及群と接続しやすい）  
3. 分割稿・推敲メモ更新  

**依存**：なし（単独可）

### meta-2. 振り返りパート新設

**背景**  
続8 で「長大な草稿では定期的な振り返り・多重記述は必要」と編集方針を確認。現状、第2章 seapunk 節などに章内振り返りはあるが、**全体を俯瞰する振り返り節**は未整備。

**方針**

| 項目 | 方針 |
|---|---|
| 行先 | 草稿**最末尾**（後記の後）。新設 `##` 節 |
| 優先 | **低**。ed-3・meta-1 等の後 |
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
| **三過程モデル**（推敲メモ） | ラベルの仮予約 → コミュニティによる充填 → **遡行的確定**で事後的に実体化 | [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 層4・続8 |
| **本稿への跳ね返し** | クロニクルが witch house→vaporwave→CARI と**線を引く**こと自体が、過去の整理・ナラティブ構築である | 後記 L1244（ed-4：「線を引いている」）の**理論的補強** |

**ed-4・既出後記との住み分け**

| 既出 | meta-3 で書くこと | 書かないこと |
|---|---|---|
| **ed-4**（L1244） | 歴史化＝制度化、Cook 事例、「線を引いている」 | 同じ比喩の繰り返し |
| **匿名性 C3**（L1242） | 「名づけたこと自体が加担」 | 匿名性の再説明 |
| **L1236**「起きたことの歴史」 | **記録＝中立な鏡ではない**という問いかけ | 「記録は嘘だ」という断定 |
| **meta-3 の核** | 遡行的確定は**観測対象でもあり本稿の方法でもある**。Frutiger Aero の例を**手がかり**に、見方の発明・過去の単純化を自覚する | 学術総論化、Wittgenstein 等の長い理論展開 |

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
3. 分割稿・[`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 更新  

**正本・参照**

- 草稿 L23（序文・遡行的確定の初出）、L1067–L1071（第5章 Frutiger Aero 節）
- [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) 層4・続8（三過程モデル・本稿の独自性）
- [`後記取込_制度化ループ_文案.md`](./後記取込_制度化ループ_文案.md)（ed-4・住み分け用）

**ステータス**：☐ 計画先行。文案作成 → 承認 → 後記反映。

---

## 結論部改稿（concl-*）

正本：[`CARI_調査ノート.md`](./CARI_調査ノート.md) §2（Guardian 2016・Leigh Alexander）、§7 執筆メモ 2d。**cari-draft 後推奨**（同一記事の別端。rev-7 の fashwave 記事とは別）。

| ID | 内容 | 状態 | 文案（案） |
|---|---|---|---|
| concl-1 | Guardian 2016 結論の**時代診断**問いかけ（ユーザー改稿・案A） | ☑ | [`第5章取込_結論_Guardian問いかけ_文案.md`](./第5章取込_結論_Guardian問いかけ_文案.md) |

### concl-1. 結論部——Guardian の時代診断問いかけ

**完了（2026-06-11）**：[`草稿.md`](./草稿.md) `## クロニクルの終わりにあたって` L1018 直後にユーザー改稿版を反映。分割稿同期済。

**背景**  
[Guardian 2016-05-19（Leigh Alexander）](https://www.theguardian.com/technology/2016/may/19/year-2000-y2k-millennium-design-aesthetic) の末尾は、Y2K 美学の議論から**現在進行形の時代診断**へ視点を広げ、十年後の回望という問いで締める。調査ノート §2「結論部の問いかけ」に英文・編集含意を整理済み。

**借用の核（Guardian 結論・要約）**

> "What will the aesthetics of this period of time look like with a decade's hindsight – and what might they reveal about us that we can't see in the present?"

記事はその直前に、2016 Met Gala の android 風ファッション、選挙不安、難民危機、シリコンバレー文化などを**今日の音楽・建築・デザインから読み解けるか**と問う。

**追記方針（案）**

| 項目 | 方針 |
|---|---|
| 行先 | `## クロニクルの終わりにあたって`（L1018）直後。**案A確定** |
| トーン | 本論考全体の「分類への欲望」「制度化」の流れを受け、**未来の回望**へ開く問いかけ。説教調にしない |
| 出典 | さらりと明示（例：「2016年、*The Guardian* は Y2K 美学を扱う記事の結びで、こう問った——」＋公開 URL）。英文の長引用は避け、日本語で要約可 |
| 分量 | **1段落以内**（編集方針：結論は増やしすぎない） |
| 接続 | CARI／Facebook グループの *discuss and define*、Aesthetics Wiki のカタログ化、TikTok 時代の美学流通——いずれか1つと短く接続すれば足りる |
| 依存 | Guardian 原文の一字確認は [`CARI_調査ノート.md`](./CARI_調査ノート.md) §2 参照。第5章 CARI 節への Guardian 追記（Priz Tats 等）とは**別文案**（結論専用） |

**手順**

1. [`第5章取込_結論_Guardian問いかけ_文案.md`](./第5章取込_結論_Guardian問いかけ_文案.md) ユーザー改稿版を草稿 L1018 直後に反映  
2. 続けて ed-4（[`後記取込_制度化ループ_文案.md`](./後記取込_制度化ループ_文案.md)）  
3. 分割稿・推敲メモ更新  

**注意**：2016 年の具体例（Met Gala、VR ブーム等）を本文で検証展開する必要はない。問いの**型**の借用が本体。

---

## 6. Seapunk 詳細調査ノート——段階的取り込み

**背景**  
[`Seapunk 詳細調査ノート.md`](./Seapunk%20詳細調査ノート.md)（1140行）は seapunk 以外（witch house、aesthetic 語法、vaporwave 接続）を大量に含む。**一括統合すると第2章のバランスが崩れる**ため、ドメイン別・段階別に取り込む。

**前提**：6a では**草稿を書き換えない**。

### 6a. 影響評価（統合しない）——**完了（計画実行済）**

**目的**：取り込み計画書を完成し、6b〜6e を機械的に実行できるようにする。

**成果物**：[`Seapunk調査_取り込み計画.md`](./Seapunk調査_取り込み計画.md)（6b〜6f まで実行済み）

**計画書に含める表**（各行を 6b〜6e のタスクにする）

| ドメイン | 調査ノート § | 草稿の行先 | 判定 | 担当 |
|---|---|---|---|---|
| seapunk 三極・内部対立 | §4, §7 | 第2章 seapunk 節 | 叙述修正 | **6b** |
| Tropicult／Tundra Dubs／w-h 接点 | §5, §6 | 第2章 seapunk（Tropicult 直後） | 追記 | **6b** |
| BuzzFeed 激怒・擁護の詳細 | §8-2a, §8-4 | 第2章 seapunk の死 | 一部追記／参照 | **6b** |
| H∆SHTAG$ ep5 発言 | §9 | aesthetic 節＝語彙・年表（**6c-2** ☑）；seapunk 節＝#Tumblrwave 厚み（**6b-reorg 後続** ☐・反映用除外） | 追記・分割 | **6c**＋**6b-reorg 後続** |
| Perpetua／Bebe Zeva の aesthetic | §8-2a | 第2章 aesthetic 節 | 年表に挿入 | **6c** |
| Dodecahedron「aesthetics」 | §9 | 第2章 aesthetic 節 | 追記 | **6c** |
| witch house 前史・レーベル | §2, §12 | 第2章 witch house 小節 | 最小限 or 正本維持 | **6d** |
| vaporwave cousin（BuzzFeed 2012-11） | §8-4, §10 | seapunk 遺産／vaporwave | 追記 | **6e** |
| health goth 並置等 | §9 末尾 | 射程外 | 参照のみ | — |

**判定**：追記＝1〜2段落／叙述修正＝節骨格の書換／参照のみ＝脚注 or 触れない／最小限＝1〜2文＋調査ノート正本

**残チェック（任意・低優先）**

- [ ] [`草稿_ファクト補強調査.md`](./草稿_ファクト補強調査.md) に Seapunk 調査ノートへのリンクを追記  

---

### 6b. Seapunk 本体——**完了（残タスクあり）**

草稿反映済み（2026-06-02）。文案：[`Seapunk取込_6b_文案.md`](./Seapunk取込_6b_文案.md)。6b-5・6b-6 は未反映。

- [ ] 文案に「調査ノート」参照・フェーズ番号が**反映用**に混入していないか（執筆メモのみ可）  
- [ ] 6b-3：VICE 年表が Lil Internet／Lil Government 作であることを明示しているか  

---

### 6b-reorg. seapunk 初期節——**完了（後続あり）**

草稿反映済み（2026-06-02）。文案：[`Seapunk取込_6b-reorg_文案.md`](./Seapunk取込_6b-reorg_文案.md)。

**未完了（任意・6d-review と並行可）**

- [ ] **M.I.A.・Tim and Eric**：激怒記事段落の**後**に追記。文案除外箱 L80。Jerome・Reblorg は L238 付近済み  
- [ ] **H∆SHTAG$ ep5（厚み）**：seapunk 節への再配置は任意（aesthetic 6c-2 ☑）

**正本（除外箱）**：調査ノート §8-2a、[RBMA ep5](https://daily.redbullmusicacademy.com/2013/03/hashtags-tumblrwave/)

---

### 6c. aesthetic 年表——**完了**

6c-1・6c-2 反映済み（2026-06-02）。6c-3 却下。文案：[`Seapunk取込_6c_文案.md`](./Seapunk取込_6c_文案.md)。

**反映後に確認（未）**：年表順（Floral Shoppe → 6c-1 → 6c-2 → Savvy J）、L254 現状維持、BuzzFeed と Bebe 引用の読み順。

**§9 へ委譲**：包含関係の逆転（L112）／FrankJavCee 系列／vaporwave 起源説 vs 多系統収束／**L254 接続文の整理**

---

### 6f. Seapunk 後続——**完了**

方針 A 反映済み（2026-06-02）。文案：[`Seapunk取込_6f_文案.md`](./Seapunk取込_6f_文案.md)。年表厚み B 案は見送り。

---

### 6d. witch house 前史——§2 還流（一次反映済み）

**状態**：[`Seapunk取込_6d_文案.md`](./Seapunk取込_6d_文案.md) に基づき草稿 `### hypnagogic popとwitch house`（L143 付近）を差し替え済み（2026-06-02）。seapunk 節 `## witch-house.com` の開設日重複は圧縮済み。

**注意**：一次反映後、**小節全体の推敲は未完了**。続きは **§6d-review**。

- [x] 文案・§2 還流の草稿反映  
- [ ] **6d-review**（下記）

---

### 6d-review. 第2章 witch house 節の改稿（まとめ型）——**一次反映済・残チェックあり**

**方針（確定）**：節構成を **`### chillwaveとhypnagogic pop`（＋憑在論）→ `### witch house`** に再編。大見出し順序は変更しない（`## vaporwaveという名前以前に` → `## 2011年6月1日のツイート` は現状維持）。

**文案**：[`Seapunk取込_6d-review_文案.md`](./Seapunk取込_6d-review_文案.md)（6d-r0 節再編 ／ 6d-r1 witch house 差し替え）  
**論点整理**：[`6d-review_aesthetic論点整理.md`](./6d-review_aesthetic論点整理.md)  
**構成案**：[`6d-review_第2章構成案.md`](./6d-review_第2章構成案.md)  
**正本素材**：[`witchhouse-chillwave調査メモ.md`](./witchhouse-chillwave調査メモ.md)（主）／[witch-house.com THE TIMELINE](https://witch-house.com/thetimeline/)（参照）

**反映手順**

| サブ | 内容 | 状態 |
|---|---|---|
| 6d-review-1 | 文案 6d-r0・6d-r1 を草稿 L131–155 に機械反映。L155 締め維持 | ☑ |
| 6d-review-2 | #### 小見出し追加（**案A** 推奨）。論点整理の零れ落ち反映 | ☑ |
| 6d-review-3 | `## vaporwaveという名前以前に` へ GATEKEEPER／aesthetic 前史の軽い接続 | ☑ |
| 6d-review-4 | 推敲メモ・調査メモ追記・ユーザー承認 | ☑（推敲メモ 続33。目視確認は任意） |

**チェックリスト**

- [x] 文案作成（まとめ型・`### witch house` 独立見出し）
- [x] 論点整理・構成案
- [x] ユーザー承認：**案A**／L155 橋渡し文は**入れない**（6d-review-3 で軽接続）
- [x] **6d-review-1**：草稿反映（2026-06-02）
- [x] **6d-review-2**：#### 小見出し（案A）。Sherburne ブログ URL 明示（2026-06-02）
- [x] **6d-review-3**：vaporwave 前史への軽接続（2026-06-02）。Megazord 出自は前節で済・第1章参照のまま
- [x] **Urdiales 前史**：本文に**入れない**（ユーザー判断 2026-06-02。Pitchfork 初出・Zoots 主線と別ルート）
- [x] **TOPY／Psychic TV**：L157 来歴段落に1文追記（Siepmann 2018。2026-06-02）
- [ ] **分量・時系列**：段落内日付順、seapunk 前史とのバランス
- [ ] **seapunk 節との接続**：`## witch-house.com` との役割分担、末尾橋渡し
- [x] [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) に 6d-review ログ（続33）

**6d-review 由来の後続（本文は別フェーズ）**

- [ ] **第4章**：The Caretaker（コロナ禍再評価）と liminal space／Backrooms／Dead Malls の接続
- [ ] **第2章後半以降**：vaporwave とオルタナ右翼（Nick Land／暗黒啓蒙、Harper 2012、2016 再読）。L349 から拡張するか独立ブロックか要判断

---

### 6e. vaporwave 接続——**完了**

6e-1・6e-2 反映済み（2026-06-02）。文案：[`Seapunk取込_6e_文案.md`](./Seapunk取込_6e_文案.md)。反映先：`## seapunkの死と遺産` 末尾。

**6d-review-3 との分担**：6e は seapunk→vaporwave の言語化済み。6d-review-3 は `## vaporwaveという名前以前に` への witch house aesthetic／GATEKEEPER **前史**の軽接続（重複しないよう1–2文程度）。

---

### aesthetic 手動調査——草稿反映（**§9-man**）

**背景（2026-06-02）**  
[`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md) の**調査・サマリーは完了**。以降の追記（Google Trends 等）は任意。**草稿への反映**は、既存フェーズと重ならないよう**タイミングを分割**する。

| タイミング | 反映する内容 | 草稿の行先 |
|---|---|---|
| **6c 反映（今）** | [`Seapunk取込_6c_文案.md`](./Seapunk取込_6c_文案.md) 6c-1・6c-2 のみ。手動調査は**裏付け**（Bebe・Perpetua・ep5）— 重複追記は不要 | `## 「aesthetic」という語` 年表（L256 直後） |
| **6e** | BuzzFeed cousin・seapunk 以降の vaporwave 言語化；r/vaporwave **chillwave 系譜**（1〜2文＋Wayback） | `## seapunkの死と遺産` 末尾 or DMY 節橋渡し |
| **§9 ＋ §9-man（本体）** | L256 Floral Shoppe／**KYM 叙述の緩和**；YouTube Wayback（2013-06・aesthetic なしの限定否定）；X 検索（2026-06-02 手動・限定付き）；Reddit 三サブ・NA（Furtherfield）；11月騒動と事後知名度のずれ；Bebe を aesthetic 節の**叙述軸** | aesthetic 節全体・図式 L112–117 |
| **§9-man 追補（任意）** | Google Trends；削除動画の代替 URL 整理 | 同節または脚注 |

**成果物**：§9 文案 `aesthetic_語法年表_文案.md` 作成時に、手動調査**冒頭サマリー**を一次素材とする（調査ノート § 参照は文案の執筆メモのみ）。

**チェックリスト**

- [x] **6c**：6c-1 → 6c-2 を草稿反映（2026-06-02）  
- [x] **6e**：上表「6e」行を草稿反映（2026-06-02）  
- [x] **§9-man**：`aesthetic_語法年表_文案.md` 作成→草稿反映（2026-06-02）  
- [x] 正文に調査ノート § 参照なし（Wayback・X 操作記録は限定付き）  
- [x] [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) に §9-man 完了ログ  

**ブロック**：§9-man 本体 4〜6時間（§9 節と同時進行可）。6c・6e 分は各フェーズの文案時間に含む。

---

### 7. ドキュメント整理③（Seapunk 取込後）——**完了**

- [x] [`第2章_命名の時代.md`](./第2章_命名の時代.md) を草稿に追従（2026-06-02。6d-review・TOPY 含む。画像コメント5件維持）  
- [x] [`第4章_爆発.md`](./第4章_爆発.md) を草稿 `## TikTokというアーキテクチャの転換` に追従（2026-06-02）  
- [x] [`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) 新設（ed-6 正本・2020広がり／2022制度化・Wikipedia 立項）
- [x] [`インターネット美学（Internet Aesthetics）調査ノート.md`](./インターネット美学（Internet%20Aesthetics）調査ノート.md) §5 へ採用ファクト還流（5-1 更新・5-8 追加）  
- [x] `Seapunk取込_6*_文案.md` → [`archive/Seapunk取込文案/`](./archive/Seapunk取込文案/) に移動（2026-06-02）  
- [x] 後記 L841 修正（「アルゴリズムなき」→ クラスタ内発見／横断配信。草稿・第5章分割稿）  
- [x] 本ファイル進捗サマリー 7 を ☑  

---

## 9. aesthetic 包含関係（**6d-review＋7 完了後**）

**前提**：6c（Perpetua 等）・6e（seapunk→vaporwave）を草稿に入れたうえで、L112 付近の**叙述骨格**を再確定する。**§9-man**（手動調査の草稿反映）と**同一文案**で進めるのが推奨。

**論点**：KYM 2015（aesthetic＝vaporwave 下位）と CARI/Wiki 2020年代（aesthetic＝上位）を同一節で扱う際の時制・因果。包含関係の「逆転」を **KYM サイト分類**／**語彙の汎化**／**CARI/Wiki 制度化**の三段に分けるか。Floral Shoppe コメント起源説は手動調査で**弱め**（§9-man）。

**正本・素材**

- 保留論点・KYM 年表：[`序文_改稿.md`](./序文_改稿.md)  
- FrankJavCee 系列：[`FrankJavCee文字起こし.md`](./FrankJavCee文字起こし.md)  
- **手動調査サマリー**：[`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md)（調査完了・反映は §9-man）  
- 成果物（作成予定）：`aesthetic_語法年表_文案.md`

**完了時**（§9-man チェックリストと兼ねる）

- [x] 草稿 第2章 aesthetic 節を [`aesthetic_語法年表_文案.md`](./aesthetic_語法年表_文案.md) で改稿（§9-man 素材反映）  
- [x] 図式（三段レジスタ）と本文の時制・因果を一致（2026-06-02）  
- [x] [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) に改稿ログ（続37）  

**ブロック**：4〜6時間

---

## 完了済み（詳細は推敲メモ）

| フェーズ | 完了日 | ログ |
|---|---|---|
| 1 ブロック F | 2025-05-29 | 推敲メモ 続8 |
| 2 三枠境界論 | 2025-05-31 | 推敲メモ 続10〜11・序文改稿 |
| 3 ドキュメント整理① | 2025-05-31 | 推敲メモ 続14 |
| 4 ファクト補強 #11〜22 | 2025-05-31 | ファクト補強調査・推敲メモ 続12〜13 |
| 5 ドキュメント整理② | 2025-05-31 | 第3〜5章分割稿・README |
| §8-1 序文・aesthetic 統合稿 | 2026-06-01 | 推敲メモ 続17・[`序文_改稿.md`](./序文_改稿.md) |
| §8-2 Tumblr For You | 2026-06-01 | [`§8-2_Tumblr_ForYou_調査メモ.md`](./§8-2_Tumblr_ForYou_調査メモ.md)・推敲メモ 続18 |
| §8-3 KYM Wayback 訂正 | 2026-06-01 | 序文_改稿・第2章分割稿・覚書 L129 |

---

## クイックリファレンス

| 段階 | 次の1手 |
|---|---|
| **今** | **inv-vektroid**／**src-1**／**ed-3**／**ed-6**（並行可） |
| **その次** | inv-swan／inv-tabor／rev-4 |
| 後回し | **meta-1** → **meta-3**（遡行的確定・後記）→ **meta-2**（振り返り・**草稿末尾・最後**） |
| 並行可 | 6b-reorg 後続、6c 残 |
| 完了済み（直近） | **inv-piajp**／**inv-steyerl**／inv-msv／inv-dclub ☑ |
| 任意 | rev-12 Caretaker、8番出口、§8 残 |

**索引の正本**：§タスク索引（本ファイル上部）

---

## 参照ファイル

| ファイル | 役割 |
|---|---|
| [`草稿.md`](./草稿.md) | 正本 |
| [`草稿_推敲メモ.md`](./草稿_推敲メモ.md) | 改稿ログ（完了フェーズの詳細） |
| [`草稿_ファクト補強調査.md`](./草稿_ファクト補強調査.md) | ファクト候補 #6〜22 |
| [`Seapunk 詳細調査ノート.md`](./Seapunk%20詳細調査ノート.md) | Seapunk 横断調査の正本 |
| [`Seapunk調査_取り込み計画.md`](./Seapunk調査_取り込み計画.md) | 6a 成果物——行単位の取込タスク |
| [`序文_改稿.md`](./序文_改稿.md) | §9 保留論点・KYM Wayback 年表 |
| [`§8-2_Tumblr_ForYou_調査メモ.md`](./§8-2_Tumblr_ForYou_調査メモ.md) | Tumblr アルゴリズム年表 |
| [`FrankJavCee文字起こし.md`](./FrankJavCee文字起こし.md) | §9 FrankJavCee 分析の正本 |
| [`aestheticに関する手動調査.md`](./aestheticに関する手動調査.md) | aesthetic 語法・Floral Shoppe コメント年代・X 検索ログ（2026-06-02） |
| [`archive/Seapunk取込文案/Seapunk取込_6d-review_文案.md`](./archive/Seapunk取込文案/Seapunk取込_6d-review_文案.md) | 6d-review 反映用本文（アーカイブ） |
| [`6d-review_aesthetic論点整理.md`](./6d-review_aesthetic論点整理.md) | aesthetic 零れ落ち・層A–E |
| [`6d-review_第2章構成案.md`](./6d-review_第2章構成案.md) | #### 案・フェーズ分割 |
| [`witchhouse-chillwave調査メモ.md`](./witchhouse-chillwave調査メモ.md) | witch house／chillwave 調査 |
| [`草稿_レビュー論点メモ.md`](./草稿_レビュー論点メモ.md) | レビュー論点の正本・rev-* ロードマップ |
| [`musicplusghost.md`](./musicplusghost.md) | FEECO *MUSIC + GHOST* 全文テキスト（src-1 正本） |
| [`supersuper.md`](./supersuper.md) | SuperSuper! 号別調査・PC Music 前史（src-2 正本） |
| [`HipposInTanks_調査ノート.md`](./HipposInTanks_調査ノート.md) | HIT カタログ・vaporwave 前史（src-5 正本） |
| [`MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md`](./MP3ブログ時代とエクスペリメンタル・シーン調査ノート.md) | MP3ブログ・レーベル史・MySpace/Tumblr設計史（src-6 調査正本） |
| [`src-6_仕分け.md`](./src-6_仕分け.md) | src-6a 成果物——節別仕分け・フェーズ6b–6f・委譲表 |
| [`vaporwave政治化_調査ノート.md`](./vaporwave政治化_調査ノート.md) | rev-7 正本（2016 fashwave・コミュニティ応答・Boriswave） |
| [`Vaporwave Is (Not) a Critique of Capitalism_Genre Work in An Online Music Scene.md`](./Vaporwave%20Is%20(Not)%20a%20Critique%20of%20Capitalism_Genre%20Work%20in%20An%20Online%20Music%20Scene.md) | Whelan & Nowak 2018 全文（@ccchristtt 引用含む） |
| [`Vaporwave_Politics_Protest_and_Identity.md`](./Vaporwave_Politics_Protest_and_Identity.md) | McLeod 2018 全文（PDF 抽出） |
| [`note_極右の世界のBGM.md`](./note_極右の世界のBGM.md) | ykic 二次・fashwave 年表（Vice 日付は14日に訂正） |
| [`CARI_調査ノート.md`](./CARI_調査ノート.md) | cari-inv／cari-draft 正本（Guardian・Facebook 制度化・Priz Tats） |
| [`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) | **ed-6** 正本（語史・Wikipedia 立項・制度化の説明例） |
| [`CARIの歴史.md`](./CARIの歴史.md) | CARI 公式年表の和訳 |
| [`ハイパーポップの歴史.md`](./ハイパーポップの歴史.md) | src-4 正本（PC Music・SOPHIE・QT・2013–2016） |
| [`編集方針.md`](./編集方針.md) | ed-1〜3 の根拠 |

---

*更新：2026-06-17（続28）。**ed-6** タスク追加（序文・インターネット美学と制度化の説明節）。調査ノート [`internet_aesthetic語と制度化_調査ノート.md`](./internet_aesthetic語と制度化_調査ノート.md) 新設。*
*更新：2026-06-17（続27）。**meta-3** タスク追加（遡行的確定・本稿の自己言及——後記追記）。*
*更新：2026-06-17（続25）。**inv-piajp** ☑ 文案＋草稿反映（第1章・『アイデア』366号／美術手帖2015/6）。*
*更新：2026-06-17（続17）。**inv-steyerl** ☑ 文案＋草稿反映（Post T.V. 節末 `####`）。*
*更新：2026-06-17（続16）。**inv-piajp** タスク追加（日本のポストインターネットアート受容——『アイデア』2014/9・美術手帖2015/6）。*
*更新：2026-06-17（続15）。**cari-inv** ☑ 完了判定（§8 残3件・PC Music 日付は任意）。次の1手＝**inv-frkwys**。*
*更新：2026-06-17。**ed-5** ☑（r/AestheticWiki）。**meta-1**／**meta-2** タスク化。rev-10 追記（Still Life/DREAM JOURNAL）反映。*
*更新：2026-06-11。**ed-2** ☑ 序文反映。**concl-1**・**ed-4** ☑。*
