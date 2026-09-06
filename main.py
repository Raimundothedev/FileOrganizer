from pathlib import Path

IMAGES = [".png", ".jpg", ".jpeg", ".gif"]
DOCUMENTS = [".pdf", ".docx", ".txt"]
VIDEOS = [".mp4", ".mkv", ".avi"]
SOUNDS = [".mp3", ".wav"]
PROGRAMS = [".exe", ".msi"]
COMPRESSED = [".zip", ".rar", ".7z"]

def inputs():

    while True:
        files_dir = (input("\nDigite o caminho da pasta que deseja organizar:" \
        "\n> "))

        if len(files_dir) == 2 and files_dir[1] == ":":
                files_dir += "\\"
        files_dir = Path(files_dir)

        if files_dir.exists():
            pass
        else:
            print("\nDigite um caminho válido")
            continue

        file_type = input("\nEscolha o tipo de arquivo que deseja organizar:" \
        "\n> 1 - Imagens"
        "\n> 2 - Vídeos"
        "\n> 3 - Documentos"
        "\n> 4 - Áudios"
        "\n> 5 - Programas"
        "\n> 6 - Compactados"
        "\n"
        "\n> ")

        new_diretory = input("\nDigite o nome da pasta que deseja criar/usar:" \
        "\n> ")

        diretory = files_dir / new_diretory

        return files_dir, file_type, diretory

def organize(files_dir, file_type, diretory):

    if file_type == "1":
        selected_type = IMAGES
    elif file_type == "2":
        selected_type = VIDEOS
    elif file_type == "3":
        selected_type = DOCUMENTS
    elif file_type == "4":
        selected_type = SOUNDS
    elif file_type == "5":
        selected_type = PROGRAMS
    elif file_type == "6":
        selected_type = COMPRESSED
    else:
        pass

    diretory.mkdir(exist_ok=True)

    while True:
        security_dialog = input(f"\nOs arquivos com final {selected_type} serão movidos para {diretory}. Confirmar? (y/n)" \
            "\n> ")
        if security_dialog == 'y':
            for file in files_dir.iterdir():
            
                    if file.is_file() and file.suffix.lower() in selected_type:
                        print(f"moved {file.name} to {diretory}")
                        file.rename(diretory / file.name)

            break

        elif security_dialog == 'n':
            start()
        else:
            print("Digite uma opção válida")
            continue 


def organize_diretory():
    file_dir, file_type, diretory = inputs()
    organize(file_dir, file_type, diretory)

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




def start():
    while True:
        print("\n======= Organizador de Arquivos =======")
        print("\n> 1- Organizar pasta                   ")
        print("> 2- Ver arquivos                      ")
        print("> 3- Histórico                         ")
        print("> 4- Sair                              ")
        print("\n====== Feito por @Raimundothedev ======")

        option = input("\nEscolha uma opção"
        "\n> ")

        if option == "1":
            organize_diretory()
            print("\nOrganizado com êxito!")
        elif option == "2":
            list_files()
        elif option == "3":
            pass
        elif option == "4":
            print("Saindo..")
            exit()
        else:
            print("Escolha uma opção válida")
            continue

if __name__ == "__main__":
    start()