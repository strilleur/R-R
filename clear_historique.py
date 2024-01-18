import openpyxl
import filelock
import time


file_path_consommation = 'fichier_excel/consommation.xlsx'

def lock_excel_file():
    # Create a file lock
    file_lock = filelock.FileLock(file_path_consommation + ".lock")
    max_attempts = 1  # Maximum attempts to acquire the lock
    attempt = 0
    
    while attempt < max_attempts:
        try:
            # Acquire the lock with a timeout of 20 seconds
            with file_lock.acquire(timeout=20):
                # Perform operations on the Excel file
                wb = openpyxl.load_workbook(file_path_consommation)
                sheet = wb.active
                sheet.delete_cols(1,53)
                sheet.append({'A': "datetime" ,'B': "depart-arrivé-escale", 'C':"MP1IN", 'D': "MP1OUT", 'E': "MP1total", 'F':"MP2IN",'G': "MP2OUT", 'H': "MP2total", 'I': "MP3IN", 'J': "MP3OUT",'K': "MP3total", 'L': "MP4IN", 'M': "MP4OUT", 'N': "MP4total",'O': "GE1OUT", 'P': "GE1OUT" , 'Q':"GE1total" , 'R':"GE2IN" ,'S': "GE2OUT", 'T': "GE2total", 'U': "GE3IN", 'V': "GE3OUT",'W': "GE3total", 'X': "GE4IN",'Y': "GE4OUT",'Z': "GE4total"})
                attempt += 1
        except filelock.Timeout:
            attempt += 1
            if attempt < max_attempts:
                time.sleep(1)  # Optional: Add a delay before retrying

        if attempt == max_attempts:
            print("Maximum attempts reached. Lock could not be acquired.")

lock_excel_file()