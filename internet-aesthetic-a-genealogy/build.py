#!/usr/bin/env python3
"""manuscript/*.md → internet-aesthetic-a-genealogy/*.html 変換スクリプト。

出力先フォルダを txt/ 配下へそのままコピーして公開する想定。
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DEPLOY_DIR = Path(__file__).resolve().parent
MANUSCRIPT = ROOT / "manuscript"
IMG_SRC = ROOT / "img"
IMG_DST = DEPLOY_DIR / "img"

# txt/internet-aesthetic-a-genealogy/ からの相対パス
SITE_ROOT = "../.."
TXT_ROOT = ".."
INDEX_PAGE = "index.html"
IMG_PREFIX = "img"
IMG_SIZE = 'width="500" height="500"'

CHAPTERS = [
    {
        "source": "序文.md",
        "output": "intro.html",
        "title": "序文",
        "short": "序文",
        "prev": None,
        "prev_label": None,
        "next": "ch01.html",
        "next_label": "第1章　土壌",
    },
    {
        "source": "第1章_土壌.md",
        "output": "ch01.html",
        "title": "第1章　土壌——Tumblrとフォークソノミー",
        "short": "第1章　土壌",
        "prev": "intro.html",
        "prev_label": "序文",
        "next": "ch02.html",
        "next_label": "第2章　シーンと土壌",
    },
    {
        "source": "第2章_シーンと土壌.md",
        "output": "ch02.html",
        "title": "第2章　シーンと土壌",
        "short": "第2章　シーンと土壌",
        "prev": "ch01.html",
        "prev_label": "第1章　土壌",
        "next": "ch03.html",
        "next_label": "第3章　命名の時代",
    },
    {
        "source": "第3章_命名の時代.md",
        "output": "ch03.html",
        "title": "第3章　命名の時代",
        "short": "第3章　命名の時代",
        "prev": "ch02.html",
        "prev_label": "第2章　シーンと土壌",
        "next": "ch04.html",
        "next_label": "第4章　lo-fiとHD",
    },
    {
        "source": "第4章_lo-fiとHD.md",
        "output": "ch04.html",
        "title": "第4章　lo-fiとHD",
        "short": "第4章　lo-fiとHD",
        "prev": "ch03.html",
        "prev_label": "第3章　命名の時代",
        "next": "ch05.html",
        "next_label": "第5章　aestheticという語",
    },
    {
        "source": "第5章_aestheticという語.md",
        "output": "ch05.html",
        "title": "第5章　「aesthetic」という語——包含関係の逆転",
        "short": "第5章　aestheticという語",
        "prev": "ch04.html",
        "prev_label": "第4章　lo-fiとHD",
        "next": "ch06.html",
        "next_label": "第6章　名前があとから来る",
    },
    {
        "source": "第6章_名前があとから来る.md",
        "output": "ch06.html",
        "title": "第6章　名前があとから来る（2015〜2019年）",
        "short": "第6章　名前があとから来る",
        "prev": "ch05.html",
        "prev_label": "第5章　aestheticという語",
        "next": "ch07.html",
        "next_label": "第7章　爆発",
    },
    {
        "source": "第7章_爆発.md",
        "output": "ch07.html",
        "title": "第7章　爆発（2020〜2021年）",
        "short": "第7章　爆発",
        "prev": "ch06.html",
        "prev_label": "第6章　名前があとから来る",
        "next": "ch08.html",
        "next_label": "第8章　制度化",
    },
    {
        "source": "第8章_制度化.md",
        "output": "ch08.html",
        "title": "第8章　制度化：分類するという欲望",
        "short": "第8章　制度化",
        "prev": "ch07.html",
        "prev_label": "第7章　爆発",
        "next": None,
        "next_label": None,
    },
]

CHAPTER_H1_RE = re.compile(r"^#\s+第\d+章.+$", re.MULTILINE)
TIME_AXIS_RE = re.compile(r"^\*\*時間軸：(.+?)\*\*\s*$", re.MULTILINE)
EXTERNAL_LINK_RE = re.compile(r'<a href="(https?://[^"]+)"')
URL_IN_TEXT_RE = re.compile(r"https?://[^\s<>\"'）)]+")
STANDALONE_IMAGE_RE = re.compile(r"^!\[([^\]]*)\]\((img/[^)]+)\)\s*$")
LINKED_IMAGE_RE = re.compile(
    r"^\[!\[([^\]]*)\]\((img/[^)]+)\)\]\((https?://[^)]+)\)\s*$"
)
COMMENT_LINE_RE = re.compile(r"^<!--(.*?)-->\s*$")
HEADING_ID_RE = re.compile(r"\s*\{#([a-zA-Z0-9_-]+)\}\s*$")


def extract_urls(text: str) -> list[str]:
    seen: set[str] = set()
    urls: list[str] = []
    for url in URL_IN_TEXT_RE.findall(text):
        url = url.rstrip(".,;:")
        if url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def comment_prose(text: str) -> str:
    prose = URL_IN_TEXT_RE.sub("", text)
    prose = re.sub(r"\s+", " ", prose).strip()
    return prose


def source_link_label(url: str) -> str:
    host = urlparse(url).netloc.removeprefix("www.")
    if host == "web.archive.org":
        return "Internet Archive"
    return host or "キャプチャ元"


def render_figure_html(
    alt: str,
    img_path: str,
    comment_lines: list[str],
    *,
    link_href: str | None = None,
) -> str:
    src = f"{IMG_PREFIX}/{Path(img_path).name}" if img_path.startswith("img/") else img_path
    alt_esc = html.escape(alt)

    notes: list[str] = []
    urls: list[str] = []
    if link_href:
        urls.append(link_href)
    for line in comment_lines:
        urls.extend(extract_urls(line))
        prose = comment_prose(line)
        if prose:
            notes.append(prose)

    # URL 重複除去（出現順維持）
    seen: set[str] = set()
    unique_urls: list[str] = []
    for url in urls:
        if url not in seen:
            seen.add(url)
            unique_urls.append(url)

    if link_href:
        href = html.escape(link_href, quote=True)
    else:
        href = src

    parts = [
        '<figure class="fig-screenshot">',
        f'  <a href="{href}">',
        f'    <img src="{src}" alt="{alt_esc}" {IMG_SIZE} loading="lazy" />',
        "  </a>",
        "  <figcaption>",
        f"    <p>{alt_esc}</p>",
    ]
    for note in notes:
        parts.append(f'    <p class="fig-note">{html.escape(note)}</p>')
    for url in unique_urls:
        label = html.escape(source_link_label(url))
        url_esc = html.escape(url, quote=True)
        parts.extend(
            [
                '    <p class="fig-source">',
                f'      <a href="{url_esc}">{label}</a>',
                "    </p>",
            ]
        )
    parts.extend(["  </figcaption>", "</figure>"])
    return "\n".join(parts)


def preprocess_figures(text: str) -> str:
    """画像（単体・リンク付き）と直後コメントを figure/figcaption へ変換する。"""
    lines = text.split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        lm = LINKED_IMAGE_RE.match(line)
        if lm:
            alt, img_path, link_url = lm.group(1), lm.group(2), lm.group(3)
            i += 1
            comment_lines: list[str] = []
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped == "":
                    i += 1
                    continue
                cm = COMMENT_LINE_RE.match(stripped)
                if cm:
                    comment_lines.append(cm.group(1).strip())
                    i += 1
                    continue
                break
            out.append(render_figure_html(alt, img_path, comment_lines, link_href=link_url))
            continue
        m = STANDALONE_IMAGE_RE.match(line)
        if m and not line.lstrip().startswith("[!"):
            alt, img_path = m.group(1), m.group(2)
            i += 1
            comment_lines: list[str] = []
            while i < len(lines):
                stripped = lines[i].strip()
                if stripped == "":
                    i += 1
                    continue
                cm = COMMENT_LINE_RE.match(stripped)
                if cm:
                    comment_lines.append(cm.group(1).strip())
                    i += 1
                    continue
                break
            out.append(render_figure_html(alt, img_path, comment_lines))
            continue
        out.append(line)
        i += 1
    return "\n".join(out)


def preprocess_md(text: str) -> tuple[str | None, str]:
    time_axis = None
    m = TIME_AXIS_RE.search(text)
    if m:
        time_axis = m.group(1).strip()
        text = TIME_AXIS_RE.sub("", text, count=1)

    text = CHAPTER_H1_RE.sub("", text)
    text = preprocess_figures(text.strip())
    return time_axis, text


def pandoc_html_fragment(md: str) -> str:
    if not md.strip():
        return ""
    result = subprocess.run(
        ["pandoc", "--from=markdown", "--to=html", "--wrap=none"],
        input=md,
        capture_output=True,
        text=True,
        check=True,
        encoding="utf-8",
    )
    html = result.stdout.strip()
    html = re.sub(r"</?p>\s*$", "", html) if html.startswith("<p>") else html
    return html


def normalize_img_tags(html: str) -> str:
    """すべての img に width/height を付与する。"""

    def repl(m: re.Match[str]) -> str:
        attrs = m.group(1)
        attrs = re.sub(r'\s*width="[^"]*"', "", attrs)
        attrs = re.sub(r'\s*height="[^"]*"', "", attrs)
        attrs = attrs.strip()
        if attrs:
            return f"<img {IMG_SIZE} {attrs} />"
        return f"<img {IMG_SIZE} />"

    return re.sub(r"<img\s([^>]*?)\s*/>", repl, html)


def postprocess_html(html: str) -> str:
    html = html.replace("(img/", f"({IMG_PREFIX}/")
    html = html.replace('src="img/', f'src="{IMG_PREFIX}/')
    html = html.replace('href="img/', f'href="{IMG_PREFIX}/')

    def add_link_attrs(m: re.Match[str]) -> str:
        tag = m.group(0)
        if "target=" in tag:
            return tag
        url = m.group(1)
        return f'<a href="{url}" target="_blank" rel="noopener"'

    html = EXTERNAL_LINK_RE.sub(add_link_attrs, html)

    # Pandoc 生成 figure：aria-hidden を外し、Luminous 用にリンクで包む
    html = re.sub(
        rf'<figure><img src="({IMG_PREFIX}/[^"]+)" alt="([^"]*)" /><figcaption aria-hidden="true">([^<]*)</figcaption></figure>',
        rf'<figure class="fig-screenshot"><a href="\1"><img src="\1" alt="\2" loading="lazy" /></a><figcaption><p>\3</p></figcaption></figure>',
        html,
    )
    html = re.sub(
        rf'<figure><img src="({IMG_PREFIX}/[^"]+)" alt="([^"]*)" />',
        rf'<figure class="fig-screenshot"><a href="\1"><img src="\1" alt="\2" loading="lazy" /></a>',
        html,
    )
    html = re.sub(
        rf'<p><img src="({IMG_PREFIX}/[^"]+)" alt="([^"]*)" /></p>',
        rf'<p><a href="\1"><img src="\1" alt="\2" loading="lazy" /></a></p>',
        html,
    )
    html = re.sub(
        rf'<p><img src="({IMG_PREFIX}/[^"]+)" alt="([^"]*)" />',
        rf'<p><a href="\1"><img src="\1" alt="\2" loading="lazy" /></a>',
        html,
    )
    return normalize_img_tags(html)


def parse_heading_line(raw: str) -> tuple[str, str | None]:
    """見出し行から表示テキストと `{#slug}` を取り出す。"""
    m = HEADING_ID_RE.search(raw)
    if not m:
        return raw.strip(), None
    slug = m.group(1)
    title = HEADING_ID_RE.sub("", raw).strip()
    return title, slug


def make_slug(title: str, used: set[str], explicit: str | None = None) -> str:
    """見出しテキストからページ内一意の id を生成する。"""
    if explicit:
        base = explicit
    else:
        latin = re.findall(r"[A-Za-z0-9]+", title)
        if sum(len(part) for part in latin) >= 2:
            base = "-".join(part.lower() for part in latin)
            base = re.sub(r"-+", "-", base).strip("-")[:60]
        else:
            fragment = pandoc_html_fragment(f"## {title}")
            match = re.search(r'\sid="([^"]+)"', fragment)
            base = match.group(1) if match else "section"
    slug = base
    n = 2
    while slug in used:
        slug = f"{base}-{n}"
        n += 1
    used.add(slug)
    return slug


def render_heading_html(title: str, level: int, slug: str) -> str:
    title_esc = html.escape(title)
    slug_esc = html.escape(slug, quote=True)
    return (
        f'<h{level} class="heading_title">{title_esc}'
        f'<a href="#{slug_esc}" class="header-link">§</a></h{level}>'
    )


def md_to_html(md: str) -> str:
    if not md.strip():
        return ""
    return postprocess_html(pandoc_html_fragment(md))


FIGURE_BLOCK_RE = re.compile(
    r'<figure class="fig-screenshot">\s*'
    r'<a href="([^"]+)"(?:[^>]*)>\s*'
    r'(<img\s[^>]+/>)\s*'
    r"</a>\s*"
    r"<figcaption>(.*?)</figcaption>\s*"
    r"</figure>",
    re.DOTALL,
)
FIGCAPTION_P_RE = re.compile(r'<p(?: class="([^"]*)")?>(.*?)</p>', re.DOTALL)


def format_figure_lines(figure_html: str, indent: str) -> list[str]:
    """figure 内をネストに合わせてインデントする。"""
    m = FIGURE_BLOCK_RE.search(figure_html.strip())
    if not m:
        spaced = re.sub(r">\s*<", ">\n<", figure_html.strip())
        return [f"{indent}{line.strip()}" for line in spaced.split("\n") if line.strip()]

    href, img_tag, cap_html = m.group(1), m.group(2).strip(), m.group(3)
    i2 = indent + "  "
    i3 = indent + "    "
    i4 = indent + "      "
    link_attrs = ' target="_blank" rel="noopener"' if href.startswith("http") else ""

    lines = [
        f'{indent}<figure class="fig-screenshot">',
        f'{i2}<a href="{href}"{link_attrs}>',
        f"{i3}{img_tag}",
        f"{i2}</a>",
        f"{i2}<figcaption>",
    ]

    for pm in FIGCAPTION_P_RE.finditer(cap_html):
        cls, inner = pm.group(1), pm.group(2).strip()
        if cls == "fig-source":
            lines.append(f'{i3}<p class="fig-source">')
            lines.append(f"{i4}{inner}")
            lines.append(f"{i3}</p>")
        elif cls:
            lines.append(f'{i3}<p class="{cls}">{inner}</p>')
        else:
            lines.append(f"{i3}<p>{inner}</p>")

    lines.extend([f"{i2}</figcaption>", f"{indent}</figure>"])
    return lines


def format_fragment(fragment: str, indent: str) -> list[str]:
    if not fragment.strip():
        return []
    fragment = fragment.strip()
    parts = re.split(
        r'(<figure class="fig-screenshot">.*?</figure>)', fragment, flags=re.DOTALL
    )
    lines: list[str] = []
    for part in parts:
        if not part.strip():
            continue
        if part.startswith('<figure class="fig-screenshot">'):
            lines.extend(format_figure_lines(part, indent))
        else:
            spaced = re.sub(r">\s*<", ">\n<", part)
            lines.extend(
                f"{indent}{line.strip()}" for line in spaced.split("\n") if line.strip()
            )
    return lines


def parse_md_blocks(text: str, md_level: int) -> list[tuple[str, str | None, str]]:
    """`{'#' * md_level} 見出し` で分割。(見出し, slug, 本文) のリスト。"""
    prefix = "#" * md_level + " "
    parts = re.split(r"\n(?=" + re.escape(prefix) + r")", text.strip())
    blocks: list[tuple[str, str | None, str]] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if part.startswith(prefix):
            lines = part.split("\n", 1)
            title, slug = parse_heading_line(lines[0][len(prefix) :].strip())
            body = lines[1].strip() if len(lines) > 1 else ""
            blocks.append((title, slug, body))
        else:
            blocks.append(("", None, part))
    return blocks


def render_section(
    heading: str,
    html_level: int,
    body: str,
    slug_used: set[str],
    indent: str,
    next_md_level: int,
    heading_slug: str | None = None,
    toc_entries: list[tuple[str, str]] | None = None,
) -> str:
    slug = make_slug(heading, slug_used, explicit=heading_slug)
    if html_level == 2 and toc_entries is not None:
        toc_entries.append((slug, heading))
    slug_attr = html.escape(slug, quote=True)
    lines = [
        f'{indent}<section id="{slug_attr}">',
        f"{indent}  {render_heading_html(heading, html_level, slug)}",
    ]

    sub_blocks = parse_md_blocks(body, next_md_level)
    if len(sub_blocks) == 1 and sub_blocks[0][0] == "":
        lines.extend(format_fragment(md_to_html(body), indent + "  "))
    else:
        prev_was_section = False
        for sub_heading, sub_slug, sub_body in sub_blocks:
            if not sub_heading:
                lines.extend(format_fragment(md_to_html(sub_body), indent + "  "))
                prev_was_section = False
            else:
                if prev_was_section:
                    lines.append("")
                lines.append(
                    render_section(
                        sub_heading,
                        html_level + 1,
                        sub_body,
                        slug_used,
                        indent + "  ",
                        next_md_level + 1,
                        heading_slug=sub_slug,
                        toc_entries=toc_entries,
                    ).rstrip("\n")
                )
                prev_was_section = True

    lines.append(f"{indent}</section>")
    return "\n".join(lines) + "\n"


def build_body(
    time_axis: str | None, text: str, page_title: str, *, is_intro: bool
) -> tuple[str, list[tuple[str, str]]]:
    slug_used: set[str] = set()
    toc_entries: list[tuple[str, str]] = []
    chunks: list[str] = []
    if time_axis:
        chunks.append(f'        <p class="time-axis"><em>時間軸：{time_axis}</em></p>\n')

    if is_intro:
        text = re.sub(r"^## 序文\s*\n", "", text.strip())
        top_md_level = 3
        html_level = 2
    else:
        top_md_level = 2
        html_level = 2

    for heading, heading_slug, body in parse_md_blocks(text, top_md_level):
        if heading:
            if is_intro or heading != page_title:
                section = render_section(
                    heading,
                    html_level,
                    body,
                    slug_used,
                    "        ",
                    top_md_level + 1,
                    heading_slug=heading_slug,
                    toc_entries=toc_entries,
                )
                if chunks and chunks[-1].rstrip().endswith("</section>"):
                    chunks.append("\n")
                chunks.append(section)
        elif body:
            lines = format_fragment(md_to_html(body), "        ")
            if lines:
                chunks.append("\n".join(lines) + "\n")

    return "".join(chunks), toc_entries


def render_toc_nav(toc_entries: list[tuple[str, str]]) -> str:
    """h2 見出しからページ内目次ナビを生成する。"""
    if not toc_entries:
        return ""
    items = "\n".join(
        f'            <li><a href="#{html.escape(slug, quote=True)}">{html.escape(title)}</a></li>'
        for slug, title in toc_entries
    )
    return f"""        <nav id="toc" aria-label="目次">
          <ol id="toc-list">
{items}
          </ol>
        </nav>
