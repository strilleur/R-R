# demande a l'utilisateur de s'identifier.
# Il y aura 2 type d'utilisateur:
# L'utilisateur basique et l'utilisateur maintenance.
# L'utilisateur basique (UB pour faire simple) pourra observer les valeur et récupérer les rapports
# L'utilisateur maintenance pourra faire tout ce qque peut faire UB avec en plus la possiblité de changer les paramètres du capteur.

import tkinter
#import tkintermapview
import customtkinter
import os
from PIL import Image
#import Identification
#from Identification import window_Identification

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class window_Menu(customtkinter.CTk):

    def __init__(self,utilisateur):
        super().__init__()



        wirth,lenth,=800,480
        self.geometry(f"{wirth}x{lenth}")

        self.grid_columnconfigure((0,2), weight=1)
        self.grid_columnconfigure((1), weight=1)
        self.grid_rowconfigure((0, 1, 2,3,4,5,6), weight=1)

        
        def goto_menu_rapport_d_appareil():
            from menu_rapport_d_appareil import window_Menu_rapport
            self.destroy() 
            window_Menu_rapport=window_Menu_rapport(utilisateur)      
            window_Menu_rapport.mainloop() 

        def retour_identification():
            from Identification import window_Identification
            self.destroy()
            window_Identificatio=window_Identification()
            window_Identificatio.mainloop()
        def goto_menu_configuration():
            from configuration import window_configuration
            #from configuration import window_configuration
            #from configuration import execute_config
            self.destroy()
            window_configurationn= window_configuration(utilisateur)
            window_configurationn.show()
            

        def goto_menu_valeur_consommation():
            from valeurtotaliseur import window_Valeur_de_consommation
            self.destroy()
            window_Valeur_de_consommation=window_Valeur_de_consommation(utilisateur)
            window_Valeur_de_consommation.mainloop()
        def goto_menu_mapview():
            from mapview import window_mapview
            self.destroy()
            window_mapview=window_mapview()
            window_mapview.mainloop()



        custom_font =("Times",30,'bold')
        nameLabel=customtkinter.CTkLabel(master=self,text="Menu",font=("Times", 30))


        if utilisateur=="Admin":
            Rapport_d_appareil_mod = customtkinter.CTkButton(master=self,width= 160,height= 34, text="Rapport d'appareil modifiable",font=("Times", 20), command=goto_menu_rapport_d_appareil)
            Rapport_d_appareil_mod.grid(row=2, column=1, padx=20, pady=(20, 10),sticky="ew")
            Configuration = customtkinter.CTkButton(master=self, width= 160,height= 34,text="Configuration",font=("Times", 20), command=goto_menu_configuration)
            Configuration.grid(row=1, column=1, padx=20, pady=(20, 10),sticky="ew")
        if utilisateur=="utilisateur_basique":
            Rapport_d_appareil = customtkinter.CTkButton(master=self, width= 160,height= 34,text="Rapport d'appareil",font=("Times", 20), command=goto_menu_rapport_d_appareil)
            Rapport_d_appareil.grid(row=2, column=1, padx=20, pady=(20, 10),sticky="ew")
            

        Valeur_de_consomation = customtkinter.CTkButton(master=self, width= 160,height= 34,text="Valeur de consommation",font=("Times", 20), command=goto_menu_valeur_consommation)
        Carte_de_consommation = customtkinter.CTkButton(master=self,width= 160,height= 34, text="Carte de consommation",font=("Times", 20), command=goto_menu_mapview)
        boutton_retour = customtkinter.CTkButton(master=self,width= 160,height= 34, text="retour",font=("Times", 20), command=retour_identification)



        nameLabel.grid(row=0, column=1, padx=20, pady=(20, 10),sticky="ew")
        Valeur_de_consomation.grid(row=3, column=1, padx=20, pady=(20, 10),sticky="ew")
        Carte_de_consommation.grid(row=4, column=1, padx=20, pady=(20, 10),sticky="ew")
        boutton_retour.grid(row=5, column=1, padx=20, pady=(20, 10),sticky="ew")
        
        self.mainloop()

"""
Menu=window_Menu("Admin")
Menu.mainloop()
"""