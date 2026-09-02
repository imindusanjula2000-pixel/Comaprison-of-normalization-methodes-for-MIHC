import anndata
import numpy as np
import pandas as pd

from scipy.stats import wasserstein_distance
from scipy.stats import chi2_contingency

from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import silhouette_score

# ======================================================
# FILES
# ======================================================

FILES = {

    "Raw":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad",

    "Z-score":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\zscore.h5ad",

    "MeanDiv":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\meandiv.h5ad",

    "ComBat":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\combat.h5ad",

    "MxNorm":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\mxnorm.h5ad",

    "UniFORM":
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\uniform.h5ad"
}

# ======================================================
# LOAD RAW
# ======================================================

raw = anndata.read_h5ad(FILES["Raw"])

X_raw = np.asarray(raw.X)

batch = raw.obs["batch"].astype(str).values

# ======================================================
# PEAK STD RAW
# ======================================================

peak_raw = []

for i in range(X_raw.shape[1]):

    hist, _ = np.histogram(
        X_raw[:, i],
        bins=50
    )

    peak_raw.append(
        np.argmax(hist)
    )

peak_raw_std = np.std(peak_raw)

# ======================================================
# WASSERSTEIN RAW
# ======================================================

raw_wass = []

for i in range(X_raw.shape[1]):

    raw_wass.append(

        wasserstein_distance(
            X_raw[:, i],
            np.random.permutation(
                X_raw[:, i]
            )
        )
    )

wass_raw_mean = np.mean(raw_wass)

# ======================================================
# RESULTS
# ======================================================

results = []

for name, path in FILES.items():

    print(
        f"Processing {name}"
    )

    adata = anndata.read_h5ad(path)

    if name == "Raw":

        X = np.asarray(
            adata.X
        )

    else:

        if len(
            adata.layers.keys()
        ) > 0:

            layer_name = list(
                adata.layers.keys()
            )[0]

            X = np.asarray(
                adata.layers[layer_name]
            )

        else:

            X = np.asarray(
                adata.X
            )

    X = np.nan_to_num(X)

    # ==================================================
    # kBET approximation
    # ==================================================

    nn = NearestNeighbors(
        n_neighbors=15
    )

    nn.fit(X)

    neigh = nn.kneighbors(
        return_distance=False
    )

    mix = []

    batches = np.unique(batch)

    for row in neigh:

        local = batch[row]

        mix.append(
            len(
                np.unique(local)
            )
            /
            len(batches)
        )

    kbet = np.mean(mix)

    # ==================================================
    # Chi2 + p
    # ==================================================

    chi_vals = []
    p_vals = []

    subset = neigh[
        :min(
            1000,
            len(neigh)
        )
    ]

    for row in subset:

        local = batch[row]

        obs = pd.crosstab(
            pd.Series(local),
            columns="count"
        )

        if obs.shape[0] > 1:

            chi2, p, _, _ = (
                chi2_contingency(obs)
            )

            chi_vals.append(chi2)
            p_vals.append(p)

    chi_mean = np.mean(
        chi_vals
    )

    p_mean = np.mean(
        p_vals
    )

    # ==================================================
    # silhouette
    # ==================================================

    sample_size = min(
        5000,
        X.shape[0]
    )

    idx = np.random.choice(
        X.shape[0],
        sample_size,
        replace=False
    )

    sil = silhouette_score(
        X[idx],
        batch[idx]
    )

    # ==================================================
    # Peak STD
    # ==================================================

    peaks = []

    for i in range(X.shape[1]):

        hist, _ = np.histogram(
            X[:, i],
            bins=50
        )

        peaks.append(
            np.argmax(hist)
        )

    peak_std = np.std(peaks)

    peak_imp = (
        (
            peak_raw_std
            -
            peak_std
        )
        /
        peak_raw_std
    ) * 100

    # ==================================================
    # Wasserstein
    # ==================================================

    wass = []

    for i in range(X.shape[1]):

        wass.append(

            wasserstein_distance(
                X[:, i],
                np.random.permutation(
                    X[:, i]
                )
            )
        )

    wass_mean = np.mean(wass)

    wass_imp = (
        (
            wass_raw_mean
            -
            wass_mean
        )
        /
        wass_raw_mean
    ) * 100

    results.append([

        name,
        round(kbet,4),
        round(chi_mean,4),
        round(p_mean,4),
        round(sil,4),
        round(peak_imp,2),
        round(wass_imp,2)

    ])

# ======================================================
# SAVE CSV
# ======================================================

df = pd.DataFrame(

    results,

    columns=[
        "Method",
        "kBET",
        "Chi2",
        "Pvalue",
        "Silhouette",
        "PeakSTD_Improvement",
        "Wasserstein_Improvement"
    ]
)

csv_file = r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\All_Method_Metrics.csv"

df.to_csv(
    csv_file,
    index=False
)

print("\nDONE\n")

print(df)

print(
    f"\nSaved:\n{csv_file}"
)