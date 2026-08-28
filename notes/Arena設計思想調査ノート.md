# Are.na 設計思想調査ノート
## ——CARI（Consumer Aesthetics Research Institute）との関係を含む

**作成日:** 2026-06-27  
**対象:** Are.na（are.na）の設計思想、創設経緯、CARIとの実践的・思想的関係  
**用途:** 「インターネット美学の系譜」原稿参照資料  
**調査方法:** 創設者インタビュー、公式ドキュメント、メディア記事の一次資料照合

---

## 1. Are.naの概要と起源

**Are.na**（are.na）は、画像・テキスト・リンク・ファイルを「ブロック」として収集し「チャンネル」に束ねるウェブプラットフォーム。アルゴリズムなし・広告なし・非パーソナライズを原則とする。共同創業者はCharles Broskoski、John Michael Boling、Daniel Pianetti他。

### del.icio.usからの系譜

- Broskoskiは2006年頃、ソーシャルブックマークサービス **del.icio.us** を通じてJohn Michael Bolingと出会い、「リンクのアーカイブが自分の思考の星座図になる」ことを体験した
- **del.icio.usのYahooによる買収・サービス劣化・終了**がare.na創設の直接的動機のひとつ
- 同じ経緯でBroskoskiはPinboard（Maciej Cegłowski運営の後継的ブックマークサービス）も高く評価している

