import anndata
import pandas as pd
from pycombat import Combat

adata = anndata.read_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

X = adata.X

batch = adata.obs["batch"]

combat = Combat()

Xc = combat.fit_transform(X, batch)

adata.layers["combat"] = Xc

adata.write_h5ad(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\combat.h5ad"
)

print("Done")