#rapport_d_appareil
#

import customtkinter
import os
from PIL import Image

"""
try:
    from recuperation_donne import recuperationdonne
except:
    print("error importation recuperation_donne")

try:
    recuperationdonne=recuperationdonne()
except:
    print("error using recuperationdonne")
"""
class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure((0,1,2), weight=1)
        #self.grid_columnconfigure((0), weight=2)
        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []
        self.nameEntry_list= []

    def what_to_do():
        print("help")
        
    def add_item(self, item,input,readandwrite=True,image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="Confirmé", width=100, height=24,)
        nameEntry = customtkinter.CTkEntry(master=self,placeholder_text=input,font=("Times", 15))
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        
        label.grid(row=len(self.label_list), column=0, padx=5,pady=(0, 10), sticky="nsew")
        nameEntry.grid(row=len(self.nameEntry_list), column=1,padx=5, pady=(0, 10),sticky="nsew")
        button.grid(row=len(self.button_list), column=2,padx=5, pady=(0, 10),sticky="nsew")

        self.label_list.append(label)
        self.button_list.append(button)
        self.nameEntry_list.append(nameEntry)

    def add_itemtitle(self, item, image=None):
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        labelremplissage = customtkinter.CTkLabel(self, text=None, image=image, compound="left", padx=5, anchor="w")
        label.grid(row=len(self.label_list), column=0,padx=2, pady=(0, 10), sticky="w")
        labelremplissage.grid(row=len(self.label_list), column=1,padx=5, pady=(0, 10), sticky="w")
        labelremplissage.grid(row=len(self.label_list), column=2,padx=5, pady=(0, 10), sticky="w")
        self.label_list.append(label)
        self.nameEntry_list.append(labelremplissage)
        self.button_list.append(labelremplissage)
        

    def add_liste_a_choix(self,Label,valeur_du_capteur,liste_des_choix):
        def write():
            value=liste_a_choix.get()
            print(" valeur actuelle:--")

            #write_float_sensor(registre,2,3)
            print(value,"----")
            
        label=customtkinter.CTkLabel(self, text= Label ,compound="left", padx=5, anchor="w")
        liste_a_choix = customtkinter.CTkComboBox(self,values=liste_des_choix)
        button = customtkinter.CTkButton(self, text="Confirmé",command=write, width=100, height=24,)

        label.grid(row=len(self.label_list), column=0,padx=5, pady=(0, 10), sticky="w")
        liste_a_choix.grid(row=len(self.label_list), column=1, padx=5, pady=(0, 10), sticky="nsew")
        button.grid(row=len(self.label_list), column=2,padx=5, pady=(0, 10), sticky="nsew")

        self.label_list.append(label)
        self.nameEntry_list.append(liste_a_choix)
        self.button_list.append(button)
        liste_a_choix.set(valeur_du_capteur)    
        

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
    #traduire les valeurs numérique en string
    #def traduction_numérique_to_string(self,valeur_bits): 
    #def traduction_string_to_numérique(self,valeur_bits):     
 