"""


def chapter_nav(ch: dict) -> str:
    prev_part = (
        f'<a href="{ch["prev"]}">← {ch["prev_label"]}</a>'
        if ch["prev"]
        else "　"
    )
    next_part = (
        f'<a href="{ch["next"]}">{ch["next_label"]} →</a>'
        if ch["next"]
        else "　"
    )
    return f"""        <nav class="chapter-nav" aria-label="章ナビゲーション">
          <p><a href="{INDEX_PAGE}">目次</a></p>
          <p>{prev_part}　|　{next_part}</p>
        </nav>
"""


def page_id(ch: dict) -> str:
    """intro.html → intro, ch01.html → ch01"""
    return Path(ch["output"]).stem


def render_page(ch: dict, body: str, toc_entries: list[tuple[str, str]]) -> str:
    title = ch["title"]
    pid = page_id(ch)
    page_title = f"{pid} - IA a genealogy - 100%health"
    toc_nav = render_toc_nav(toc_entries)
    return f"""<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{page_title}</title>
  <link rel="stylesheet" href="{SITE_ROOT}/1column.css">
  <link rel="stylesheet" href="./text.css">
  <link rel="icon" type="image/svg+xml" href="/favicon.svg">
  <script src="{SITE_ROOT}/js/jquery-3.6.0.min.js"></script>
  <script src="{SITE_ROOT}/js/main.js"></script>
  <script src="/js/mouse.js" defer></script>

