import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"
weights = [55.5, 55.2, 55.0, 54.8, 54.5]
days = [1, 2, 3, 4, 5]
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, weights)
ax.set_xticks(days)

for i, w in enumerate(weights):
    ax.annotate(
        f"{w}", (days[i], w), textcoords="offset points", xytext=(0, 8), ha="center"
    )

ax.set_title("내 몸무게 변화")
fig.savefig("my_weight_chart.png")