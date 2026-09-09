import customtkinter as ctk
from config import Config
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path
import organizer
import webbrowser

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

        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=18
        )
        self.main_frame.pack(
            padx=50,
            pady=35,
            fill="both",
            expand=True
        )

        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="FileOrganizer",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=32,
                weight="bold"
            )
        )
        self.title_label.pack(pady=(30, 5))

        self.subtitle_label = ctk.CTkLabel(
            self.main_frame,
            text="Organize seus arquivos de forma simples e rápida.",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        )
        self.subtitle_label.pack(pady=(0, 25))

        # Diretório

        self.label_dir = ctk.CTkLabel(
            self.main_frame,
            text="DIRETÓRIO",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=13,
                weight="bold"
            )
        )
        self.label_dir.pack(anchor="w", padx=80)

        self.dir_frame = ctk.CTkFrame(
            self.main_frame,
            fg_color="transparent"
        )
        self.dir_frame.pack(
            fill="x",
            padx=80,
            pady=(7, 20)
        )

        self.btn_dir = ctk.CTkButton(
            self.dir_frame,
            text="Selecionar pasta",
            height=40,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            ),
            command=self.select_dir
        )
        self.btn_dir.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.btn_deselect_dir = ctk.CTkButton(
            self.dir_frame,
            text="×",
            width=45,
            height=40,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=20,
                weight="bold"
            ),
            command=self.deselect_dir,
            fg_color="transparent",
            hover_color=("gray80", "gray25"),
            text_color=("gray20", "gray90")
        )
        self.btn_deselect_dir.pack(
            side="left",
            padx=(7, 0)
        )

        # Tipo

        self.label_type = ctk.CTkLabel(
            self.main_frame,
            text="TIPO DE ARQUIVO",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=13,
                weight="bold"
            )
        )
        self.label_type.pack(anchor="w", padx=80)

        self.opt_type = ctk.CTkOptionMenu(
            self.main_frame,
            values=[
                "Imagens",
                "Vídeos",
                "Documentos",
                "Áudios",
                "Programas",
                "Compactados",
                "HTML",
                "Asesprite"
            ],
            height=40,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            ),
            command=self.get_file_type
        )
        self.opt_type.pack(
            fill="x",
            padx=80,
            pady=(7, 20)
        )

        # Pasta de destino

        self.label_dir_name = ctk.CTkLabel(
            self.main_frame,
            text="PASTA DE DESTINO",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=13,
                weight="bold"
            )
        )
        self.label_dir_name.pack(anchor="w", padx=80)

        self.dir_name_input = ctk.CTkEntry(
            self.main_frame,
            placeholder_text="Ex.: Imagens",
            height=40,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14
            )
        )
        self.dir_name_input.pack(
            fill="x",
            padx=80,
            pady=(7, 25)
        )

        # Organizar

        self.btn_organize = ctk.CTkButton(
            self.main_frame,
            text="Organizar arquivos",
            height=45,
            width=250,
            font=ctk.CTkFont(
                family="Segoe UI",
                size=15,
                weight="bold"
            ),
            command=self.organize
        )
        self.btn_organize.pack(pady=(0, 25))

        # Github Button


        self.github_link = ctk.CTkLabel(
            self.main_frame,
            text=f"{Config.GIT_HUB_REPOSITORY}",
            text_color="#4A90E2",
            cursor="hand2",
            font=ctk.CTkFont(
                family="Segoe UI",
                size=14,
                underline=True
            )
        )

        self.github_link.pack(side="bottom")

        self.github_link.bind(
            "<Button-1>",
            lambda event: webbrowser.open(Config.GIT_HUB_REPOSITORY)
        )

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
        return self.file_type

    def get_file_input(self):
        self.file_input = self.dir_name_input.get().strip()
        return self.file_input
        

    def organize(self):
        if not self.get_file_input() or not self.file_type or not self.files_dir:
            input_error = messagebox.showwarning(
                "INPUT ERROR",
                "É necessario preencher todas as informações disponíveis."
            )
            return
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

        
