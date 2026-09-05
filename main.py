from pathlib import Path

files = Path("D:/")
directory = Path("D:/Imagens")
directory.mkdir(exist_ok=True)
images = [".png", ".jpg", ".jpeg", ".gif"]

for file in files.iterdir():
    if file.suffix in images:
        file.rename(directory / file.name)
