import tkinter as tk
from tkinter import messagebox, filedialog
import os, cv2
from pyzbar.pyzbar import decode

def changename():
    eingabe = eingabefeld.get()   # Inhalt vom Eingabefeld holen
    root.title(eingabe) # Fensternamen ändern
    print(f"Fenstername geändert zu: {eingabe} und eingabe feld geleert")
    eingabe = "" # wert löschen von variable
    eingabefeld.delete(0, "end") # eingabe feld leeren von zeichen 0 (1. zeichen) bis letztes zeichen ("end")

def choosefile():
    file = filedialog.askopenfilename(
        title="Bild",
        filetypes=[("Bilder", "*.png *.jpg *.jpeg *.bmp")]
    )
    if file:
        print(f"Gewähltes Bild: {file}")
        changebuttontext(file)

        image = cv2.imread(file)
        if image is None:
            print("Fehler: Bild konnte nicht geladen werden!")
            return

        codes = decode(image)
        if codes:
            for code in codes:
                print(f"Gefunden: {code.data.decode('utf-8')}")
        else:
            print("Kein QR-Code erkannt.")
        

def changebuttontext(path):
    filename = os.path.basename(path)
    button1.config(text=f"{filename}")

C = "aaaaaaaaaaaaaaaa"  # Globale variable. von hier wird name des hauptfensters genommen

if __name__ == "__main__":
    root = tk.Tk()
    root.title(C) # hauptfenster name definieren
    root.geometry("400x200") # Fenster größe definieren

    
    eingabefeld = tk.Entry(root, width=20)  # textfeld Breite in Zeichen
    eingabefeld.grid(row=0, column=2,)
    
    button2 = tk.Button(root,
        text="Fenstername ändern", command=changename
                        )
    button2.grid(row=0, column=3, padx=4)
    
    label1 = tk.Label(root, text="Wählen Sie eine Datei aus.")
    label1.grid(row=2, column=3, sticky="we")
    root.grid_rowconfigure(1, minsize=50)
    
    button1 = tk.Button(root,
                        text="Bild auswählen", command=choosefile)
    button1.grid(row=3, column=3, sticky="we")

    label2 = tk.Label(root, text="Inhalt aus QR-Code: ")
    label2.grid(row=4, column=2)
    
root.mainloop()