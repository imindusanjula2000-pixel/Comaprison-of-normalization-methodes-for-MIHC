import anndata
import numpy as np

adata = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

X = adata.X.copy()

mx = np.max(X, axis=0)

Xn = X / (mx + 1e-9)

adata.layers["mxnorm"] = Xn

adata.write_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\mxnorm.h5ad"
)

print("Done")