class window_rapport(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Rapport d'appareil")
        #self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        #current_dir="image projet\icone_rapport_d'appareil.png"
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=900,height=800, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=0, padx=5, pady=0, sticky="nsew")
        # ajout d'item dans le rapport
        

        #self.scrollable_label_button_frame.add_liste_a_choix(f"l/h",("P","l/h","m/s"))
        #expert
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t expert")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t expert")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t État verrouillage")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t Droits d'accès via logiciel "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t Entrer code d'accès "," ")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t expert")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Traitement événement")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t  Traitement événement")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Traitement événement "," ")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Comportement du diagnostic")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t  Comportement du diagnostic")
        #self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.140",traduction_capt_to_ordi_Affecter_Numéro_de_diagnostic(),["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.046","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.144","Warning",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.832","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.833","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.834","Warning",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.835","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.912","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.913","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.944","Warning",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.192","Warning",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.274","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.392","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.592","Alarm",["off","Logbook entry only","Warning","Alarm"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t\t Affecter Numéro de diagnostic no.992","Alarm",["off","Logbook entry only","Warning","Alarm"])


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Administration")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t  Administration")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Reset appareil","Cancel",["Cancel","Restart device","To delivery setting"])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Activer options software "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Aperçu des options logiciels "," ")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Sauvegarde permanente","on",["off","on"])
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Désignation du point de mesure  ",recuperationdonne.)

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Valeur mesurée")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Variables process")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t  Variables process")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Débit massique  "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Débit volumique  "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Débit volumique corrigé "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Densité  "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Densité de référence "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Température "," ")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Valeur de pression "," ")
        """
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Totalisateur")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t  Totalisateur")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur totalisateur 1 ",recuperationdonne.Valeur_totalisateur_1)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Dépassement totalisateur 1 ",recuperationdonne.Dépassement_totalisateur_1)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur totalisateur 2  ",recuperationdonne.Valeur_totalisateur_2)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Dépassement totalisateur 2  ",recuperationdonne.Dépassement_totalisateur_2)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur totalisateur 3 ",recuperationdonne.Valeur_totalisateur_3)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Dépassement totalisateur 3 ",recuperationdonne.Dépassement_totalisateur_3)

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Unités système")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Unités système")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de débit massique",recuperationdonne.Unité_de_débit_massique,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de masse",recuperationdonne.Unité_de_masse,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de débit volumique",recuperationdonne.Unité_de_débit_volumique,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de volume",recuperationdonne.Unité_de_volume,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité du débit volumique corrigé",recuperationdonne.Unité_du_débit_volumique_corrigé,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de volume corrigé ",recuperationdonne.Unité_de_volume_corrigé,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de densité",recuperationdonne.Unité_de_densité,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de densité de référence ",recuperationdonne.Unité_de_densité_de_référence,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de température",recuperationdonne.Unité_de_température,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de pression  ",recuperationdonne.Unité_de_pression,["g/s","on"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Format date/heure",recuperationdonne.Format_date_heure,["g/s","on"])



        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Unités spécifiques utilisateur")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Unités spécifiques utilisateur")
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Nom unité masse utilisateur  ",recuperationdonne.)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Facteur masse utilisateur ",recuperationdonne.User_mass_factor)
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Nom unité volume utilisateur   ",recuperationdonne.)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Facteur volume utilisateur ",recuperationdonne.User_volume_factor)
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Nom unité volume corrigé utilisateur  ",recuperationdonne.)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Facteur volume corrigé utilisateur  ",recuperationdonne.User_corrected_volume_factor)
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Nom unité densité utilisateur   ",recuperationdonne.)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Offset densité utilisateur  ",recuperationdonne.User_density_offset)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Facteur densité utilisateur  ",recuperationdonne.User_density_factor)
        #self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Texte pression utilisateur ",recuperationdonne.)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Compensation de pression utilisateur   ",recuperationdonne.User_pressure_offset)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t Facteur de pression utilisateur  ",recuperationdonne.User_pressure_factor)


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Paramètres process")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Paramètres process")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortissement débit ",recuperationdonne.Amortissement_débit)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortissement densité ",recuperationdonne.Amortissement_densité)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortissement température ",recuperationdonne.Amortissement_température)
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Dépassement débit ",recuperationdonne.Dépassement_débit,["On","Off"])

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Suppression débit de fuite")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Suppression débit de fuite")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Affecter variable process",recuperationdonne.Affecter_variable_process_Suppression_débit_de_fuite,["Off","Mass flow","Volume flow","Corrected volume flow"])     
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur 'on' débit de fuite",recuperationdonne.Valeur_on_débit_de_fuite)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur 'off' débit de fuite ",recuperationdonne.Valeur_off_débit_de_fuite)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Suppression effet pulsatoire  ",recuperationdonne.Suppression_effet_pulsatoire)



        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Détection tube partiellement rempli")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Détection tube partiellement rempli")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Assign process variable",recuperationdonne.Affecter_variable_process_Détection_tube_partiellement_rempli,["Off ","Density","Reference density"])   
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur basse détect. tube part. rempli",recuperationdonne.Valeur_basse_détect_tube_part_rempli)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur haute détect. tube part. rempli  ",recuperationdonne.Valeur_haute_détect_tube_part_rempl)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Temps réponse détect. tube part. rempl  ",recuperationdonne.Tempsréponsedétect_tube_part_rempli)
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortis. max. détect. tube part. rempli  ",recuperationdonne.Amortis_max_détect_tube_part_rempli)


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Mode de mesure")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Mode de mesure")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Sélectionner fluide ",recuperationdonne.Sélectionner_fluide)


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Compensation externe")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Compensation externe")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Compensation de pression ",recuperationdonne.Compensation_de_pression,["Off ","Fixed value","External value"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode de température  ",recuperationdonne.,["Internal measured value ","External value"])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Mode de température    ",recuperationdonne.)
        """

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Valeurs calculées")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Calcul du débit volumique corrigé")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Calcul du débit volumique corrigé")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Compensation de pression ","Off",["Calculated reference density ","Fixed reference density","External reference density","Reference density by API table 53"])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Température de référence    ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Coefficient de dilation linéaire    ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Coefficient de dilatation au carré    ","value")


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Ajustage capteur")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Ajustage capteur")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Sens de montage  ","value")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Sens de montage  ","Flow in arrow direction",["Flow in arrow direction ","Flow against arrow direction"])

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Ajustage du zéro")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Ajustage du zéro")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Commande d'ajustage du zéro  ","Cancel ",["Cancel  ","Start","Zero point adjust failure","Busy"])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t En cours  ","value")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Ajustage densité")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Ajustage variable process")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t\t Ajustage variable process")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de débit massique    ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de débit massique    ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de débit volumique     ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de débit volumique     ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de densité     ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de densité     ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de débit volumique corrigé     ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de débit volumique corrigé   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de densité de référence   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de densité de référence      ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Offset de température   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t\t\t Facteur de température   ","value")


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Étalonnage")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Étalonnage")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Facteur d'étalonnage   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Zéro   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Diamètre nominal  ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C0  ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C2   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C3   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C4   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t C5   ","value")


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Points test")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Points test")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Fréquence d'oscillation 0  ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Fréquence d'oscillation 1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Fluctuations fréquence 0   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Fluctuations fréquence 1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amplitude de l'oscillation 0   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amplitude de l'oscillation 1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortissement de l'oscillation 0  ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Amortissement de l'oscillation 1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Fluctuations amortissement tube 0   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t  Fluctuations amortissement tube 1   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t symétrie signal   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Température électronique  ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Courant d'excitation 0   ","value")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Courant d'excitation 1   ","value")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Raw values")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t RawMassFlow  ","value")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Supervision")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Oscillation")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Limit value measuring tube damping ","value")

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t Communication")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Configuration Modbus")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Configuration")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Baudrate  ","19200 baud ",["1200 BAUD" ,"2400 BAUD" , "4800 BAUD" "9600 BAUD" ," 19200 BAUD" , "38400 BAUD" ,"57600 BAUD", "115200 BAUD"])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode de transfert de données    ","RTU",[" RTU" ,"ASCII" ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Parité ","Even ",[" Even " ,"Odd" ,"None / 2 stop bits" ,"None / 1 stop bit" ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Ordre des octets  "," 1-0-3-2 ",["  0-1-2-3 " ,"3-2-1-0" ,"2-3-0-1" ," 1-0-3-2 " ])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Délai Télégramme ","value")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Assign diagnostic behavior  ","Alarm  ",[" Off " ,"Warning" ,"Alarm " ,"Alarm or warning" ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode défau  ","Alarm  ",["  NaN value  " ," Last valid value" ,"Alarm " ,"Alarm or warning" ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode interpréteur   ","Standard  ",[" Standard " ,"Ignore surplus bytes" ])



        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t Application")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Application")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t RAZ tous les totalisateurs ","Cancel   ",[" Cancel  " ,"Reset + totalize" ])

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Totalisateur 1")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Totalisateur 1")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Affecter variable process   ","Alarm  ",[' Off ', ' Mass flow (Default) ', ' Volume flow ', ' Corrected volume flow ', ' Target mass flow ', 'Carrier mass flow' ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de masse  ","t ",[' g ', ' kg  ', ' t ', ' oz ', ' lb ', ' STon ', ' User mass'])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode de fonctionnement totalisateur ","Net flow total   ",[' Net flow total (Default) ', ' Forward flow total ', ' Reverse flow total'] )
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Contrôle totalisateur 1 ","Totalize   ",[" Totalize " ,"Reset + totalize" ,"Preset + hold " ,"Reset + hold","Preset + totalize" ])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur de présélection 1 ","value")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode défaut ","Stop   ",[" Stop  " ,"Actual value","Last valid value" ])

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Totalisateur 2")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Totalisateur 2")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Affecter variable process   ","Alarm  ",[' Off ', ' Mass flow (Default) ', ' Volume flow ', ' Corrected volume flow ', ' Target mass flow ', 'Carrier mass flow' ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de masse  ","kg  ",[' g ', ' kg  ', ' t ', ' oz ', ' lb ', ' STon ', ' User mass'])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode de fonctionnement totalisateur ","Net flow total   ",[' Net flow total (Default) ', ' Forward flow total ', ' Reverse flow total'] )
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Contrôle totalisateur 1 ","Totalize   ",[" Totalize " ,"Reset + totalize" ,"Preset + hold " ,"Reset + hold","Preset + totalize" ])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur de présélection 1 ","value")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode défaut ","Stop   ",[" Stop  " ,"Actual value","Last valid value" ])


        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Totalisateur 3")
        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t\t Totalisateur 3")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Affecter variable process   ","Alarm  ",[' Off ', ' Mass flow (Default) ', ' Volume flow ', ' Corrected volume flow ', ' Target mass flow ', 'Carrier mass flow' ])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Unité de masse  ","kg",[' g ', ' kg  ', ' t ', ' oz ', ' lb ', ' STon ', ' User mass'])
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode de fonctionnement totalisateur ","Net flow total   ",[' Net flow total (Default) ', ' Forward flow total ', ' Reverse flow total'] )
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Contrôle totalisateur 1 ","Totalize   ",[" Totalize " ,"Reset + totalize" ,"Preset + hold " ,"Reset + hold","Preset + totalize" ])
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur de présélection 1 ","value")
        self.scrollable_label_button_frame.add_liste_a_choix("\t\t\t\t\t\t Mode défaut ","Stop   ",[" Stop  " ,"Actual value","Last valid value" ])
#page 13

        self.scrollable_label_button_frame.add_itemtitle(f"\t\t\t\t\t Diagnostic")
        self.scrollable_label_button_frame.add_item(f"\t\t\t\t\t\t Valeur de présélection 1 ","value")



    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")


if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    window_rapport = window_rapport()
    window_rapport.mainloop()