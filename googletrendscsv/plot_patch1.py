"""Plot patch1 Google Trends CSV (5-term comparison, vaporwave anchor batch)."""
import csv
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

DIR = Path(__file__).parent
CSV = next(DIR.glob("patch1_time_series_*.csv"))
OUT = DIR / "patch1_plot.png"

SKIP_TERMS = {"witch house"}
ROW_GAP = 0.016

# (date, label) — before 2013 → below axis; 2013+ → above axis
MARKERS = [
    (datetime(2011, 6, 1), "2011-06\nseapunk ツイート"),
    (datetime(2011, 9, 1), "2011-09\nSuperSuper 特集"),
    (datetime(2012, 3, 1), "2012-03\nVICE 年表"),
    (datetime(2012, 7, 1), "2012-07\nHarper vaporwave"),
    (datetime(2012, 11, 1), "2012-11\nRihanna SNL"),
    (datetime(2014, 8, 1), "2014-08\nsoft grunge"),
    (datetime(2017, 1, 1), "2017-01\nvaporwave peak"),
    (datetime(2018, 7, 1), "2018-07\ntumblr aesthetic"),
]

SPLIT_YEAR = 2013

for name in ("Yu Gothic", "Meiryo", "MS Gothic", "Segoe UI"):
    if any(name in f.name for f in fm.fontManager.ttflist):
        plt.rcParams["font.family"] = name
        break

plt.rcParams.update({
    "font.size": 12,
    "axes.labelsize": 14,
    "ytick.labelsize": 12,
    "legend.fontsize": 14,
})

COLORS = {
    "vaporwave": "#2563eb",
    "seapunk": "#0891b2",
    "soft grunge": "#db2777",
    "tumblr aesthetic": "#ea580c",
}


def load(path: Path):
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        terms = [c for c in reader.fieldnames if c != "Time"]
        series = {t: {"dates": [], "values": []} for t in terms}
        for row in reader:
            d = datetime.strptime(row["Time"].strip('"'), "%Y-%m-%d")
            for t in terms:
                raw = row[t].strip('"')
                v = 0.0 if raw in ("", "<1") else float(raw)
                series[t]["dates"].append(d)
                series[t]["values"].append(v)
    return series


def estimate_width(label: str) -> float:
    lines = label.split("\n")
    max_chars = max(len(line) for line in lines)
    return min(0.19, 0.010 * max_chars + 0.022 * len(lines))


def assign_rows(markers, xlim):
    t0 = mdates.date2num(xlim[0])
    t1 = mdates.date2num(xlim[1])
    span = t1 - t0

    items = []
    for dt, label in markers:
        xf = (mdates.date2num(dt) - t0) / span
        items.append({
            "dt": dt,
            "label": label,
            "x": xf,
            "w": estimate_width(label),
            "row": None,
            "zone": "below" if dt.year < SPLIT_YEAR else "above",
        })
    items.sort(key=lambda i: i["x"])

    for zone in ("below", "above"):
        zone_items = [i for i in items if i["zone"] == zone]
        row_slots = [[] for _ in range(6)]
        for item in zone_items:
            for row_idx, slot in enumerate(row_slots):
                conflict = any(
                    abs(item["x"] - other["x"]) < (item["w"] + other["w"]) / 2 + ROW_GAP
                    for other in slot
                )
                if not conflict:
                    item["row"] = row_idx
                    slot.append(item)
                    break
            else:
                item["row"] = len(row_slots) - 1
                row_slots[-1].append(item)

    return items


def draw_annotations(ax, placed):
    bbox_kw = dict(
        boxstyle="round,pad=0.28",
        facecolor="white",
        edgecolor="#bbb",
        alpha=0.96,
    )
    below_step = 0.052
    above_step = 0.055

    for item in placed:
        dt = item["dt"]
        xf = item["x"]
        row = item["row"]

        ax.axvline(
            dt, color="#999", linestyle="--", linewidth=0.9, alpha=0.5, zorder=0,
        )

        if item["zone"] == "below":
            y = -0.02 - row * below_step
            ax.annotate(
                item["label"],
                xy=(xf, 0.0),
                xycoords=("axes fraction", "axes fraction"),
                xytext=(xf, y),
                textcoords=("axes fraction", "axes fraction"),
                fontsize=10.5,
                ha="center",
                va="top",
                color="#222",
                linespacing=1.15,
                clip_on=False,
                bbox=bbox_kw,
                arrowprops=dict(arrowstyle="-", color="#aaa", lw=0.7, shrinkA=0, shrinkB=2),
                zorder=5 + row,
            )
        else:
            y = 1.012 + row * above_step
            ax.annotate(
                item["label"],
                xy=(xf, 1.0),
                xycoords=("axes fraction", "axes fraction"),
                xytext=(xf, y),
                textcoords=("axes fraction", "axes fraction"),
                fontsize=10.5,
                ha="center",
                va="bottom",
                color="#222",
                linespacing=1.15,
                clip_on=False,
                bbox=bbox_kw,
                arrowprops=dict(arrowstyle="-", color="#aaa", lw=0.7, shrinkA=0, shrinkB=2),
                zorder=5 + row,
            )


def main():
    series = load(CSV)
    xlim = (datetime(2009, 1, 1), datetime(2026, 7, 1))

    fig, ax = plt.subplots(figsize=(15, 8.5), dpi=150)
    fig.patch.set_facecolor("white")

    for term, data in series.items():
        if term in SKIP_TERMS:
            continue
        ax.plot(
            data["dates"],
            data["values"],
            label=term,
            color=COLORS.get(term, "#333"),
            linewidth=2.6,
            alpha=0.95,
        )

    placed = assign_rows(MARKERS, xlim)
    max_above = max((p["row"] for p in placed if p["zone"] == "above"), default=0)
    max_below = max((p["row"] for p in placed if p["zone"] == "below"), default=0)

    ax.set_ylim(-2, 100)
    ax.set_xlim(*xlim)

    ax.set_title("")  # use suptitle so title is not clipped by annotation rows
    ax.set_ylabel("検索関心（相対値 0–100）", fontsize=15, labelpad=4)
    ax.set_xlabel("")
    ax.set_yticks([t for t in range(0, 101, 20)])
    ax.grid(True, linestyle=":", alpha=0.45, linewidth=0.8)
    ax.legend(
        loc="upper right",
        framealpha=0.97,
        fontsize=14,
        edgecolor="#ccc",
        fancybox=False,
    )

    ax.xaxis.set_major_locator(mdates.YearLocator(1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.tick_params(axis="x", pad=6, length=5, width=1.2)
    for label in ax.get_xticklabels():
        label.set_fontsize(17)
        label.set_fontweight("bold")

    draw_annotations(ax, placed)

    note = (
        "Worldwide · monthly · 2004–2026 ｜ "
        "同一クエリ5語の相対指数（最大ピーク = 100）— 絶対検索数ではない ｜ "
        "破線は原稿年表の手がかり（witch house はノイズのため非表示）"
    )
    fig.text(0.01, 0.008, note, fontsize=10, color="#444")

    fig.suptitle("Google Trends", fontsize=22, fontweight="bold", y=0.98)

    top = 0.88 - max_above * 0.022
    bottom = 0.12 + max_below * 0.045
    fig.subplots_adjust(left=0.045, right=0.998, top=max(0.78, top), bottom=bottom)
    fig.savefig(OUT, bbox_inches="tight", pad_inches=0.10, facecolor="white")
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
