import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()

results = []
results = [die_1.roll() + die_2.roll() for r in range(1000)]

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(1, max_result + 1)
frequencies = [results.count(v) for v in poss_results]

title = "Result of rolling Two D6 Dice 1,000 Times"
labels = {"x": "Result", "y": "Frequencies of result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.show()
# fig.write_html("dice_visual_d6.html")
