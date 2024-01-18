import minimalmodbus # Don't forget to import the library!!
from openpyxl import Workbook 
from openpyxl import load_workbook
import datetime
import subprocess
from datetime import datetime
import time


class recuperationdonne():
    def __init__(self,address_appareil,utilisateur,**kwargs):
    #def __init__(self, address,**kwargs):    
        self.address_appareil=address_appareil
        self.utilisateur=utilisateur
        #self.mb_address = address # Modbus address of sensor
        address_appareil=address_appareil
        self.rs485communication = minimalmodbus.Instrument('/dev/ttyUSB0',address_appareil)	
        #self.rs485communication = minimalmodbus.Instrument('COM6',address_appareil)

        self.rs485communication.serial.baudrate = 19200				# BaudRate
        self.rs485communication.serial.bytesize = 8	# Number of data bits to be requested
        self.rs485communication.serial.parity = minimalmodbus.serial.PARITY_EVEN	# Parity Setting here is NONE but can be ODD or EVEN
        self.rs485communication.serial.stopbits = 1					# Number of stop bits
        self.rs485communication.serial.timeout  = 0.5		# Timeout time in seconds
        self.rs485communication.mode = minimalmodbus.MODE_RTU				# Mode to be used (RTU or ascii mode)
        #self.rs485communication.mode=minimalmodbus.BYTEORDER_BIG_SWAP
        """
        a tester avec la synchronisation du excel
        rs485communication.clear_buffers_before_each_transaction = True
        rs485communication.close_port_after_each_call = True
        """

    def read_rapport(self):
        self.Droits_d_accès_via_logiciel =self.rs485communication.read_register(2177,0,3)
        self.Entrer_code_d_accès =self.rs485communication.read_register(2176,0,3)

        self.Temporisation_alarme = self.rs485communication.read_float(6807,3,2,3) 

        self.Affecter_Numéro_de_diagnostic_046 =self.rs485communication.read_register(2755,0,3) 
        self.Affecter_Numéro_de_diagnostic_144 =self.rs485communication.read_register(2080,0,3) 
        self.Affecter_Numéro_de_diagnostic_832 =self.rs485communication.read_register(2758,0,3) 
        self.Affecter_Numéro_de_diagnostic_833 =self.rs485communication.read_register(2761,0,3) 
        self.Affecter_Numéro_de_diagnostic_834 =self.rs485communication.read_register(2760,0,3) 
        self.Affecter_Numéro_de_diagnostic_835 =self.rs485communication.read_register(2759,0,3) 
        self.Affecter_Numéro_de_diagnostic_912 =self.rs485communication.read_register(2757,0,3) 
        self.Affecter_Numéro_de_diagnostic_913 =self.rs485communication.read_register(2753,0,3) 
        self.Affecter_Numéro_de_diagnostic_944 =self.rs485communication.read_register(2081,0,3) 
        self.Affecter_Numéro_de_diagnostic_192=self.rs485communication.read_register(2021,0,3) 
        self.Affecter_Numéro_de_diagnostic_274=self.rs485communication.read_register(2754,0,3) 
        self.Affecter_Numéro_de_diagnostic_392=self.rs485communication.read_register(2022,0,3) 
        self.Affecter_Numéro_de_diagnostic_592 =self.rs485communication.read_register(2023,0,3) 
        self.Affecter_Numéro_de_diagnostic_992=self.rs485communication.read_register(2020,0,3) 

        self.Reset_appareil= self.rs485communication.read_register(6816,0,3) 
        self.Activer_options_software= self.rs485communication.read_register(2794,0,3) 
        self.Aperçu_des_options_logiciels=self.rs485communication.read_register(2901,0,3) 
        self.Sauvegarde_permanente = self.rs485communication.read_register(6906,0,3) 
        #self.Désignation_du_point_de_mesure= self.rs485communication.read_string(4900,0,3 )

        self.Débit_massique = self.rs485communication.read_float(2006,3,2,3)
        self.Débit_volumique = self.rs485communication.read_float(2008,3,2,3)
        self.Débit_volumique_corrigé = self.rs485communication.read_float(2010,3,2,3)
        self.Densité = self.rs485communication.read_float(2012,3,2,3)
        self.Densité_de_référence = self.rs485communication.read_float(2014,3,2,3)
        self.Température = self.rs485communication.read_float(2016,3,2,3)
        self.Valeur_de_pression = self.rs485communication.read_float(2088,3,2,3)


        self.Valeur_totalisateur_1 = self.rs485communication.read_float(2609,3,2,3)
        self.Dépassement_totalisateur_1 = self.rs485communication.read_float(2611,3,2,3)
        self.Valeur_totalisateur_2 = self.rs485communication.read_float(2809,3,2,3)
        self.Dépassement_totalisateur_2= self.rs485communication.read_float(2811,3,2,3)
        self.Valeur_totalisateur_3 = self.rs485communication.read_float(3009,3,2,3)
        self.Dépassement_totalisateur_3 = self.rs485communication.read_float(3011,3,2,3)

        self.Unité_de_débit_massique  = self.rs485communication.read_register(2100,0,3) 
        self.Unité_de_masse  = self.rs485communication.read_register(2101,0,3) 
        self.Unité_de_débit_volumique = self.rs485communication.read_register(2102,0,3) 
        self.Unité_de_volume  = self.rs485communication.read_register(2103,0,3) 
        self.Unité_du_débit_volumique_corrigé  =self.rs485communication.read_register(2104,0,3) 
        self.Unité_de_volume_corrigé  =self.rs485communication.read_register(2105,0,3) 
        self.Unité_de_densité =self.rs485communication.read_register(2106,0,3) 
        self.Unité_de_densité_de_référence =self.rs485communication.read_register(2107,0,3) 
        self.Unité_de_température =self.rs485communication.read_register(2108,0,3) 
        self.Unité_de_pression =self.rs485communication.read_register(2129,0,3) 
        self.Format_date_heure =self.rs485communication.read_register(2149,0,3) 


        #self.User_mass_text= self.rs485communication.read_string(2530,0,3 )
        self.User_mass_factor = self.rs485communication.read_float(2114,3,2,3)
        #self.User_volume_text= self.rs485communication.read_string(2541,0,3 )
        self.User_volume_factor  = self.rs485communication.read_float(2118,3,2,3)
        #self.User_corrected_volume_text= self.rs485communication.read_string(2567,0,3 )
        self.User_corrected_volume_factor = self.rs485communication.read_float(2572,3,2,3)
        #self.User_density_text= self.rs485communication.read_string(2548,0,3)
        self.User_density_offset = self.rs485communication.read_float(2555,3,2,3)
        self.User_density_factor  = self.rs485communication.read_float(2122,3,2,3)
        #self.User_pressure_text= self.rs485communication.read_string(2558,0,3 )
        self.User_pressure_offset = self.rs485communication.read_float(2565,3,2,3)
        self.User_pressure_factor= self.rs485communication.read_float(2563,3,2,3)

        self.Amortissement_débit =self.rs485communication.read_float(5509,3,2,3)
        self.Amortissement_densité =self.rs485communication.read_float(5507,3,2,3)
        self.Amortissement_température =self.rs485communication.read_float(5126,3,2,3)
        self.Dépassement_débit =self.rs485communication.read_register(5502,0,3)

        self.Affecter_variable_process_Suppression_débit_de_fuite =self.rs485communication.read_register(5100,0,3)
        self.Valeur_on_débit_de_fuite =self.rs485communication.read_float(5137,3,2,3)
        self.Valeur_off_débit_de_fuite =self.rs485communication.read_float(5103,3,2,3)
        self.Suppression_effet_pulsatoire =self.rs485communication.read_float(5139,3,2,3)
            
        self.Affecter_variable_process_Détection_tube_partiellement_rempli =self.rs485communication.read_register(5105,0,3)
        self.Valeur_basse_détect_tube_part_rempli =self.rs485communication.read_float(5109,3,2,3)
        self.Valeur_haute_détect_tube_part_rempl =self.rs485communication.read_float(5111,3,2,3)
        self.Tempsréponsedétect_tube_part_rempli =self.rs485communication.read_float(5107,3,2,3)
        self.Amortis_max_détect_tube_part_rempli =self.rs485communication.read_float(2413,3,2,3)

        self.Sélectionner_fluide =self.rs485communication.read_register(2441,0,3)
        """
            non utilisé
            self.Affecter_variable_process_Détection_tube_partiellement_rempli = self.rs485communication.read_register(5228,0,3)
            self.Tempsréponsedétect_tube_part_rempli = self.rs485communication.read_float(7412,3,2,3)
            self.Amortis_max_détect_tube_part_rempli = self.rs485communication.read_float(7410,3,2,3)
        """
            
        self.Compensation_de_pression = self.rs485communication.read_register(5183,0,3)
        self.Mode_de_température  = self.rs485communication.read_register(5514,0,3)
        """
            non utilisé
            self.Amortis_max_détect_tube_part_rempli = self.rs485communication.read_float(2439,3,2,3)
            self.Affecter_variable_process_Détection_tube_partiellement_rempli = self.rs485communication.read_register(5514,0,3)
            self.Tempsréponsedétect_tube_part_rempli = self.rs485communication.read_float(2506,3,2,3)
            """

        self.Calcul_du_débit_volumique_corrigé  =self.rs485communication.read_register(5128,0,3)
        self.Température_de_référence  =self.rs485communication.read_float(5135,3,2,3)
        self.Coefficient_de_dilation_linéaire  =self.rs485communication.read_float(5131,3,2,3)
        self.Coefficient_de_dilatation_au_carré  =self.rs485communication.read_float(5133,3,2,3)
            
        self.Sens_de_montage  =self.rs485communication.read_register(5500,0,3)

        self.Commande_d_ajustage_du_zéro  =self.rs485communication.read_register(5120,0,3)
        self.En_cours   =self.rs485communication.read_register(6796,0,3)

        self.Offset_de_débit_massique  =self.rs485communication.read_float(5520,3,2,3)
        self.Facteur_de_débit_massique  =self.rs485communication.read_float(5518,3,2,3)
        self.Offset_de_débit_volumique  =self.rs485communication.read_float(5524,3,2,3)
        self.Facteur_de_débit_volumique =self.rs485communication.read_float(5522,3,2,3)
        self.Offset_de_densité  =self.rs485communication.read_float(5528,3,2,3)
        self.Facteur_de_densité  =self.rs485communication.read_float(5526,3,2,3)
        self.Offset_de_débit_volumique_corrigé  =self.rs485communication.read_float(2043,3,2,3)
        self.Facteur_de_débit_volumique_corrigé  =self.rs485communication.read_float(2075,3,2,3)
        self.Offset_de_densité_de_référence  =self.rs485communication.read_float(2045,3,2,3)
        self.Facteur_de_densité_de_référence  =self.rs485communication.read_float(2041,3,2,3)
        self.Offset_de_température =self.rs485communication.read_float(5532,3,2,3)
        self.Facteur_de_température   =self.rs485communication.read_float(5530,3,2,3)


        self.Calibration_factor  =self.rs485communication.read_float(7512,3,2,3)
        self.Zero_point   =self.rs485communication.read_float(7526,3,2,3)
            #self.Nominal_diameter  =self.rs485communication.read_string(2047,0,3)
        self.C0 =self.rs485communication.read_float(7500,3,2,3)
        self.C1 =self.rs485communication.read_float(7502,3,2,3)
        self.C2 =self.rs485communication.read_float(7504,3,2,3)
        self.C3 =self.rs485communication.read_float(7506,3,2,3)
        self.C4 =self.rs485communication.read_float(7508,3,2,3)
        self.C5 =self.rs485communication.read_float(7510,3,2,3)


        self.Fréquence_d_oscillation_0  =self.rs485communication.read_float(9500,3,2,3)
        self.Fréquence_d_oscillation_1 =self.rs485communication.read_float(9502,3,2,3)
        self.Fluctuations_fréquence_0 =self.rs485communication.read_float(2497,3,2,3)
        self.Fluctuations_fréquence_1 =self.rs485communication.read_float(2499,3,2,3)
        self.Amplitude_de_l_oscillation_0 =self.rs485communication.read_float(2448,3,2,3)
        self.Amplitude_de_l_oscillation_1 =self.rs485communication.read_float(2450,3,2,3)
        self.Amortissement_de_l_oscillation_0 =self.rs485communication.read_float(9504,3,2,3)
        self.Amortissement_de_l_oscillation_1 =self.rs485communication.read_float(9506,3,2,3)
        self.Fluctuations_amortissement_tube_0  =self.rs485communication.read_float(2501,3,2,3)
        self.Fluctuations_amortissement_tube_1 =self.rs485communication.read_float(2503,3,2,3)
        self.Asymétrie_signal =self.rs485communication.read_float(2442,3,2,3)
        self.Température_électronique =self.rs485communication.read_float(2456,3,2,3)
        self.Carrier_pipe_temperature =self.rs485communication.read_float(9512,3,2,3)
        self.Courant_d_excitation_0 =self.rs485communication.read_float(9508,3,2,3)
        self.Courant_d_excitation_1 =self.rs485communication.read_float(9510,3,2,3)

        self.RawMassFlow=self.rs485communication.read_float(10231,3,2,3)

        self.Adresse_Bus  =self.rs485communication.read_register(4909,0,3)
        self.Baudrate  =self.rs485communication.read_register(4911,0,3)
        self.Mode_de_transfert_de_données  =self.rs485communication.read_register(4912,0,3)
        self.Parité  =self.rs485communication.read_register(4913,0,3)
        self.Byte_order  =self.rs485communication.read_register(4914,0,3)
        self.Telegram_delay=self.rs485communication.read_float(4915,3,2,3)
        self.Assign_diagnostic_behavior =self.rs485communication.read_register(4921,0,3)
        self.Failure_mode =self.rs485communication.read_register(4920,0,3)
        self.Interpreter_mode =self.rs485communication.read_register(4924,0,3)

        self.Registre_de_la_liste_de_scrutation_0 =self.rs485communication.read_register(5000,0,3)
        self.Registre_de_la_liste_de_scrutation_1 =self.rs485communication.read_register(5001,0,3)
        self.Registre_de_la_liste_de_scrutation_2 =self.rs485communication.read_register(5002,0,3)
        self.Registre_de_la_liste_de_scrutation_3 =self.rs485communication.read_register(5003,0,3)
        self.Registre_de_la_liste_de_scrutation_4 =self.rs485communication.read_register(5004,0,3)
        self.Registre_de_la_liste_de_scrutation_5 =self.rs485communication.read_register(5005,0,3)
        self.Registre_de_la_liste_de_scrutation_6 =self.rs485communication.read_register(5006,0,3)
        self.Registre_de_la_liste_de_scrutation_7 =self.rs485communication.read_register(5007,0,3)
        self.Registre_de_la_liste_de_scrutation_8 =self.rs485communication.read_register(5008,0,3)
        self.Registre_de_la_liste_de_scrutation_9 =self.rs485communication.read_register(5009,0,3)
        self.Registre_de_la_liste_de_scrutation_10 =self.rs485communication.read_register(5010,0,3)
        self.Registre_de_la_liste_de_scrutation_11 =self.rs485communication.read_register(5011,0,3)
        self.Registre_de_la_liste_de_scrutation_12 =self.rs485communication.read_register(5012,0,3)
        self.Registre_de_la_liste_de_scrutation_13 =self.rs485communication.read_register(5013,0,3)
        self.Registre_de_la_liste_de_scrutation_14 =self.rs485communication.read_register(5014,0,3)
        self.Registre_de_la_liste_de_scrutation_15 =self.rs485communication.read_register(5015,0,3)

        self.RAZ_tous_les_totalisateurs =self.rs485communication.read_register(2608,0,3)

        self.Affecter_variable_process_1  =self.rs485communication.read_register(2600,0,3)
        self.Unité_de_masse_1 =self.rs485communication.read_register(2601,0,3)
        self.Mode_de_fonctionnement_totalisateur_1 =self.rs485communication.read_register(2604,0,3)
            #self.Volume_unit  =self.rs485communication.read_register(2603,0,3)
            #self.Corrected_volume_unit =self.rs485communication.read_register(2604,0,3)
        self.Contrôle_totalisateur_1 =self.rs485communication.read_register(2607,0,3)
        self.Valeur_de_présélection_1 =self.rs485communication.read_register(2589,0,3)
        self.Mode_défaut_1   =self.rs485communication.read_register(2605,0,3)

        self.Affecter_variable_process_2 =self.rs485communication.read_register(2800,0,3)
        self.Unité_de_masse_2 =self.rs485communication.read_register(2801,0,3)
        self.Mode_de_fonctionnement_totalisateur_2 =self.rs485communication.read_register(2802,0,3)
            #self.Volume_unit = self.rs485communication.read_register(2803,0,3)
            #self.Corrected_volume_unit = self.rs485communication.read_register(2804,0,3)
        self.Contrôle_totalisateur_2 =self.rs485communication.read_register(2807,0,3)
        self.Valeur_de_présélection_2 =self.rs485communication.read_register(2591,0,3)
        self.Mode_défaut_2   =self.rs485communication.read_register(2805,0,3)

        self.Affecter_variable_process_3 =self.rs485communication.read_register(3000,0,3)
        self.Unité_de_masse_3 =self.rs485communication.read_register(3001,0,3)
        self.Mode_de_fonctionnement_totalisateur_3 =self.rs485communication.read_register(3004,0,3)
            #self.Volume_unit = self.rs485communication.read_register(3002,0,3)
            #self.Corrected_volume_unit = self.rs485communication.read_register(2604,0,3)
        self.Contrôle_totalisateur_3 = self.rs485communication.read_register(2607,0,3)
        self.Valeur_de_présélection_3 = self.rs485communication.read_register(2589,0,3)
        self.Mode_défaut_3   = self.rs485communication.read_register(2605,0,3)
            #page 22 ou 13 rapport
            #possible erreur sur Diagnostic_actuel car il est dis de luis qu'il est un interger masi il affiche pourtant des string  !!!!!!!!!
        """
            self.Diagnostic_actuel = self.rs485communication.read_register(2731,0,3)
            self.Dernier_diagnostic = self.rs485communication.read_string(2718,0,3 )
            self.Temps_de_fct_depuis_redémarrage = self.rs485communication.read_string(2623,0,3 )
            self.Temps_de_fonctionnement = self.rs485communication.read_string(2630,0,3 )

            self.Désignation_du_point_de_mesure = self.rs485communication.read_string(2025,0,3 )
            self.Numéro_de_série  = self.rs485communication.read_string(7002,0,3 )
            self.Version_logiciel  = self.rs485communication.read_string(7276,0,3 )
            self.Nom_d_apparei = self.rs485communication.read_string(7262,0,3 )
            self.Code_commande = self.rs485communication.read_string(2057,0,3 )
            self.Version_ENP = self.rs485communication.read_string(4002,0,3 )
            self.Compteur_configuration  = self.rs485communication.read_string(3100,0,3 )
            
            self.Référence_de_commande_1 = self.rs485communication.read_string(2211,0,3 )
            self.Référence_de_commande_2 = self.rs485communication.read_string(2221,0,3 )
            self.Référence_de_commande_3  = self.rs485communication.read_string(2231,0,3 )
        """
        self.Valeur_minimale_Température_électronique=self.rs485communication.read_float(2420,3,2,3)
        self.Valeur_maximale_Température_électronique=self.rs485communication.read_float(2418,3,2,3)

        self.Valeur_minimale_Température_du_fluide=self.rs485communication.read_float(7528,3,2,3)
        self.Valeur_maximale_Température_du_fluide=self.rs485communication.read_float(7530,3,2,3)

        self.Valeur_minimale_Fréquence_d_oscillation=self.rs485communication.read_float(2458,3,2,3)
        self.Valeur_maximale_Fréquence_d_oscillation=self.rs485communication.read_float(2467,3,2,3)
            
        self.Valeur_minimale_Amplitude_de_l_oscillation=self.rs485communication.read_float(2471,3,2,3)
        self.Valeur_maximale_Amplitude_de_l_oscillation=self.rs485communication.read_float(2469,3,2,3)

        self.Valeur_minimale_Amortissement_de_l_oscillation=self.rs485communication.read_float(2477,3,2,3)
        self.Valeur_maximale_Amortissement_de_l_oscillation=self.rs485communication.read_float(2422,3,2,3)
            
        self.Valeur_minimale_Asymétrie_signal=self.rs485communication.read_float(2473,3,2,3)
        self.Valeur_maximale_Asymétrie_signal=self.rs485communication.read_float(2475,3,2,3)

        self.Year =self.rs485communication.read_register(2494,0,3)
        self.Month =self.rs485communication.read_register(2493,0,3)
        self.Day =self.rs485communication.read_register(2492,0,3)
        self.Hour =self.rs485communication.read_register(2491,0,3)

        
    def read_consommation(self):
            
        self.consommation=self.rs485communication.read_float(2609,3,2,3)
            

    def write_register_sensor(self,addresse_register,value):
        self.rs485communication.write_register(addresse_register,value)

    def write_float_sensor(self,addresse_register,value):
        self.rs485communication.write_float(addresse_register,value,2,3)

    def write_string_sensor(self,addresse_register,value):
        self.rs485communication.write_register(addresse_register,value)
    print("finis")

#recuperationdonnee=recuperationdonne(address_appareil=11,utilisateur="Admin")

