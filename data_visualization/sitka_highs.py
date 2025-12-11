from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

root = Path(__file__).parent  # 当前脚本所在目录 data_visualization
path = root / "weather_data" / "death_valley_2014.csv"
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#     print(index, column_header)

dates, highs, lows = [], [], []
for row in reader:
    try:
        # Max TemperatureF is column index 1; skip rows with missing data
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[2])
    except ValueError:
        print(f"Missing data for current {current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

plt.style.use("seaborn-v0_8-dark-palette")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

ax.set_title("Daily High Temperature, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
