"""Analyze 4-patch Google Trends CSVs with vaporwave anchor."""
import csv
from pathlib import Path

DIR = Path(__file__).parent
PATCHES = sorted(DIR.glob("patch*_time_series_*.csv"))

def load(path):
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f)
        cols = r.fieldnames
        rows = []
        for row in r:
            d = {}
        for c in cols:
            raw = row[c].strip('"')
            if c == "Time":
                d[c] = raw
            else:
                d[c] = float(raw) if raw not in ("", "<1") else 0.0
            rows.append(d)
    return cols, rows

print("=== patch contents ===")
for p in PATCHES:
    cols, _ = load(p)
    print(f"{p.name}: {cols[1:]}")

print("\n=== vaporwave anchor (peak per patch) ===")
ref_peak = None
for p in PATCHES:
    cols, rows = load(p)
    vw = [row["vaporwave"] for row in rows]
    peak = max(vw)
    peak_idx = vw.index(peak)
    dates = [row["Time"].strip('"') for row in rows]
    if ref_peak is None:
        ref_peak = peak
        ref_name = p.name
    ratio = ref_peak / peak if peak else 0
    print(f"{p.name}: peak={peak:.0f} @ {dates[peak_idx]}  scale_to_patch1={ratio:.3f}")

print("\n=== true max per column (each patch) ===")
for p in PATCHES:
    cols, rows = load(p)
    print(f"\n{p.name}:")
    for c in cols:
        if c == "Time":
            continue
        best = max((r[c], r["Time"]) for r in rows)
        print(f"  {c:<24} max={best[0]:5.1f} @ {best[1]}")

