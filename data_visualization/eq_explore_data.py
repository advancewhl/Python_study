from pathlib import Path
import json
import plotly.express as px
import pandas as pd

root = Path(__file__).parent
path = root / "eq_data" / "4.5_week.geojson"
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding="utf-8")

all_eq_data = json.loads(contents)

path = root / "eq_data/readable_eq_data.geojson"
raedable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(raedable_contents)


all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

mags = [d["properties"]["mag"] for d in all_eq_dicts]
titles = [d["properties"]["title"] for d in all_eq_dicts]
lons = [d["geometry"]["coordinates"][0] for d in all_eq_dicts]
lats = [d["geometry"]["coordinates"][1] for d in all_eq_dicts]

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])


data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=["经度", "维度", "位置", "震级"])

fig = px.scatter(
    data,
    x="经度",
    y="维度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
    color="震级",
    color_continuous_scale=px.colors.sequential.Inferno,  # 选一个渐变
    hover_name="位置",
)


fig.write_html("globel_earthquakes.html")
fig.show()
