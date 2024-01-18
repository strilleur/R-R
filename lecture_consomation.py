import openpyxl
import time
import filelock

file_path = 'fichier_excel/consommation.xlsx'
sheet_name = "Sheet1"

#datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def write_to_consommation(traverse_ou_quai=None,time=0,MP1IN=0,MP1OUT=0,MP2IN=0,MP2OUT=0,MP3IN=0,MP3OUT=0,MP4IN=0,MP4OUT=0,GE1IN=0,GE1OUT=0,GE2IN=0,GE2OUT=0,GE3IN=0,GE3OUT=0,GE4IN=0,GE4OUT=0):
    # Acquire a file lock
    with filelock.FileLock(file_path + ".lock"):
        # Load the Excel file
        wb = openpyxl.load_workbook(file_path)
        sheet = wb[sheet_name]
        # Write data to the Excel sheet
        print("Data written to Excel.")
        if traverse_ou_quai==None:
            sheet.append({'A': time,'C': MP1IN, 'D':MP1OUT, 'E': MP1OUT-MP1IN, 'F': MP2IN, 'G':MP2OUT,'H': MP2OUT-MP2IN, 'I': MP3IN, 'J': MP3OUT, 'K': MP3OUT-MP3IN,'L': MP4IN, 'M': MP4OUT, 'N': MP4OUT-MP4IN, 'O': GE1IN,'P': GE1OUT, 'Q': GE1OUT-GE1IN , 'R':GE2IN , 'S':GE2OUT ,'T': GE2OUT-GE2IN, 'U': GE3IN, 'V': GE3OUT, 'W': GE3OUT-GE3IN,'X': GE4IN, 'Y': GE4OUT,'Z': GE4OUT-GE4IN})
        else:
            sheet.append({'A': time,})
        wb.save(file_path)

        
def read_from_consommation():
    # Acquire a file lock
    with filelock.FileLock(file_path + ".lock"):
        # Load the Excel file
        wb = openpyxl.load_workbook(file_path, data_only=True)
        sheet = wb[sheet_name]

        # Read data from the Excel sheet
        data = sheet["A1"].value
        print(f"Data read from Excel: {data}")

