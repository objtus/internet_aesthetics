# Nanoformats（ナノフォーマット）の概要と歴史

## 1. Nanoformatsとは

Nanoformats（ナノフォーマット）とは、Twitter（現X）などのマイクロブログサービス上の短いテキスト投稿（140文字以内）に**セマンティック（意味的）な情報を付加するための軽量な記法・規約**のことである。

Microformats（マイクロフォーマット）がHTMLに構造化データを埋め込む手法であるのに対し、Nanoformatsはさらに制約の厳しいマイクロブログの短文テキスト向けに設計された派生概念である。

> 参照: [microformats.org/wiki/microblogging-nanoformats](http://microformats.org/wiki/microblogging-nanoformats)

---

## 2. 詳細年表

### 前史：HTMLセマンティクスの萌芽（2000〜2003年）

|日付|出来事|
|---|---|
|**2000-03-21**|Dan ConnollyがW3Cメーリングリストで「XHTMLをデータのプライマリソースとして使うべき」と提唱。データベース・RDF・XMLではなくHTMLを主要データソースとする考え方の最初期の記録。|
|**2003-03-11**|Tantek Çelikが SXSW Interactive「Beyond the Blog」セッションにて、ブログロールのリンクに `rel="friend"` を使うことを提案。将来のGMPG共同創設者Matthew Mullenweg（後のWordPress創設者）の隣で発言。|
|**2003-03-14**|Kevin Marksが Vote Links を提案。|

> 参照: [microformats.org/wiki/history-of-microformats](https://microformats.org/wiki/history-of-microformats)

---

### Microformatsの確立（2004〜2005年）

|日付|出来事|
|---|---|
|**2004-02-11**|Tantek Çelikが「lowercase semantic web（小文字のセマンティックウェブ）」概念を公開定義。同日、O'Reilly ETechにてTantek ÇelikとKevin Marksが「real world semantics」プレゼンを発表。`rel-license` の一般公開も同日。|
|**2004-08-16**|Tantek Çelik、Eric Meyer、Matt MullenweggがXFN 1.1を策定。|
|**2004-09-11**|hCalendar が構想・導入される（同月30日にブログ掲載）。hCardも同時期に構想。|
|**2004-09-30**|hCard という用語がウェブ上で正式に定義・公開される。|
|**2005-06-20**|Dan CederholmとTantek Çelikの協力により **microformats.org** が正式に開設。「人間のために設計され、機械にも読めるオープンなデータフォーマットの集合体」として定義される。hCard・hCalendarなど主要仕様が公開。|

> 参照: [microformats.org/wiki/history-of-microformats](https://microformats.org/wiki/history-of-microformats)  
> 参照: [microformats.org/wiki/hcard-history](http://microformats.org/wiki/hcard-history)  
> 参照: [microformats.org/wiki/what-are-microformats](http://microformats.org/wiki/what-are-microformats)

---

### Twitterの誕生（2006年）

|日付|出来事|
|---|---|
|**2006-02**|Jack DorseyらOdeo社内でTwitter（当初のコードネーム「twttr」）の開発開始。|
|**2006-03-21**|Jack Dorseyが最初のツイート「just setting up my twttr」を投稿（午前9時50分）。|
|**2006-07-15**|Twitterが一般公開される。|
|**2006-10**|Biz Stone・Evan Williams・Dorsey他がObvious Corporationを設立し、OdeoからTwitterを買収。|

> 参照: [en.wikipedia.org/wiki/History_of_Twitter](https://en.wikipedia.org/wiki/History_of_Twitter)  
> 参照: [en.wikipedia.org/wiki/Twitter](https://en.wikipedia.org/wiki/Twitter)  
> 参照: [computerhistory.org – March 21 This Day in History](https://www.computerhistory.org/tdih/march/21/)

---

### ハッシュタグの誕生とNanoformatsの提案（2007年）

|日付|出来事|
|---|---|
|**2007-03**|SXSWi（South by Southwest Interactive）でTwitterが爆発的注目を集める。1日あたりのツイート数が20,000件から60,000件に急増。|
|**2007-08-23**|Chris Messina（テクノロジーコンサルタント・オープンソースアドボケイト）が「How do you feel about using # (pound) for groups. As in #barcamp [msg]?」とツイートし、**ハッシュタグの使用を提案**。IRCのチャンネル命名規則にヒントを得たもの。Twitterの共同創設者Biz Stoneに直接売り込みに行ったが、当初は「ニッチすぎる」と却下される。|
|**2007-08-25**|Chris Messinaがハッシュタグの詳細提案をブログ記事（約2,000語）として公開。|
|**2007-08-26**|Stowe Boydがブログ記事「Hash Tags = Twitter Groupings」を公開。"hash tag" という用語の最初の公開使用とされる（米国方言協会辞書学者Ben Zimmerによる認定）。|
|**2007-10**|カリフォルニア州サンディエゴで大規模山火事が発生。MessinaがFlickrタグ「sandiegofire」の使用を呼びかけ、ハッシュタグが**初めて実用的な集合知ツールとして機能する転換点**となる。|
|**2007年後半**|Gorka Julio（Elurnet Informatika Zerbitzuak S.L.、スペイン・バスク）がMicroformats Wikiに **Nanoformats仕様の草案**を投稿。Twitterにおける自然発生的な慣習（`@username`・位置情報共有など）を体系化する試み。仕様はパブリックドメインとして公開。|

> 参照: [en.wikipedia.org/wiki/Chris_Messina_(open-source_advocate)](https://en.wikipedia.org/wiki/Chris_Messina_\(open-source_advocate\))  
> 参照: [en.wikipedia.org/wiki/Hashtag](https://en.wikipedia.org/wiki/Hashtag)  
> 参照: [buffer.com – A Concise History of Twitter Hashtags](https://buffer.com/resources/a-concise-history-of-twitter-hashtags-and-how-you-should-use-them-properly/)  
> 参照: [cnbc.com – How Chris Messina got Twitter to use the hashtag](https://www.cnbc.com/2020/01/09/how-chris-messina-got-twitter-to-use-the-hashtag.html)  
> 参照: [microformats.org/wiki/microblogging-nanoformats](http://microformats.org/wiki/microblogging-nanoformats)

---

### Nanoformats仕様の公開と展開（2008年）

|日付|出来事|
|---|---|
|**2008-01-07**|Microformats WikiにNanoformatsのフランス語版（`twitter-nanoformats-fr`）ページが作成・公開。仕様の国際的広がりを示す。|
|**2008-04-11**|Microformats Wiki上の `twitter-nanoformats` ページ（`microblogging-nanoformats`へのリダイレクト）が最終更新。|
|**2008年**|Nanoformats仕様に対応するツール群が登場：Txioka（NanoformatsをhCalendar等Microformatsに変換）、plusplus bot（`tag++`/`tag--`投票）、foamee（@usernameフィルタ）など。|
|**2008年**|`tag:` ナノフォーマットが廃止され、`#tag`（ハッシュタグ）記法に統一されることが承認。`http://hashtags.org/` による実績がこの移行を後押しした。|
|**2008-06**|BBCがアクセシビリティ上の懸念からMicroformats（abbrデザインパターン）の使用を中止すると発表。Microformats自体の設計上の課題も議論され始める。|
|**2008年**|Sarven CapadisliがMicroformats仕様に `in-reply-to` の追加を提案（Atom仕様拡張 RFC 4685 にヒントを得たもの）。|

> 参照: [microformats.org/wiki/twitter-nanoformats-fr](http://microformats.org/wiki/twitter-nanoformats-fr)  
> 参照: [microformats.org/wiki/twitternanoformats](http://microformats.org/wiki/twitternanoformats)  
> 参照: [microformats.org/wiki/microblogging-nanoformats](http://microformats.org/wiki/microblogging-nanoformats)  
> 参照: [en.wikipedia.org/wiki/Microformat](https://en.wikipedia.org/wiki/Microformat)  
> 参照: [book.micro.blog/microformats/](https://book.micro.blog/microformats/)

---

### ハッシュタグの公式採用とその後（2009年〜）

|日付|出来事|
|---|---|
|**2009**|2009〜2010年のイラン選挙抗議運動でハッシュタグが国際的に広まる。**Twitterがハッシュタグをクリッカブルリンクとして公式採用**し、Trending Topics（トレンド）機能も追加。|
|**2010-05-02**|microformats2（mf2）がFOO East 2010のディスカッションセッションで提案・概念化される。|
|**2014-06**|「hashtag」という語がオックスフォード英語辞典に正式収録。定義：「ソーシャルメディアで同じテーマのメッセージを検索しやすくするために、単語やフレーズの前に付ける # 記号」。|
|**2018**|インターネット上位50サイトの85%以上でハッシュタグが使用されていることが確認される。|
|**2020**|GoogleがコンテンツインデックスのためにMicroformatsを引き続きパースしていることを公式確認。|

> 参照: [en.wikipedia.org/wiki/Hashtag](https://en.wikipedia.org/wiki/Hashtag)  
> 参照: [fortune.com – Twitter hashtag creator says goodbye](https://fortune.com/2023/04/19/twitter-hashtag-creator-says-goodbye-chris-messina/)  
> 参照: [en.wikipedia.org/wiki/Microformat](https://en.wikipedia.org/wiki/Microformat)  
> 参照: [microformats.org/wiki/history-of-microformats](https://microformats.org/wiki/history-of-microformats)

---

## 3. Nanoformatsの主な記法と仕様

|記法|用途|例|
|---|---|---|
|`@username`|ユーザーへのメンション・返信|`@mike 同意します`|
|`#tag`|タグ付け（ハッシュタグ）※`tag:`を置き換え|`コンサート #music`|
|`L:`|現在地の共有|`L:Ondarreta beach, Donostia`|
|`event:`|イベント情報|`event:party`|
|`time:`|時刻情報|`time:2007-06-24 21:00`|
|`lang:`|投稿の言語定義|`lang:ja`|
|`tag++` / `tag--`|賛成・反対投票|`microformats++`|

**記法の利用ルール（抜粋）**

- 同じ種類のNanoformatを1つの投稿に複数使わない（`#tag`は例外）。
- `@username` は投稿の先頭に置くのが慣例。
- Nanoformatは組み合わせて使える（例：`@teketen 今夜パーティー time:2007-06-24 21:00 L:Ondarreta beach #party`）。

> 参照: [microformats.org/wiki/microblogging-nanoformats](http://microformats.org/wiki/microblogging-nanoformats)

---

## 4. 歴史の流れ（まとめ）

```
2000-03-21  HTMLをプライマリデータソースとする考え方の提唱（Dan Connolly）
     ↓
2003-03-11  rel="friend" の提案（Tantek Çelik @ SXSW）
     ↓
2004-02-11  "lowercase semantic web" 公開・ETech プレゼン
     ↓
2004-09-30  hCard 公開
     ↓
2005-06-20  microformats.org 正式開設
     ↓
2006-03-21  Twitterの最初のツイート（Jack Dorsey）
     ↓
2006-07-15  Twitter 一般公開
     ↓
2007-08-23  ハッシュタグ提案（Chris Messina）
     ↓
2007-08-26  "hash tag" という語が初めて公開使用（Stowe Boyd）
     ↓
2007-10    サンディエゴ山火事でハッシュタグが実用化
     ↓
2007年後半  Nanoformats仕様 Microformats Wiki に登場（Gorka Julio）
     ↓
2008-01-07  Nanoformats仏語版ページ公開
     ↓
2008-04-11  Nanoformats twitter-nanoformats ページ最終更新
     ↓
2009       Twitter がハッシュタグを公式採用・Trending Topics 導入
     ↓
2010-05-02  Microformats 2（mf2）提案
     ↓
2014-06    "hashtag" がオックスフォード英語辞典に収録
```

---

## 5. 参考URL一覧

|内容|URL|
|---|---|
|Microblogging Nanoformats（仕様本文）|http://microformats.org/wiki/microblogging-nanoformats|
|Twitter Nanoformats（リダイレクト元）|http://microformats.org/wiki/twitter-nanoformats|
|Nanoformats仏語版|http://microformats.org/wiki/twitter-nanoformats-fr|
|Microformatsの歴史|https://microformats.org/wiki/history-of-microformats|
|hCard 歴史|http://microformats.org/wiki/hcard-history|
|Microformatsとは|http://microformats.org/wiki/what-are-microformats|
|Twitter Syntax – Microformats Wiki|https://microformats.org/wiki/twitter-syntax|
|Wikipedia – Microformat|https://en.wikipedia.org/wiki/Microformat|
|Wikipedia – Hashtag|https://en.wikipedia.org/wiki/Hashtag|
|Wikipedia – Chris Messina|https://en.wikipedia.org/wiki/Chris_Messina_(open-source_advocate)|
|Wikipedia – History of Twitter|https://en.wikipedia.org/wiki/History_of_Twitter|
|Wikipedia – Twitter|https://en.wikipedia.org/wiki/Twitter|
|Computer History Museum – First Tweet|https://www.computerhistory.org/tdih/march/21/|
|Buffer – History of Twitter Hashtags|https://buffer.com/resources/a-concise-history-of-twitter-hashtags-and-how-you-should-use-them-properly/|
|CNBC – How Chris Messina got Twitter to use the hashtag|https://www.cnbc.com/2020/01/09/how-chris-messina-got-twitter-to-use-the-hashtag.html|
|book.micro.blog – Microformats|https://book.micro.blog/microformats/|
|TwitLogic（RDF変換ツール）|https://laurensgoessemantic.wordpress.com/2010/10/24/twitlogic/|