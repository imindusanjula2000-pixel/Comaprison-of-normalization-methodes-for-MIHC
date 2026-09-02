from pathlib import Path
from fcsparser import parse

fcs_file = next(
    Path(
        r"C:\Users\IMIDU SANJULA\Desktop\AP\syn12345"
    ).glob("*.fcs")
)

meta, data = parse(
    str(fcs_file),
    reformat_meta=True
)

print("FILE:")
print(fcs_file.name)

print("\nSHAPE:")
print(data.shape)

print("\nCHANNELS:")

for col in data.columns:
    print(col)