</head>

<body>
  <div id="wrapper">
    <header id="header">
      <div id="header-flex">
        <nav id="back" aria-label="戻るナビゲーション">
          <a id="backicon" href="{INDEX_PAGE}">
            &lt;
          </a>
        </nav>
        <nav id="address" class="addressbar" aria-label="パンくずナビゲーション">
          <ol class="breadcrumb">
            <li><a href="{SITE_ROOT}/index.html">100%health</a></li>
            <li><a href="{TXT_ROOT}/txt_main.html">txt</a></li>
            <li><a href="{INDEX_PAGE}">internet aesthetic: a genealogy</a></li>
            <li aria-current="page">{pid}</li>
          </ol>
        </nav>
      </div>
    </header>
    <main id="main">
      <header id="category-header">
        <nav aria-label="カテゴリナビゲーション">
          <ol class="main-category">
            <li><a href="/aboutme.html">about</a></li>
            <li><a href="/gallery/gallery_main.html">gallery</a></li>
            <li><a href="/works/works_main.html">works</a></li>
            <li><a href="/txt/txt_main.html">txt</a></li>
            <li><a href="/links/links_main.html">links</a></li>
            <li><a href="/misc/index.html">misc</a></li>
          </ol>
          <ol class="sub-category">
            <li><a href="/txt/txt_main.html">txt</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/index.html">internet aesthetic: a genealogy</a></li>
          </ol>
          <ol class="sub-category">
            <li><a href="/txt/internet-aesthetic-a-genealogy/intro.html">intro</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch01.html">ch01</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch02.html">ch02</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch03.html">ch03</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch04.html">ch04</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch05.html">ch05</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch06.html">ch06</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch07.html">ch07</a></li>
            <li><a href="/txt/internet-aesthetic-a-genealogy/ch08.html">ch08</a></li>
          </ol>
        </nav>
{toc_nav}      </header>
      <article id="textblock">
        <h1 class="title">{title}</h1>

