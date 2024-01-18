import customtkinter
import os
from PIL import Image

try:
    from récupération_des_address import getalladdress
except:
    print("error importation recuperation_donne")


try:
    getalladdress=getalladdress()
except:
    print("error using getalladdress")

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master,utilisateur="utilisateur_basique", command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master=master
        self.grid_columnconfigure(0, weight=1)
        
        self.command = command
        self.utilisateur=utilisateur
        
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []
    def retour_Window_menu(self):
        from Menu import window_Menu
        self.destroy()
        self.master.destroy()
        window_Menuu=window_Menu(self.utilisateur)
        window_Menuu.mainloop()
    def gotorapport(self,address):
        from rapport_appareil import window_rapport
        self.destroy()
        self.master.destroy()
        window_rapport=window_rapport(int(address),self.utilisateur)
        #window_rapport=window_rapport(11,"Admin")
        window_rapport.mainloop()
    def choix(self,address,label):
        if label=="retour":
            self.retour_Window_menu()
        else:
            self.gotorapport(address)

    def add_item(self, item,address, image=None):
        
        
        label = customtkinter.CTkLabel(self, text=item, image=image, compound="left", padx=5, anchor="w")
        button = customtkinter.CTkButton(self, text="afficher",command=lambda: self.choix(address,label.cget("text")) , width=100, height=24)
        
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button)
        

    def add_title(self, item):
        label = customtkinter.CTkLabel(self, text=item, font=("Times", 30))
        button_empty = customtkinter.CTkLabel(self, text=" ")
        label.grid(row=len(self.label_list), column=0, pady=(0, 10), sticky="nsew")  
        button_empty.grid(row=len(self.button_list), column=1, pady=(0, 10), padx=5)
        self.label_list.append(label)
        self.button_list.append(button_empty)
        

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
    

class window_Menu_rapport(customtkinter.CTk):
    def __init__(self,utilisateur):
        super().__init__()
        self.utilisateur=utilisateur
        
        self.title("CTkScrollableFrame example")
        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(2, weight=1)
        wirth,lenth = 800,500
        #self.geometry(f"{wirth}x{lenth}")
        #self.geometry("%dx%d+%d+%d" %(wirth,lenth,(self.winfo_screenwidth()-wirth)/2,(self.winfo_screenheight()-lenth)/2))
        #self.resizable(width=False, height=False)
        #self.attributes('-fullscreen', True)

        #current_dir="image projet\icone_rapport_d_appareil.png"
        #current_dir="image projet\icone_rapport_d'appareil.png"
        

        
            
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width = 1920, height = 1080,utilisateur=self.utilisateur, command=self.label_button_frame_event, corner_radius=0)
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")
        self.scrollable_label_button_frame.add_title(f"Menu apport d'appareil")
        self.scrollable_label_button_frame.add_item("retour",0)
        
        for i in range(len(getalladdress)):
            self.scrollable_label_button_frame.add_item(f"rapport du capteur {getalladdress[i]}",getalladdress[i])
        
        
        #self.scrollable_label_button_frame.add_item(f"rapport du capteur {11}",11)
        #self.scrollable_label_button_frame.add_item(f"rapport du capteur {12}",12)
    
    def label_button_frame_event(self, item):
        print(f"label button frame clicked: {item}")

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    window_Menu_rapport = window_Menu_rapport("Admin")
    window_Menu_rapport.state("zoomed")
    window_Menu_rapport.mainloop()



