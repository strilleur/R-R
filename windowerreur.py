
import minimalmodbus # Don't forget to import the library!!
import customtkinter
import os
from PIL import Image


class window_erreur(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("erreur")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        wirth,lenth=800,480
        self.geometry(f"{wirth}x{lenth}")
        label = customtkinter.CTkLabel(self, text="erreur d'écriture: L'erreur de communication peut être due a type d'écriture non adapter (integer,float ou string regarder la documentation pour les détailles  ) ", compound="left",font=("Times", 15), padx=5, anchor="w")
        label.grid(row=1, column=1, padx=5,pady=(0, 10), sticky="nsew")
        #window_erreur = window_erreur()
        

class window_erreur_text(customtkinter.CTk):
    def __init__(self,showtext):
        super().__init__()
        self.title("erreur")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("blue")
        wirth,lenth=400,300
        self.geometry(f"{wirth}x{lenth}")
        label = customtkinter.CTkLabel(self, text=showtext, compound="left",font=("Times", 15), padx=5, anchor="w")
        label.grid(row=1, column=1, padx=5,pady=(0, 10), sticky="nsew")
        window_erreur = window_erreur()
        window_erreur.mainloop()


