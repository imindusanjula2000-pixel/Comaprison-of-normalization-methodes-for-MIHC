import anndata
import numpy as np

adata = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

X = adata.X.copy()

means = np.mean(X, axis=0)

Xn = X / (means + 1e-9)

adata.layers["meandiv"] = Xn

adata.write_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\meandiv.h5ad"
)

print("Done")