import anndata
import numpy as np

adata = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

X = adata.X.copy().astype(float)

# Log transform
X = np.log1p(X)

# Marker-wise percentile normalization
X_uni = np.zeros_like(X)

for j in range(X.shape[1]):

    col = X[:, j]

    p1 = np.percentile(col, 1)
    p99 = np.percentile(col, 99)

    X_uni[:, j] = (col - p1) / (p99 - p1 + 1e-9)

    X_uni[:, j] = np.clip(X_uni[:, j], 0, 1)

adata.layers["uniform"] = X_uni

adata.write_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\uniform.h5ad"
)

print("UniFORM-style normalization completed.")
print("Saved:")
print(r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\uniform.h5ad")