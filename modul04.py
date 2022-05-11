# Klassen in Python
# Sind "Blaupausen"
# Ihre Attribute und Methoden sind public
# Ermöglichen Vererbung
# Definition:
# class ClassName(erbt von)

from re import S
from typing import NewType

Vehicle = NewType("Vehicle", object)

class Vehicle():
    x = 100 # Klassen-Variable
    
    # Constructor:
    def __init__(self,  hp: int, maxSpeed: float, wheels: int = 8) -> Vehicle:
        """Erstellt eine neue Instanz der Klasse Auto

        Args:
            hp (int): _description_
            maxSpeed (float): _description_
            wheels (int, optional): _description_. Defaults to 8.

        Returns:
            Vehicle: Die neu erstellte Instanz
        """
        self.wheels = wheels
        self.hp = hp
        self.maxSpeed = maxSpeed
        self.engineStatus = False
        self.currentSpeed = 0
    # Methode     
    def __str__(self):
        return f"Ein Fahrzeug mit {self.wheels} Rädern, einer derzeitigen Geschwindigkeit von {self.currentSpeed} km/h und einer maximalen Geschwindigkeit von {self.maxSpeed} km/h"

    def switchEngine(self):
        """ Ändert den Motorstatus
        """
        self.engineStatus = not self.engineStatus
        
    @classmethod
    def set_x(cls, newVal):
        cls.x = newVal

# Erstellen einer Instanz

bmw = Vehicle(maxSpeed = 120,hp= 250)

print(type(bmw))
print(f"{bmw}")
print(bmw.engineStatus)
bmw.switchEngine()
print(bmw.engineStatus) # Spricht das Attribut direkt an
bmw.engineStatus = True
bmw.currentSpeed = 125
# Können die Attribute direkt verändern
print(bmw)
bmw.brand = "BMW"
bmw.model = "i3"
del bmw.model
del bmw.engineStatus
# print(bmw.model)
# del bmw.x # Fehler, da man keine Klassenvariablen löschen kann
print(type(bmw))

# Erstellt eine Klasse Lebewesen
# Sie soll folgende Attribute haben:
# Spezies
# Extremitäten
# Alter
# Sie soll über eine __str__ Methode verfügen, die alle attribute auflistet, die wir definiert haben
# Und eine altern Methode, die bei jedem Aufruf das ALter um 1 erhöht

class Lebewesen:
    def __init__(self, spezies, extremitäten, alter):
        self._spezies = spezies
        self.extremitäten = extremitäten
        self.alter = alter
        
    @property
    def spezies(self):
        return f"Spezies: {self._spezies}"
    
    @spezies.setter
    def spezies(self, neueSpezies):
        print("Spezies kann nicht geändert werden")
        return self.spezies

    def __str__(self):
        # return str(self.__dict__)
        return f"Spezies: {self.spezies} | Alter: {self.alter}"
    
    def altern(self):
        self.alter += 1
    
    def testMethode(test):
        print(test)
    
    @classmethod
    def test_lebewesen(cls):
        return cls("test", 8, 12)

pferd = Lebewesen("Pferd", 4 , 5)
print(pferd.spezies)
print(pferd._spezies)
testLebewesen = Lebewesen.test_lebewesen()
print(testLebewesen)

pferd.spezies = "Hund"
print(pferd.spezies)
pferd._spezies = "Hund"
print(pferd.spezies)

class Mensch(Lebewesen):
    def __init__(self, alter, geschlecht, vorname, nachname):
        super().__init__(spezies = "Mensch", extremitäten = 4, alter=alter)
        self.geschlecht = geschlecht
        self.vornamen = vorname
        self.nachname = nachname
    
    def _altern(self):
        super().altern()
        self.alter += 1
        
    def __str__(self):
        # return str(self.__dict__)
        return f"Spezies: {self.spezies} | Alter: {self.alter} | Name: {self.vornamen}"
    
    def testMethode(test, test2):
        print(test, test2)

maxi = Mensch(23, "männlich", "Max", "Mustermann")
print(maxi.spezies)
maxi.spezies = "Hund"
print(maxi)
# Wenn ich die Methode der Elternklasse aufrufen will, muss ich diese direkt ansprechen und meine Instanz als Referenz übergeben
Lebewesen.altern(maxi)
# Normaler aufruf:
maxi.altern()
print(maxi)


def testOverload(x = None, y = None, z = None):
    if x:
        print(x)
    else:
        print("Nichts angekommen")
    if y and z:
        print(x + y + z)
    if y:
        print(x + y)
        
testOverload(2, 3, 4)

