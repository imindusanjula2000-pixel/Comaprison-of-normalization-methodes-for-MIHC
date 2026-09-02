iimport anndata
import numpy as np
import matplotlib.pyplot as plt
import umap.umap_ as umap

# ======================================================
# LOAD DATA
# ======================================================

raw = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

zscore = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\zscore.h5ad"
)

meandiv = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\meandiv.h5ad"
)

combat = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\combat.h5ad"
)

mxnorm = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\mxnorm.h5ad"
)

uniform = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\uniform.h5ad"
)

# ======================================================
# EXTRACT MATRICES
# ======================================================

X_raw = raw.X
X_z = zscore.layers["zscore"]
X_m = meandiv.layers["meandiv"]
X_c = combat.layers["combat"]
X_x = mxnorm.layers["mxnorm"]
X_u = uniform.layers["uniform"]

# ======================================================
# FIX NaN / INF
# ======================================================

def clean(X):
    X = np.asarray(X, dtype=np.float32)
    X = np.nan_to_num(X)
    return X

methods = {
    "Raw": clean(X_raw),
    "Z-score": clean(X_z),
    "MeanDiv": clean(X_m),
    "ComBat": clean(X_c),
    "MxNorm": clean(X_x),
    "UniFORM": clean(X_u)
}

# ======================================================
# USE ONLY 5000 CELLS FOR SPEED
# ======================================================

np.random.seed(42)

n_cells = min(5000, X_raw.shape[0])

idx = np.random.choice(
    X_raw.shape[0],
    n_cells,
    replace=False
)

# ======================================================
# UMAP
# ======================================================

fig, axes = plt.subplots(
    2,
    3,
    figsize=(16,10)
)

axes = axes.flatten()

for ax, (name, X) in zip(
    axes,
    methods.items()
):

    X_sub = X[idx]

    reducer = umap.UMAP(
        n_neighbors=15,
        min_dist=0.3,
        random_state=42
    )

    embedding = reducer.fit_transform(X_sub)

    ax.scatter(
        embedding[:,0],
        embedding[:,1],
        s=3,
        alpha=0.6
    )

    ax.set_title(name)

    ax.set_xlabel("UMAP 1")
    ax.set_ylabel("UMAP 2")

plt.tight_layout()

plt.savefig(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\UMAP_All_Methods.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nDONE")
print(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\UMAP_All_Methods.png"
)

plt.show()