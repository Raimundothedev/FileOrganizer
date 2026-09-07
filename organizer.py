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
    moved_files = 0

    for file in files_dir.iterdir():
        if file.is_file() and file.suffix.lower() in selected_type:
            print(f"moved {file.name} to {directory}")
            file.rename(directory / file.name)
            moved = True
            moved_files += 1

    return moved, moved_files

def list_files():
    while True:
        file_dir = Path(input("\nDigite o caminho da pasta que deseja ver:" \
                "\n> "))
        if file_dir.exists():
            title = (f"=== Arquivos em {file_dir} ===")
            print(title)
            for file in file_dir.iterdir():
                if file.is_file:
                    
                    print(f"> {file.name}                 ")
            print("=" * len(title))
            exit = input("Voltar? (y/n)" \
            "\n> ")
            if exit == 'y':
                break
            elif exit == 'n':
                continue
            else:
                print("Digite uma opção válida")
                continue




            
            
        else:
            print("\nDigite um caminho válido")
            continue


