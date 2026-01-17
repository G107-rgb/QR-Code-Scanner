import tkinter as tk
from tkinter import messagebox, filedialog
import os, cv2
from pyzbar.pyzbar import decode

C = "QR-Code Scanner" # Globale variable. von hier wird name des hauptfensters genommen
scanresult = ""

def changename():
    eingabe = eingabefeld.get() # Inhalt vom Eingabefeld holen
    root.title(eingabe) # Fensternamen ändern
    eingabefeld.delete(0, "end") # eingabe feld leeren von zeichen 0 (1. zeichen) bis letztes zeichen ("end")

def showscanresult():
    
    label2.config(text=f"Inhalt aus QR-Code: {scanresult}")

def choosefile():
    global scanresult  
    
    file = filedialog.askopenfilename(
        title="Bild auswählen",
        filetypes=[("Bilder", "*.png *.jpg *.jpeg *.bmp")]
    )
    
    if file:
        changebuttontext(file)
        image = cv2.imread(file)
        
        if image is None:
            scanresult = "Fehler: Bild laden fehlgeschlagen"
        else:
            found_codes = decode(image)
            if found_codes:
                
                scanresult = found_codes[0].data.decode('utf-8')
            else:
                scanresult = "Kein QR-Code erkannt."
        
        
        showscanresult()

def copytoclipboard():
    root.clipboard_append(scanresult)  # Inhalt von scanresult in Zwischenablage kopieren
    root.update() 
    messagebox.showinfo("Kopiert", "Inhalt wurde in die Zwischenablage kopiert.")

def changebuttontext(path):
    filename = os.path.basename(path)
    button1.config(text=f"{filename}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title(C) # Hauptfenster name definieren
    root.geometry("400x200") # Fenster größe definieren

    
    eingabefeld = tk.Entry(root, width=20) # Textfeld Breite in Zeichen
    eingabefeld.grid(row=0, column=0, padx=10, pady=10)
    
    button2 = tk.Button(root, text="Fenstername ändern", command=changename) 
    button2.grid(row=0, column=1, padx=10)
    
    label1 = tk.Label(root, text="Wählen Sie eine Datei aus.") 
    label1.grid(row=1, column=0, columnspan=2, pady=5)
    
    button1 = tk.Button(root, text="Bild auswählen", command=choosefile)
    button1.grid(row=2, column=0, columnspan=2, sticky="we", padx=10)

    
    label2 = tk.Label(root, text="Inhalt aus QR-Code: ")
    label2.grid(row=3, column=0, columnspan=2, sticky="w", pady=20)

    copybutton = tk.Button(root, text="Inhalt kopieren", command=copytoclipboard)
    copybutton.grid(row=3, column=2, pady=10)

    root.mainloop()