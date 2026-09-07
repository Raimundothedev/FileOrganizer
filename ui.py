import customtkinter as ctk

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(f"FileOrganizer{version}")

        
