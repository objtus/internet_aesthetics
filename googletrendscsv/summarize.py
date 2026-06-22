import csv
import re
from datetime import datetime
from pathlib import Path

DIR = Path(__file__).parent
rows = []

for f in sorted(DIR.glob("*_time_series_*.csv")):
    with open(f, encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        time_col = reader.fieldnames[0]
        val_col = reader.fieldnames[1]
        data = []
        for row in reader:
            t = datetime.strptime(row[time_col].strip('"'), "%Y-%m-%d")
            raw = row[val_col].strip('"')
            val = 0.0 if raw == "<1" else float(raw)
            data.append((t, val))

    kw = re.match(r"(.+?)_time_series", f.name).group(1).replace("-", " ")
    peak_date, peak_val = max(data, key=lambda x: x[1])
    first_nz = next((d for d, v in data if v > 0), None)
    post = [v for d, v in data if d.year >= 2010]
    rows.append(
        (kw, int(peak_val), peak_date.strftime("%Y-%m"),
         first_nz.strftime("%Y-%m") if first_nz else "-",
         round(sum(post) / len(post), 1))
    )

rows.sort(key=lambda x: -x[1])
print(f"{'keyword':<22} {'peak':>4}  peak_date  first>0  mean2010+")
for kw, peak, pdate, first, mean in rows:
    print(f"{kw:<22} {peak:>4}  {pdate:<10} {first:<8} {mean:>7}")
