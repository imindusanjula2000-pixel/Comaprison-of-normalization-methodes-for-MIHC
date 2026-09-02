from pathlib import Path

data_dir = Path(r"C:\Users\IMIDU SANJULA\Desktop\AP\syn12345")

print("Files found:\n")

for f in data_dir.rglob("*"):
    if f.is_file():
        print(f)