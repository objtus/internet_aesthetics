"""Merge patch1–4 CSV into trends_data.json and trends_data.js."""
import csv
import json
from datetime import datetime
from pathlib import Path

DIR = Path(__file__).parent

PATCH_META = {
    1: {
        "label": "patch1 — 第2章（2010年代ミーム）",
        "terms": ["vaporwave", "seapunk", "witch house", "soft grunge", "tumblr aesthetic"],
    },
    2: {
        "label": "patch2 — 第4–5章（2020美学）",
        "terms": ["vaporwave", "cottagecore", "dark academia", "liminal space", "internet aesthetic"],
    },
    3: {
        "label": "patch3 — 第3章（○○ aesthetic 複合語）",
        "terms": [
            "vaporwave",
            "internet aesthetics",
            "vaporwave aesthetic",
            "seapunk aesthetic",
            "witch house aesthetic",
        ],
    },
    4: {
        "label": "patch4 — 汎用語（aesthetic / aesthetics）",
        "terms": ["vaporwave", "aesthetic", "aesthetics"],
    },
}

COLORS = {
    "vaporwave": "#2563eb",
    "seapunk": "#0891b2",
    "witch house": "#7c3aed",
    "soft grunge": "#db2777",
    "tumblr aesthetic": "#ea580c",
    "cottagecore": "#16a34a",
    "dark academia": "#854d0e",
    "liminal space": "#64748b",
    "internet aesthetic": "#0d9488",
    "internet aesthetics": "#0f766e",
    "vaporwave aesthetic": "#3b82f6",
    "seapunk aesthetic": "#06b6d4",
    "witch house aesthetic": "#9333ea",
    "aesthetic": "#525252",
    "aesthetics": "#737373",
}

DEFAULT_VISIBLE = {
    "witch house": False,
}

ANNOTATIONS = [
    {"date": "2011-06-01", "title": "2011-06", "text": "seapunk ツイート", "patches": [1], "zone": "below"},
    {"date": "2011-09-01", "title": "2011-09", "text": "SuperSuper 特集", "patches": [1], "zone": "below"},
    {"date": "2012-03-01", "title": "2012-03", "text": "VICE 年表", "patches": [1], "zone": "below"},
    {"date": "2012-07-01", "title": "2012-07", "text": "Harper vaporwave", "patches": [1], "zone": "below"},
    {"date": "2012-11-01", "title": "2012-11", "text": "Rihanna SNL", "patches": [1], "zone": "below"},
    {"date": "2014-08-01", "title": "2014-08", "text": "soft grunge", "patches": [1], "zone": "above"},
    {"date": "2017-01-01", "title": "2017-01", "text": "vaporwave peak", "patches": [1], "zone": "above"},
    {"date": "2018-07-01", "title": "2018-07", "text": "tumblr aesthetic", "patches": [1], "zone": "above"},
    {"date": "2019-04-01", "title": "2019-04", "text": "cottagecore 上昇", "patches": [2], "zone": "below"},
    {"date": "2020-03-01", "title": "2020-03", "text": "lockdown / TikTok", "patches": [2], "zone": "below"},
    {"date": "2020-11-01", "title": "2020-11", "text": "cottagecore peak", "patches": [2], "zone": "above"},
    {"date": "2021-01-01", "title": "2021-01", "text": "dark academia peak", "patches": [2], "zone": "above"},
    {"date": "2020-02-01", "title": "2020-02", "text": "witch house aesthetic", "patches": [3], "zone": "below"},
    {"date": "2026-02-01", "title": "2026-02", "text": "vaporwave aesthetic", "patches": [3], "zone": "above"},
    {"date": "2020-09-01", "title": "2020-09", "text": "aesthetic peak", "patches": [4], "zone": "above"},
    {"date": "2026-05-01", "title": "2026-05", "text": "aesthetics peak", "patches": [4], "zone": "above"},
]


def load_patch(path: Path, patch_id: int) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        terms = [c for c in reader.fieldnames if c != "Time"]
        rows = list(reader)

    series_list = []
    for term in terms:
        sid = f"p{patch_id}-{term.replace(' ', '_')}"
        data = []
        for row in rows:
            t = row["Time"].strip('"')
            raw = row[term].strip('"')
            v = 0.0 if raw in ("", "<1") else float(raw)
            data.append([t, v])

        series_list.append({
            "id": sid,
            "patch": patch_id,
            "term": term,
            "label": term if patch_id == 1 or term != "vaporwave" else f"{term} (p{patch_id})",
            "color": COLORS.get(term, "#333333"),
            "visible": DEFAULT_VISIBLE.get(term, True),
            "data": data,
        })
    return series_list


def main():
    all_series = []
    for n in range(1, 5):
        csv_path = next(DIR.glob(f"patch{n}_time_series_*.csv"))
        all_series.extend(load_patch(csv_path, n))

    payload = {
        "meta": {
            "region": "Worldwide",
            "granularity": "monthly",
            "range": ["2004-01-01", "2026-06-01"],
            "defaultView": ["2009-01-01", "2026-07-01"],
            "note": (
                "同一 patch 内の相対指数（最大ピーク = 100）。"
                "patch 間・単独 CSV 間ではスケールが異なる。"
                "vaporwave は patch ごとに正規化が違う。"
            ),
        },
        "patches": {str(k): v for k, v in PATCH_META.items()},
        "series": all_series,
        "annotations": ANNOTATIONS,
    }

    json_path = DIR / "trends_data.json"
    js_path = DIR / "trends_data.js"
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    js_path.write_text(
        "const TRENDS_DATA = " + json.dumps(payload, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    print(f"Wrote {json_path} ({len(all_series)} series, {len(ANNOTATIONS)} annotations)")
    print(f"Wrote {js_path}")


if __name__ == "__main__":
    main()
