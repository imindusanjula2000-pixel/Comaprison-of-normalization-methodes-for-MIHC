import pandas as pd
import matplotlib.pyplot as plt

# ===================================================
# ENTER YOUR RESULTS HERE
# ===================================================

results = {
    "Method": ["Z-score", "MeanDiv", "ComBat", "MxNorm", "UniFORM"],

    "PeakSTD_Raw": [100, 100, 100, 100, 100],

    "PeakSTD_Norm": [72, 64, 48, 58, 35],

    "Wass_Raw": [100, 100, 100, 100, 100],

    "Wass_Norm": [70, 62, 40, 55, 30]
}

df = pd.DataFrame(results)

# ===================================================
# IMPROVEMENT %
# ===================================================

df["PeakSTD_Improvement"] = (
    (df["PeakSTD_Raw"] - df["PeakSTD_Norm"])
    / df["PeakSTD_Raw"]
) * 100

df["Wasserstein_Improvement"] = (
    (df["Wass_Raw"] - df["Wass_Norm"])
    / df["Wass_Raw"]
) * 100

# ===================================================
# SAVE TABLE
# ===================================================

output_csv = r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Peak_Wasserstein_Table.csv"

df.to_csv(output_csv, index=False)

print("\nTable Saved:")
print(output_csv)

print("\n")
print(df)

# ===================================================
# GRAPH
# ===================================================

fig, ax = plt.subplots(
    1,
    2,
    figsize=(12, 5)
)

# Peak STD

ax[0].bar(
    df["Method"],
    df["PeakSTD_Improvement"],
    color="steelblue"
)

ax[0].set_title(
    "Peak STD Improvement (%)"
)

ax[0].set_ylabel(
    "Improvement (%)"
)

# Wasserstein

ax[1].bar(
    df["Method"],
    df["Wasserstein_Improvement"],
    color="darkorange"
)

ax[1].set_title(
    "Wasserstein Distance Improvement (%)"
)

ax[1].set_ylabel(
    "Improvement (%)"
)

plt.tight_layout()

output_png = r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\Peak_Wasserstein_Improvement.png"

plt.savefig(
    output_png,
    dpi=300,
    bbox_inches="tight"
)

print("\nGraph Saved:")
print(output_png)

plt.show()