from pathlib import Path
from fcsparser import parse
import pandas as pd
import anndata as ad
import numpy as np

DATA_DIR = r"C:\Users\IMIDU SANJULA\Desktop\AP\syn12345"

MARKERS = [
    "CD56","CD14","CD4","HLA-Dr",
    "Ki67","GrzB","IFNg","Epcam",
    "CD45","DCM","CD8",
    "CD11c","CD3"
]

all_data = []
all_obs = []

files = list(Path(DATA_DIR).glob("*.fcs"))

for f in files:

    if "Compensation Controls" in f.name:
        continue

    try:

        meta, df = parse(str(f))

        cols = [c for c in MARKERS if c in df.columns]

        if len(cols) < 5:
            continue

        tmp = df[cols].copy()

        sample = f.stem

        obs = pd.DataFrame({
            "sample_id": [sample]*len(tmp),
            "batch": [sample]*len(tmp)
        })

        all_data.append(tmp)
        all_obs.append(obs)

        print("Loaded:", sample)

    except Exception as e:
        print("Skip:", f.name, e)

X = pd.concat(all_data)
OBS = pd.concat(all_obs)

adata = ad.AnnData(
    X=X.values,
    obs=OBS,
    var=pd.DataFrame(index=X.columns)
)

adata.write(
    r"C:\Users\IMIDU SANJULA\Desktop\AP\Results\synapse_raw.h5ad"
)

print(adata)