# demande a l'utilisateur de s'identifier.
# Il y aura 2 type d'utilisateur:
# L'utilisateur basique et l'utilisateur maintenance.
# L'utilisateur basique (UB pour faire simple) pourra observer les valeur et récupérer les rapports
# L'utilisateur maintenance pourra faire tout ce qque peut faire UB avec en plus la possiblité de changer les paramètres du capteur.

import tkinter
from tkinter import Tk
#import tkintermapview
import customtkinter

class window_Identification(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.UB="3210"
        self.UM="Admin"
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        wirth,lenth=800,480
        self.geometry(f"{wirth}x{lenth}")

        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=0)

        def gotowindowMenu(utilisateur):
            from Menu import window_Menu
            window_Menu(utilisateur)
            

        def tentative_de_connection():
            value_of_identifiant=identifiant.get()
            if(value_of_identifiant==self.UB):
                self.destroy()
                gotowindowMenu("utilisateur_basique")
            elif(value_of_identifiant==self.UM):
                self.destroy()
                gotowindowMenu("Admin")
            else:
                print("wrong ID")

        nameLabel=customtkinter.CTkLabel(master=self, width = 10, height = 150,text="Identification",font=("Times", 30))
        identifiant = customtkinter.CTkEntry(master=self,placeholder_text="identifient",font=("Times", 15))
        button = customtkinter.CTkButton(master=self, text="Connect", command=tentative_de_connection,font=("Times", 15))


        nameLabel.grid(row=0, column=1, padx=20, pady=(20, 10),sticky="ew")
        identifiant.grid(row=1, column=1, padx=20, pady=(20, 10),sticky="ew")
        button.grid(row=2, column=1, padx=20, pady=(20, 10),sticky="ew")
        
        self.mainloop()

window_Identification()