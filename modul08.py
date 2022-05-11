from cmath import log
from decimal import DivisionByZero
import logging
from sys import exc_info

logging.basicConfig(level=logging.DEBUG, filename="exceptions.log",
                    format="%(name)s %(levelname)s %(process)d %(asctime)s - %(message)s",
                    datefmt="%d-%m-%Y %H:%M:%S")


try:
    print(10 / 0)
except ZeroDivisionError as e: # Wird nur bei Division durch 0 ausgeführt
    print(e)
    print("Es kann nicht durch 0 geteilt werden")
    # logging.error(f"Exception aufgetreten: {e}") Übergibt die Fehlermeldung direkt
    # logging.error("Exception trat auf", exc_info=True) # Überträgt den gesamten Traceback in die Logging-Datei
    logging.exception("Exception trat auf") # Ist immer loglevel Exception
    # Hängt den Traceback auch an
    # Da es die gesamte exception info mitübergibt sollte es nur in einem except block stehen
except TypeError as e: # wird nur bei TypeError ausgeführt
    print(e)
    print("Es muss durch einen Integer oder einen Float geteilt werden")
except NameError as e: # Falls die Variable undeklariert ist
    print(e)
    print("Die Variable gibt es nicht")
except Exception as e: # Als catch-all das jeden Fehler einfängt, de rnicht schon spezifischer behandelt wurde
    print(e)
    print("Ein unerwarteter Fehler ist aufgetreten")
else: # Wird nur durchgeführt, falls kein Fehler auftrat
    print("Programm wurde ohne Fehler durchgeführt")
finally: # Wird immer ausgeführt
    print("Programm wird beendet")
    

try:
    file = open("Test3.txt", "r")
    x = "Ich bin ein text"
except FileNotFoundError as e:
    print(e)
    print("Datei wurde nicht gefunden")
else:
    lines = file.readlines()
    print(lines)
    file.close()
finally:
    print("Datei wurde geschlossen")
    

# Eigene Exceptions erstellen:

class IdError(Exception):
    def __init__(self, message="Die Id darf nicht kleiner 0 sein"):
        self.message = message
        super().__init__(self.message)


try:
    x = int(input("Gib eine Zahl ein:\n"))
    assert (x > 0), "Id darf nicht kleiner 0 sein"
    y = int(input("Gib eine weitere Zahl ein:\n"))
    
    if x < 0 : raise IdError()
except ValueError as e:
    print(e)
    print("Es können nur Zahlen eingegeben werden")
except IdError as e:
    print(e)
except AssertionError as e:
    print("Assertion war falsch")
else:
    print(x + y)