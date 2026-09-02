import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# DATA
# ==================================================

data = {
    "Raw":       [0.045, 278.00, 0.014, -0.022, 0.0, 0.0],
    "UniFORM":   [0.072, 88.00, 0.017, -0.135, 65.0, 70.0],
    "Z-score":   [0.201, 59.00, 0.059, -0.085, 28.0, 30.0],
    "MeanDiv":   [0.095, 84.00, 0.021, -0.134, 36.0, 38.0],
    "ComBat":    [0.116, 96.00, 0.029, -0.079, 52.0, 60.0],
    "MxNorm":    [0.105, 90.00, 0.025, -0.100, 42.0, 45.0]
}

metrics = [
    "kBET",
    "χ² Statistic\n(lower=better)",
    "p-value",
    "Silhouette\n(lower=better)",
    "Peak STD\nImprov.%",
    "Wasserstein\nImprov.%"
]

# ==================================================
# CONVERT TO DF
# ==================================================

df = pd.DataFrame(data, index=metrics).T

# ==================================================
# NORMALIZE TO 0-100
# ==================================================

radar = pd.DataFrame(index=df.index)

# higher better
radar["kBET"] = (
    df["kBET"] / df["kBET"].max()
) * 100

# lower better
radar["χ² Statistic\n(lower=better)"] = (
    1 -
    df["χ² Statistic\n(lower=better)"]
    /
    df["χ² Statistic\n(lower=better)"].max()
) * 100

# higher better
radar["p-value"] = (
    df["p-value"]
    /
    df["p-value"].max()
) * 100

# more negative better
radar["Silhouette\n(lower=better)"] = (
    abs(df["Silhouette\n(lower=better)"])
    /
    abs(df["Silhouette\n(lower=better)"]).max()
) * 100

# higher better
radar["Peak STD\nImprov.%"] = (
    df["Peak STD\nImprov.%"]
    /
    df["Peak STD\nImprov.%"].max()
) * 100

radar["Wasserstein\nImprov.%"] = (
    df["Wasserstein\nImprov.%"]
    /
    df["Wasserstein\nImprov.%"].max()
) * 100

# ==================================================
# RADAR SETUP
# ==================================================

labels = radar.columns.tolist()

num_vars = len(labels)

angles = np.linspace(
    0,
    2*np.pi,
    num_vars,
    endpoint=False
).tolist()

angles += angles[:1]

# ==================================================
# COLORS
# ==================================================

colors = {
    "Raw": "#B0B0B0",
    "UniFORM": "#4E79A7",
    "MeanDiv": "#9C755F",
    "Z-score": "#59A14F",
    "ComBat": "#7B6FB2",
    "MxNorm": "#E15759"
}

# ==================================================
# PLOT
# ==================================================

fig, ax = plt.subplots(
    figsize=(10,10),
    subplot_kw=dict(polar=True)
)

for method in radar.index:

    values = radar.loc[method].tolist()
    values += values[:1]

    ax.plot(
        angles,
        values,
        linewidth=2,
        color=colors[method],
        label=method
    )

    ax.fill(
        angles,
        values,
        alpha=0.08,
        color=colors[method]
    )

# ==================================================
# FORMAT
# ==================================================

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=11)

ax.set_ylim(0,100)

ax.set_title(
    "Overall Method Comparison - Radar Chart",
    fontsize=18,
    pad=25
)

ax.legend(
    loc="upper left",
    bbox_to_anchor=(1.15,1.15)
)

plt.tight_layout()

plt.savefig(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Radar_Comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Saved:")
print(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Radar_Comparison.png"
)