{body}
{chapter_nav(ch)}
      </article>
    </main>
    <footer id="main-footer">
      <div id="texthtml"></div>
      <div id="sitenachtml"></div>
      <!-- main.jsから#footerへfooter.htmlの挿入 -->
      <div id="footerhtml"></div>
    </footer>
  </div>
  <div id="lightbox">
    <link rel="stylesheet" href="{SITE_ROOT}/luminous-basic.min.css">
    <script src="{SITE_ROOT}/Luminous.min.js"></script>
    <script>
      new LuminousGallery(document.querySelectorAll('a[href$=jpg],a[href$=png],a[href$=gif],a[href$=webp]'));
    </script>
  </div>
</body>

</html>
"""


def sync_images() -> None:
    if not IMG_SRC.is_dir():
        print(f"Warning: image source not found: {IMG_SRC}")
        return
    if IMG_DST.exists():
        shutil.rmtree(IMG_DST)
    shutil.copytree(IMG_SRC, IMG_DST)
    count = sum(1 for _ in IMG_DST.iterdir())
    print(f"  img/  ←  {IMG_SRC} ({count} files)")


def convert_chapter(ch: dict) -> None:
    src = MANUSCRIPT / ch["source"]
    text = src.read_text(encoding="utf-8")
    time_axis, text = preprocess_md(text)
    is_intro = ch["source"] == "序文.md"
    body, toc_entries = build_body(time_axis, text, ch["title"], is_intro=is_intro)
    out = DEPLOY_DIR / ch["output"]
    out.write_text(render_page(ch, body, toc_entries), encoding="utf-8")
    print(f"  {ch['output']}  ←  {ch['source']}")


def sync_index_toc() -> None:
    """index.html の目次リストを CHAPTERS から更新する。"""
    index_path = DEPLOY_DIR / "index.html"
    if not index_path.exists():
        print("  Warning: index.html not found, skipping toc sync")
        return

    lines = [
        f'            <li><a href="{ch["output"]}">{ch["title"]}</a></li>'
        for ch in CHAPTERS
    ]
    toc_html = "\n".join(lines)

    text = index_path.read_text(encoding="utf-8")
    pattern = re.compile(r"<!-- toc:start -->.*?<!-- toc:end -->", re.DOTALL)
    replacement = f"<!-- toc:start -->\n{toc_html}\n          <!-- toc:end -->"
    if not pattern.search(text):
        print("  Warning: toc markers not found in index.html")
        return
    index_path.write_text(pattern.sub(replacement, text), encoding="utf-8")
    print("  index.html  ←  toc synced")


def remove_stale_html() -> None:
    """旧ファイル名の HTML を削除する。"""
    keep = {ch["output"] for ch in CHAPTERS} | {INDEX_PAGE}
    for path in DEPLOY_DIR.glob("*.html"):
        if path.name not in keep:
            path.unlink()
            print(f"  removed stale {path.name}")


def main() -> int:
    print(f"Building into {DEPLOY_DIR} …")
    sync_images()
    for ch in CHAPTERS:
        convert_chapter(ch)
    remove_stale_html()
    sync_index_toc()
    print(f"Done. Deploy folder: {DEPLOY_DIR.name}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
