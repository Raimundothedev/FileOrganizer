import customtkinter as ctk
from config import Config
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
import organizer

ctk.set_appearance_mode(Config.THEME)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"FileOrganizer | {Config.VERSION}")
        self.geometry("900x600")

        self.create_widgets()

        self.files_dir = None
        self.file_type = "Imagens"

    #========================
    # Create Widgets
    #========================    

    def create_widgets(self):

        self.title_label = ctk.CTkLabel(
            self,
            text="FileOrganizer",
            font=ctk.CTkFont(size=28, weight="bold",family="Georgia")
        )
        self.title_label.pack(pady=20)

        self.label_dir = ctk.CTkLabel(
            self,
            text="Selecione um diretório:",
            font=ctk.CTkFont(size=18,family="Georgia")
        )
        self.label_dir.pack(pady=(20, 0))

        self.dir_frame = ctk.CTkFrame(self)
        self.dir_frame.pack(pady=(10, 0))

        self.btn_dir = ctk.CTkButton(
            self.dir_frame,
            text="Selecionar pasta",
            font=ctk.CTkFont(family="Georgia"),
            command=self.select_dir
        )
        self.btn_dir.pack(side="left")

        self.btn_deselect_dir = ctk.CTkButton(
            self.dir_frame,
            text="X",
            width=40,
            font=("Georgia", 16, "bold"),
            command=self.deselect_dir,
            fg_color="red",
            hover_color="darkred"
        )
        self.btn_deselect_dir.pack(side="left", padx=(5, 0))

        self.label_type = ctk.CTkLabel(
                    self,
                    text="Selecione o arquivo que quer organizar: ",
                    font=ctk.CTkFont(size=18,family="Georgia"),
        )
        self.label_type.pack(pady=(20, 0))

        self.opt_type = ctk.CTkOptionMenu(
            self,
            values=["Imagens", "Vídeos", "Documentos", "Áudios", "Programas", "Compactados", "HTML", "Asesprite"],
            font=ctk.CTkFont(family="Georgia"),
            command=self.get_file_type
        )
        self.opt_type.pack(pady=(10, 0))

        self.label_dir_name = ctk.CTkLabel(
                            self,
                            text="Digite o nome da pasta que deseja criar/usar: ",
                            font=ctk.CTkFont(size=18,family="Georgia")
                        )
        self.label_dir_name.pack(pady=(20, 0))

        self.dir_name_input = ctk.CTkEntry(
            self,
            placeholder_text="Examplefolder",
            width=200,
        )
        self.dir_name_input.pack(pady=(10, 0))

        self.btn_organize = ctk.CTkButton(
            self,
            text="Organizar",
            font=ctk.CTkFont(family="Georgia"),
            command=self.organize
        )
        self.btn_organize.pack(pady=(10, 0))

    #========================
    # Functions
    #========================

    def select_dir(self):
        self.files_dir = filedialog.askdirectory()
        files_dir = self.files_dir

        if files_dir:
            if len(files_dir) > 50:
                files_dir = files_dir[:25] + "..." + files_dir[-22:]
            self.btn_dir.configure(
                text=f"{files_dir}"
            )
    def deselect_dir(self):
        self.files_dir = None

        if not self.files_dir:
            self.btn_dir.configure(
                            text=f"Selecionar pasta"
                        )

    def get_file_type(self, file_type):
        self.file_type = file_type

    def get_file_input(self):
        self.file_input = self.dir_name_input.get().strip()
        

    def organize(self):
        self.get_file_input()
        directory = Path(self.files_dir) / self.file_input
        file_type = self.file_type
        files_dir = self.files_dir

        confirm = messagebox.askyesno(
            "Confirmar organização",
            f"Diretório: {files_dir}\n"
            f"Tipo: {file_type}\n"
            f"Pasta destino: {directory}\n\n"
            "Deseja continuar?"
        )

        if not confirm:
            return
    
        moved, moved_files = organizer.organize(
            files_dir,
            file_type,
            directory
        )
        if moved:
            messagebox.showinfo(
            "FileOrganizer",
            f"Organização concluida com êxito!\n Foram movidos {moved_files} arquivos."
        )
        else:
            messagebox.showinfo(
            "FileOrganizer",
            "Nenhum arquivo foi encontrado"
        )


    
        

def start_ui():
    window = App()
    window.mainloop()

        
