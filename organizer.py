from pathlib import Path

IMAGES = [".png", ".jpg", ".jpeg", ".gif"]
DOCUMENTS = [".pdf", ".docx", ".txt"]
VIDEOS = [".mp4", ".mkv", ".avi"]
SOUNDS = [".mp3", ".wav"]
PROGRAMS = [".exe", ".msi"]
COMPRESSED = [".zip", ".rar", ".7z"]
HTML = [".html"]
ASESPRITE = [".ase"]

def organize(files_dir, file_type, directory):

    files_dir = Path(files_dir)
    directory = directory

    if directory.exists():
        print("existe")


    types = {
    "Imagens": IMAGES,
    "Vídeos": VIDEOS,
    "Documentos": DOCUMENTS,
    "Áudios": SOUNDS,
    "Programas": PROGRAMS,
    "Compactados": COMPRESSED,
    "HTML": HTML,
    "Asesprite" : ASESPRITE
}

    selected_type = types.get(file_type)

    directory.mkdir(exist_ok=True)

    moved = False
    moved_files = []

    for file in files_dir.iterdir():
        if file.is_file() and file.suffix.lower() in selected_type:
            file.rename(directory / file.name)
            moved = True
            moved_files.append(file.name)

    return moved, moved_files