> "Around 2006, I met John Michael Boling through a social bookmarking website called Del.icio.us. Your Del.icio.us profile ended up being a nice representation of what you were interested in and actively thinking about." — Charles Broskoski  
> 出典: [The Creative Independent, 2017-10-25](https://thecreativeindependent.com/people/charles-broskoski-on-self-discovery-upon-revisiting-things-youve-accumulated-over-time/)

> "Delicious shutting down was one of the things that moved us to create Are.na."  
> 出典: [UMass Amherst / Initiative for Digital Public Infrastructure ポッドキャスト](https://publicinfrastructure.org/podcast/40-arena/)

---

## 2. 設計思想の核心：「考えるための道具」

### 2-1. 広告モデルの原則的排除

Are.naは創設当初から広告をビジネスモデルとして検討していない。理由は機能的なものではなく**思想的なもの**。

> "For us, advertising as a business model was never on the table. Are.na is a tool for thinking and showing ads would very obviously degrade the experience of being able to think through things on Are.na."  
> 出典: [Upstatement インタビュー（Charles Broskoski）](https://upstatement.com/blog/interview-with-charles-broskoski)

この立場の根拠は「動機の整合性（alignment of motivations）」にある。広告モデルでは顧客が広告主となり、ユーザーへの奉仕と利益相反が生じる。

> "It really just comes down to motivation. How does a company's business model motivate them to shape the experience? Our main goal as a company is to make sure that our motivations are aligned with the community we serve."  
> 出典: [同上]

### 2-2. アルゴリズムの不在という積極的選択

Are.naには：
- フィードを駆動するアルゴリズムがない
- コンテンツのパーソナライズ推薦がない
- 「いいね」数などエンゲージメント指標がない（▲いいね機能の有無は要確認）

この設計はシリコンバレー的なエンゲージメント最大化モデルへの明確な批判として提示されている。

> "One of the ways to describe Are.na is things that it doesn't have. It doesn't have advertising. It doesn't have an algorithm that drives a feed. It doesn't have an attempt to personalize itself to your own needs. […] especially in an age where there's so many personalized algorithms that are recommending you content all the time, [deciding if a piece of information is important and where it lives in your universe of thought] is a behavior that can be learned, and also extremely valuable."  
> 出典: [UMass Amherst / IDPI ポッドキャスト（Broskoski & Daniel Pianetti）](https://publicinfrastructure.org/podcast/40-arena/)

### 2-3. 「空間を与える」設計哲学

Are.naの設計は「ソートするのではなく空間を与えること」を中心に置く。

> "It's so easy to treat technology as though it can prescribe a solution to a particular problem. But what humans really need is much more simple: time and space to think and process. Are.na's design philosophy centers on giving you space rather than sorting things for you. The best tools don't tell you what to pay attention to."  
> 出典: [Substack / "Everything is Personal for Are.na Founder Charles Broskoski", 2026-02-25](https://jdahl.substack.com/p/cab)

Broskoski自身のare.na使用法を見ると、チャンネルは「すでに記述できるアイデアのコレクション」ではなく「まだ形になっていない思考領域」として始まる：

> "I tend to think of my channels as areas of thought that become more articulated over time. I like it when I don't necessarily know how to describe what the channel is but still know when I see something in the world (or online) that belongs in the channel."  
> 出典: [Upstatement インタビュー](https://upstatement.com/blog/interview-with-charles-broskoski)

---

## 3. ビジネスモデルと思想的整合性

### 3-1. VC拒否と持続可能性

Are.naはVC資金を一切受け入れていない。2018年のエクイティクラウドファンディング（約27万ドル）が唯一の外部資金調達であり、通常のVC投資とは性格が異なる。

> "They've never raised formal venture capital, but in 2018 participated in a ~$270K equity crowdfunding round that allowed people to invest to own a small stake of Are.na."  
> 出典: [Kernel Magazine, "Taking Business Personally: A Conversation with Charles Broskoski"](https://www.kernelmag.io/3/charles-broskoski-interview)

2016年にKnight Foundationから3万5千ドルのグラントを受けており、これが「ブランドに合う」資金として受け入れられた最初の外部資金。

> "We got a grant from the Knight Foundation in 2016. It was $35,000, which wasn't much, but it was wind in our sails. And that money felt on brand. We started to ask ourselves — what wouldn't we be embarrassed by?"  
> 出典: [Kernel Magazine, 同上]

### 3-2. 「慶雲館モデル」——超長期持続性

Are.naの目標比較対象は他のSNSではなく、705年創業の旅館：

> "Eventually, Broskoski hopes Are.na will become the 'next Nishiyama Onsen Keiunkan,' a hot spring spa founded in Hayakawa, Japan in 705 A.D. — a sustainable business that is around for the long-haul."  
> 出典: [Kernel Magazine, 同上]

### 3-3. 財務透明性

Are.naは財務データを公開している（▲現在の公開状況は要確認）。この透明公開はコミュニティファーストモデルの制度的表明として位置づけられる。

> "From being directly funded by its users, to publishing all of its financial data transparently on their website, Are.na has found a way to make a community-first model work."  
> 出典: [ZORA ZINE, "Are.na Is Where We Go to Find Ourselves Online"](https://zine.zora.co/arena-charles-broskoski)

---

## 4. 創設者の背景：アーティストによるツール制作

Broskoskiはパーソンズ・スクール・オブ・デザインでファインアートを学び、Artsyでエンジニアリング・リードを務めた後are.naに専念。

> "During the last show I made, I was thinking a lot about generosity as an artist, as in, 'How can an artwork be generous to a viewer?' Towards the end of the show, I came to the conclusion that making tools was probably the most generous thing that I could do, as an artist."  
> 出典: [Upstatement インタビュー](https://upstatement.com/blog/interview-with-charles-broskoski)

チームはクリエイティブ出身者で構成されており、Broskoskiはこれが**「インターネットを面白くするための条件」**だと主張する：

> "Are.na's team comes from creative backgrounds, and Charles believes creative decision-making is harder to teach than the mechanics of running a company. The internet would be more interesting if more people like that were building things."  
> 出典: [Substack / Dahl, 2026-02-25](https://jdahl.substack.com/p/cab)

---

## 5. ユーザー論：「connected knowledge collectors」

Are.naが想定するユーザー像はデモグラフィックより**サイコグラフィック**で定義される：

> "I think it's more of a kind of like psychographic than it is of a demographic. It's people who are interested in pursuing lots of different disciplines. People who are interested in directing their own learning or education. We have this really cheesy term, but we say, connected knowledge collectors."  
> 出典: [UMass Amherst / IDPI ポッドキャスト](https://publicinfrastructure.org/podcast/40-arena/)

are.naの使用には認知的なハードルがある——受動的消費から能動的なキュレーションへの「跳躍」。Broskoskiはこれが学習可能な行動だと主張している。

---

## 6. CARIとAre.naの関係

### 6-1. Are.naはCARIの「研究基盤」

Evan CollinsのAre.naプロフィール（`are.na/evan-collins-1522646491`）には明示的に記載：

> "Our CARI (Consumer Aesthetics Research Institute) work is based here on Are.na; if you'd like more information on any item let me know by commenting on the block and I can try to track it down. This page acts a front-facing collection of research work done by both our CARI members, and work done by others online."  
> 出典: [Evan Collins | Are.na プロフィール](https://www.are.na/evan-collins-1522646491) ／ [Hexbear経由のミラー引用](https://hexbear.net/post/213516)

### 6-2. ワークフロー上の役割

CARIの研究プロセスにおいて、Are.naは**初期のアイデア出しと協働研究**の場として機能：

> "This process begins with community members submitting examples sourced from physical media, such as scans of vintage magazines, product brochures, and design catalogs, which are then organized using digital platforms like Are.na for initial ideation and research collaboration."  
> 出典: [Grokipedia / Consumer Aesthetics Research Institute](https://grokipedia.com/page/consumer_aesthetics_research_institute)（▲二次的要約資料のため要一次確認）

### 6-3. 各aestheticページとのチャンネル対応

CARIサイト（cari.institute）の各aestheticページには対応するare.naチャンネルへのリンクが設置されている。例：
- Internet Awesomesauce: `are.na/consumer-aesthetics-research-institute/internet-awesomesauce-_ej3pgc0pwe`  
  出典: [CARI | Internet Awesomesauce](https://cari.institute/aesthetics/internet-awesomesauce)
- Global Village Coffeehouse: `are.na/consumer-aesthetics-research-institute/global-village-coffeehouse-qbdtrttfhcw`  
  出典: [CARI | Global Village Coffeehouse](https://cari.institute/aesthetics/global-village-coffeehouse)

公式グループ: `are.na/consumer-aesthetics-research-institute`  
出典: [Consumer Aesthetics Research Institute | Are.na](https://www.are.na/consumer-aesthetics-research-institute/channels)

Aesthetics Wikiにも「CARI / are.na対応インデックス」が存在する：  
出典: [Aesthetics Wiki / Consumer Aesthetics Research Institute](https://aesthetics.fandom.com/wiki/Consumer_Aesthetics_Research_Institute)

### 6-4. BroskoskiによるEvan Collins言及

Are.na創設者自身がEvan Collinsを「最もおもしろいアカウント」として名指し：

> "The easiest one, that always gets anyone I show it to, is Evan Collins' account. He has such a fascinating way of recognizing historical trends in design. If you just browse his channels for a few minutes, you'll get the idea."  
> 出典: [Upstatement インタビュー（Charles Broskoski）](https://upstatement.com/blog/interview-with-charles-broskoski)

### 6-5. CARIとAre.naの機能分担

| 層 | 担当 |
|---|---|
| 概念・命名・テキスト解説 | cari.institute |
| 視覚資料収集・協働研究 | Are.na（各aesthetic対応チャンネル） |
| 日常的画像ストリーム | Tumblr（Collins個人: `evan-collins90.tumblr.com`） |
| 命名議論・コミュニティ投票 | Facebookグループ |
| 告知・普及 | Twitter/X（`@CARI_Institute`） |

---

## 7. Are.naの設計思想とインターネット美学研究の関係

Are.naが「インターネット美学のアーカイブ基盤」として選ばれた理由は、その設計思想と研究倫理の整合にある：

1. **SEO・アルゴリズムによる汚染がない** → 資料が「人気」ではなく「意味」で集積される
2. **広告収益モデルでない** → キュレーションが商業的誘因に歪められない
3. **「チャンネル」という単位** → aestheticごとの視覚コーパスを構造化して保持できる
4. **ブロックの相互接続性** → 異なるチャンネル間でのブロック共有により、aesthetic間の系譜関係が可視化される

Broskoskiの「考えるための空間」という設計思想は、CARIが行うような**名前のないものに名前を与える作業**——「形になっていない思考領域」を少しずつ輪郭付けていく作業——と構造的に同型である。

---

## 8. 未検証事項・要追加調査

- 【要検証】Are.naの財務透明公開ページの現在の状況（URL確認）
- 【要検証】Are.naの「いいね」機能の有無・変遷
- 【要検証】Grokipedia記事の一次資料（CARIのどの公開文書に基づくか）
- 【要追加】Are.naの創設年（▲2012年頃とされるが正確な年月要確認）
- 【要追加】Are.na APIの公開状況とCARIによる活用の有無
- 【要追加】CARI are.naグループのチャンネル総数・ブロック総数の現在値

---

## 主要一次資料リスト

| 資料 | URL | 備考 |
|---|---|---|
| Broskoski / The Creative Independent (2017) | https://thecreativeindependent.com/people/charles-broskoski-on-self-discovery-upon-revisiting-things-youve-accumulated-over-time/ | del.icio.us起源の詳述 |
| Broskoski / Upstatement インタビュー | https://upstatement.com/blog/interview-with-charles-broskoski | 広告拒否・Evan Collins言及 |
| Broskoski / Kernel Magazine | https://www.kernelmag.io/3/charles-broskoski-interview | VC拒否・慶雲館モデル |
| Broskoski / ZORA ZINE | https://zine.zora.co/arena-charles-broskoski | コミュニティファーストモデル |
| Broskoski / Substack (Dahl, 2026) | https://jdahl.substack.com/p/cab | 設計哲学の最新整理 |
| UMass Amherst / IDPI ポッドキャスト | https://publicinfrastructure.org/podcast/40-arena/ | Broskoski & Pianetti共同インタビュー |
| Evan Collins / Are.na プロフィール | https://www.are.na/evan-collins-1522646491 | "CARI work is based here on Are.na" |
| CARI 公式Are.naグループ | https://www.are.na/consumer-aesthetics-research-institute/channels | 公式グループ |
| CARI / Project History | https://cari.institute/history | CARIの年表（プラットフォーム遷移の記録） |
| CARI / FAQ | https://cari.institute/faq | "consumer aesthetic"の定義 |
| It's Nice That (2025-11) | https://www.itsnicethat.com/features/the-consumer-aesthetics-research-institute-spotlight-creative-industry-121125 | "Evan's prolific Are.na"言及 |
| Wikipedia / CARI | https://en.wikipedia.org/wiki/Consumer_Aesthetics_Research_Institute | 基本事項確認用 |

---

## 9. Are.naの「いいね」機能：不在の設計史

### 9-1. 創設当初から「いいね」なし

Are.naは**設計段階から「いいね（like）」「お気に入り（favorite）」「シェア（share）」を持たない**プラットフォームとして構築された。これは機能的な未実装ではなく、思想的な選択。

> "Are.na was built as a successor to hypertext projects like Ted Nelson's Xanadu, and as an ad-free alternative to social networks like Facebook, forgoing 'likes,' 'favorites,' or 'shares' in its design."  
> 出典: [Wikipedia / Are.na](https://en.wikipedia.org/wiki/Are.na)

> "It is a digital space to collect images, text, links, and documents, but what you collect on the site isn't about popularity: There are no 'like' buttons. That's because it was created by designers and artists who are attuned to good, ethical design."  
> 出典: [Fast Company / Co.Design, 2018-01-18（Katharine Schwab）](https://www.fastcompany.com/90157216/this-is-what-a-designer-led-social-networking-site-looks-like)

### 9-2. なぜ「いいね」がないのか：設計思想との接続

Are.naの「いいね」不在は、複数の設計原則の帰結：

1. **アルゴリズム拒否との整合**——「いいね」数はアルゴリズムによるコンテンツ推薦の入力値。これを廃することで、人気順の表面浮上を原理的に防ぐ。
2. **「考えるための道具」としての一貫性**——「いいね」は消費的・受動的関与の記録であり、「どのチャンネルにこれが属するか」という能動的キュレーション行為と相容れない。
3. **「popularity ≠ value」の価値観**——Fast Companyの記事は「what you collect is not about popularity」と明示している。

### 9-3. 変遷の記録

現時点（2026年6月）で確認できる限り、Are.naに「いいね」機能が後から追加・削除された記録は存在しない。**いいね不在は創設（2014年正式公開）から一貫した方針**と判断される。

> ▲ ただし、フォロー機能（チャンネルのフォロー）は存在する。「いいね」に類似する行為として「チャンネルをフォローする」「ブロックを別チャンネルに接続（connect）する」がある。「接続」の数はある意味で参照頻度の指標になり得るが、アルゴリズム的な表示順序への入力には使われていない（【要確認】）。

---

## 10. CARIのDiscordサーバー：設立経緯・構造・Are.naとの関係

### 10-1. Discord設立の経緯

CARIのDiscordサーバーは**2017年11月27日にFroyo Tamが創設**し、Jada Paigeが最初のメンバーとなった。

2021年5月に@Y2K_Aestheticアカウントが「CARIのDiscordを公開する」とツイートした時点で、すでに800人超のコミュニティが存在していたと報告している（招待リンク: `discord.gg/ZPTu8bZtck`）。

### 10-2. Discordサーバーの構造

CARIのDiscordは研究プラットフォームとして機能している：

> "In addition to the numerous channels for categorizing aesthetic references by period and motifs, CARI has channels for discussing retro tech, fashion, and sharing original work."  
> 出典: [virtualgoodsdealer, 2021-11-08](https://pages.virtualgoodsdealer.com/articles/2021/11/08/discord-servers-for-research-and-creative-inspiration/)

コミュニティの自己記述：「A group focused on the research and analysis of zeitgeists of consumer design. Our goal is to create a contemporary lexicon on postmodern design since 1970s to the present.」（同上）

### 10-3. Discordがnaming・term coinage の場として機能

CARI Project Historyより、Discordは**aesthetic命名の実験場・投票の場**として機能してきたことが判明：

- `2017-01-05` Froyo TamがFacebookポールで「McBling」を提案・命名（Discordより前の事例だが、命名の民主的プロセスの先例）
- Discordの「チャンネル説明文」がaesthetic定義の最初の草稿として機能してきた——後にcari.instituteへ移植

> "The goal of the Maintenance Effort began as a way to rewrite the channel descriptions in our Discord Server to help them better describe the aesthetics being discussed. As this effort grew however, it became apparent that the descriptions being written and other important metadata we gathered would require a framework to properly organize them. This eventually expanded the scope to the information we present on our website as well."  
> 出典: [CARI / Project History](https://cari.institute/history)

つまり**Discordのチャンネル説明文 → Website（cari.institute）の aesthetic記述**という知識生産フローが存在する。

### 10-4. Discord「セミプライベート化」の経緯

Maintenance Effort（2021〜2024）の期間中、CARIのDiscordはモデレーション負荷軽減のためセミプライベート化された。2024年10月12日にMaintenance Effortが一段落し（92aestheticsのうち58のチャンネル説明を改訂）、その後も継続的な整備が行われている。

### 10-5. DiscordとAre.naの機能的役割分担

CARIにおけるDiscordとAre.naの分担を整理すると以下のようになる：

| プラットフォーム | 主な機能 | 性質 |
|---|---|---|
| **Are.na** | 視覚資料（ブロック）のアーカイブ・aesthetic別チャンネル管理 | 静的・参照的・公開 |
| **Discord** | リアルタイム議論・命名投票・新aesthetic提案・Maintenance Effort | 動的・会話的・コミュニティ参加 |
| **cari.institute** | 確定した定義・命名帰属・公式テキスト公開 | 静的・規範的・公開 |
| **Facebook グループ** | 初期期（〜2017年頃）の議論場。現在は補助的 | 歴史的・漸減 |

重要な点：Discordは**研究プロセスの「生きた議論」の場**であり、Are.naは**その成果物（視覚コーパス）の保存場**として機能している。Discordで生まれた定義がAre.naのチャンネル説明に結晶し、さらにcari.instituteの公式ページへと昇格するという**三段階の知識生産フロー**が読み取れる。

### 10-6. 発見の帰属とDiscordコミュニティ

CARIのWebサイトには発見者クレジットにDiscordメンバーが明示されることがある：

> "1978 magazine ads for Wega audio gear by Hartmut Esslinger / Frog Design-- A gorgeous example of 'cassette futurism.' **Thanks to CommodoreCoCo in the CARI Discord for finding these!**"  
> 出典: [CARI / Cohost](https://cohost.org/CARI)（CARI公式SNS投稿）

これはDiscordが単なる会話空間ではなく、**資料発見・共有の実践コミュニティ**として機能していることを示す。

---

## 11. 未検証事項の更新

- [更新] Are.naの「いいね」機能：**創設時から不在、変遷なし**と判断（Wikipedia・Fast Company記事で確認）
- 【要確認】Are.naの「接続（connect）」数がアルゴリズムに入力されているかどうか
- 【要確認】CARIのDiscordサーバーの現在の公開状況（完全公開 / セミプライベート / 招待制）
- 【要追加】Maintenance Effort後（2024年10月以降）のDiscord運営体制の変化
- 【要追加】Are.naとDiscordの間で資料が「橋渡し」される具体的なワークフローの一次証言

---

## 更新された主要資料リスト（追加分）

| 資料 | URL | 備考 |
|---|---|---|
| Wikipedia / Are.na | https://en.wikipedia.org/wiki/Are.na | 「いいね」不在の公式記述・創設者・年表 |
| Fast Company / Co.Design (2018) | https://www.fastcompany.com/90157216/this-is-what-a-designer-led-social-networking-site-looks-like | "no like buttons"の明示 |
| Are.na / About | https://www.are.na/about | 財務透明性・ミッション記述 |
| CARI / Project History | https://cari.institute/history | Discord設立日・Maintenance Effort詳細 |
| Y2K Aesthetic / Twitter (2021-05-17) | https://x.com/y2k_aesthetic/status/1394004726660882433 | Discord公開告知・800人超の記録 |
| virtualgoodsdealer (2021-11-08) | https://pages.virtualgoodsdealer.com/articles/2021/11/08/discord-servers-for-research-and-creative-inspiration/ | CARIサーバーの構造説明 |
| CARI / Cohost | https://cohost.org/CARI | Discordメンバーへの帰属クレジット事例 |
