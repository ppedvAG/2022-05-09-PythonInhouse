# In & Output:

def createFile():
    # fileName = input("Wie soll die Datei heißen?\n")
    # fileName += ".txt"
    # open(fileName, modus)
    # Möglichkeiten für den zweiten parameter
    # x - Erstellt die Datei, Fehler falls sie bereits existiert
    # w - Write Öffnet die Datei und überschreibt derzeitigen inhalt
    # r - read liest die Datei ein, kann nichts verändern, Fehler falls die Datei nicht existiert
    # a - Append, Öffnet die Datei und hängt neue Zeilen an
    #! Falls auf diese Art geöffnet braucht es auch immer ein close
    # Mit with, wird die Verbindung geöffnet und nach Ende des Blockes wieder geschlossen
    # Mit Zusatz "b" wird die Datei im binary Mode eingelsen oder geschrieben
    # Z.B: für pdfs
    with open("Grundlagen.pdf", "rb") as fileOne:
        lines = fileOne.readlines()
        with open("binary.txt", "wb") as fileTwo:
            fileTwo.writelines(lines)
            # writeToFile(file)
    
    
    

def writeToFile(file):
    lines = []
    while True:
        userInput = input("Schreib etwas:\n")
        if userInput.lower() in ["exit", "e"]:
            file.writelines(lines)
            break
        else:
            userInput += "\n"
            lines.append(userInput)
createFile()

# os-Modul

import os 

# Modul für Interaktionen mit dem Betriebssystem

path = os.getcwd() # Gibt derzeitgen Arbeitspfad zurück
# os.mkdir("NewFolder") 
# Erstellt einen neuen Ordner
# Wirft Fehler, falls er bereits existiert
print(os.listdir(path))
# Gibt eine Liste von Dateien und Ordnern im Pfad zurück

print(os.path.exists(path + "\\Grundlagen.pdf"))
# Prüft ob die Gesuchte Datei/Ordner existieren