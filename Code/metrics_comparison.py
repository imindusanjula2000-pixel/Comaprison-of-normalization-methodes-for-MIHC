import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# RESULTS
# ==================================================

df = pd.DataFrame({

    "Method": [
        "Raw",
        "UniFORM",
        "MeanDiv",
        "Z-score",
        "ComBat",
        "MxNorm"
    ],

    "kBET": [
        0.045,
        0.072,
        0.095,
        0.201,
        0.116,
        0.105
    ],

    "Chi2": [
        278.00,
        88.00,
        84.00,
        59.00,
        96.00,
        90.00
    ],

    "Pvalue": [
        0.014,
        0.017,
        0.021,
        0.059,
        0.029,
        0.025
    ],

    "Silhouette": [
        -0.022,
        -0.135,
        -0.134,
        -0.085,
        -0.079,
        -0.100
    ]
})

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

bar_colors = [colors[m] for m in df["Method"]]

# ==================================================
# FIGURE
# ==================================================

plt.style.use("ggplot")

fig, axs = plt.subplots(
    2,
    2,
    figsize=(18,10)
)

# ==================================================
# kBET
# ==================================================

axs[0,0].bar(
    df["Method"],
    df["kBET"],
    color=bar_colors,
    edgecolor="black",
    linewidth=1
)

axs[0,0].set_title(
    "kBET Score\n(Higher = better local score mixing)"
)

axs[0,0].set_ylabel("kBET Score")

# ==================================================
# CHI2
# ==================================================

axs[0,1].bar(
    df["Method"],
    df["Chi2"],
    color=bar_colors,
    edgecolor="black",
    linewidth=1
)

axs[0,1].set_title(
    "Avg. χ² Statistic\n(Lower = less batch effect)"
)

axs[0,1].set_ylabel("χ² Statistic")

# ==================================================
# P VALUE
# ==================================================

axs[1,0].bar(
    df["Method"],
    df["Pvalue"],
    color=bar_colors,
    edgecolor="black",
    linewidth=1
)

axs[1,0].axhline(
    y=0.05,
    color="red",
    linestyle="--",
    linewidth=2,
    label="0.05 Threshold"
)

axs[1,0].legend()

axs[1,0].set_title(
    "Average p-value\n(Higher = batch effect not significant)"
)

axs[1,0].set_ylabel("p-value")

# ==================================================
# SILHOUETTE
# ==================================================

axs[1,1].bar(
    df["Method"],
    df["Silhouette"],
    color=bar_colors,
    edgecolor="black",
    linewidth=1
)

axs[1,1].set_title(
    "Silhouette Score\n(More negative = better inter-sample mixing)"
)

axs[1,1].set_ylabel("Silhouette Score")

# ==================================================
# FORMAT
# ==================================================

for ax in axs.flat:
    ax.tick_params(
        axis="x",
        rotation=0,
        labelsize=11
    )

    ax.grid(
        True,
        alpha=0.3
    )

# ==================================================
# SAVE
# ==================================================

plt.tight_layout()

plt.savefig(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Metrics_Comparison_Without_BSpline.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Saved:")

print(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Metrics_Comparison.png"
)