import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

time = []
distance = []
holes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

with open('data.txt', 'r') as dataFile:
    for line in dataFile:
        value = line.split(" ")
        valueTime = value[0]
        valueDistance = value[1]
        
        time.append(float(valueTime))
        distance.append(float(valueDistance))

col_labels = ["Furos", "Distância (cm)", "Periodo (s)"]
tableData = list(zip(holes, distance, time))


fig = plt.figure(figsize = (10, 5), layout='constrained')
gs = GridSpec(1, 2, width_ratios = [2, 1])

fig.canvas.manager.set_window_title("Gráfico de Periodo por distância")

ax = fig.add_subplot(gs[0])

ax.plot(
    distance, time,
    color = "blue",
    linestyle = "solid",
    linewidth = 2,
    marker = "o",
    markersize = 8,
    markerfacecolor = "blue",
)

ax.set_title("Periodo X Distância do centro de massa")
ax.set_xlabel("Distância do centro de massa (cm)")
ax.set_ylabel("Periodo (s)")

ax.set_xlim(min(distance) - 1, max(distance) + 1)
ax.set_ylim(min(time) - 0.01, max(time) + 0.01)




ax2 = fig.add_subplot(gs[1])
ax2.axis('off')

table = ax2.table(
    cellText = tableData,
    colLabels = col_labels,
    loc = "center",
    cellLoc = "center"
)


table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.4)

plt.tight_layout()


plt.show()
