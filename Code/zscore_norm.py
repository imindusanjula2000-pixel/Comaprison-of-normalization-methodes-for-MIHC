import anndata
import numpy as np
from scipy.stats import zscore

adata = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

X = adata.X.copy()

X = zscore(X, axis=0)

adata.layers["zscore"] = X

adata.write_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\zscore.h5ad"
)

print("Done")