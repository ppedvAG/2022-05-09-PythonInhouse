import modul02

def main():
    # Die print() Funktion gibt alle Parameter in der Konsole aus
    print("Hallo Welt")
    # Ich bin ein Kommentar und werde vom Interpreten ignoriert
    # Variablen:
    # Namen angebenen = Wert
    # Brauchen keinen Typen angeben, da Python  dynmaisch typisiert ist
    firstName = "Marius"
    # Bei Strings ist es egal ob wir einfache oder doppelte Anfürhungszeichen benutzen
    # Datentypen in Python:
    # str - String Alles was mit Anführungszeichen umschlossen ist
    lastName = 'Sommer'
    # escape : \ vor dem Sonderzeichen
    # int - Integer Alle Ganzzahlen
    zahlEins = 15
    # float - Gleitkommazahlen
    kommazahlEins = 4.2  # Muss mit punkt sein
    # complex - Komplexe Zahlen
    komplexeZahl = (5j + 2)
    # bool - Boolean wahr/falsch
    boolean = True  # False
    # dict - Dictionary
    # Sammlung von key: value Paaren
    dictEins = {"firstName": "Max", "lastName": "Mustermann",
                "age": 34, "employed": True, "te'st": "test"}
    print(dictEins["employed"])
    # Dictionary Methoden:
    # dict.get("schlüssel") Gibt den Wert des Keys zurück
    # Falls der Key nicht vorhanden ist wird none zurückgegeben
    print(dictEins.get("hallo"))  # none
    # dict.items() GIbt alle Key:Value Paare als Liste aus Tupeln zurück
    print(dictEins.items())
    # dict.keys() Gibt alle Keys als list zurück
    print(dictEins.keys())
    # dict.values() Gibt alle Values als Liste aus
    print(dictEins.values())
    # dict.copy() GIbt eine Kopie des Dictionaries zurück
    dictZwei = dictEins.copy()
    # dict.pop("key") löscht das Key:Value paar mit dem angegeben Schlüssel
    dictZwei.pop("te'st")
    print(dictZwei)  # Jetzt ohne "test"
    print(dictEins)
    # dict.popitem() löscht letztes Element aus dem dictionary
    dictZwei.popitem()
    print(dictZwei)  # Jetzt ohne employed
    # Verändern von Werten
    # Entweder direkt über die Klammernschreibweise
    dictZwei["age"] = 44
    print(dictZwei)
    # Per dict.update({"key": "value"})
    # Falls nicht vorhanden wird das K:V-Paar neugesetzt
    dictZwei.update({"age": 55})
    dictZwei.update({"test": 12})
    print(dictZwei)
    # dict.setdefault("key", "value")
    # Falls der Key bereits vorhanden ist wird der Wert davon zurückgegeben, falls er nocht nicht
    # existiert wird er  mit dem vlaue neugesetzt
    print(dictZwei.setdefault("age", 66))
    print(dictZwei.setdefault("test2", 500))
    print(dictZwei)
    # dict.clear() Löscht den Inhalt des Dictionaries
    dictZwei.clear()
    print(dictZwei)
    # Lists
    # Können Duplikate enthalten
    # Können aus verschiedenen Typen bestehen
    # Starten bei Index: 0
    # Sind veränderbar, d.h. neue elemente dazu oder bestehende sind löschbar
    listEins = ["Test", 1, 2, 4, True]
    print(listEins)
    print(listEins[3])
    # Startet bei Index 2 und gibt alles bis exklusive Index 4 aus
    print(listEins[2:4])
    print(listEins[-1])  # Fängt von hinten an zu zählen
    listEins[0] = 0  # Verändert den Wert am angegebenen Index
    listEins[-1] = 5
    print(listEins)
    # list.append(value) Fügt den Wert am Ende der Liste an
    listEins.append(6)
    # list.copy() Gibt eine Kopie der Liste zurück
    listZwei = listEins.copy()
    # list.count(wert) zählt wie oft der Wert in der Liste enthalten ist
    print(listZwei.count(1))
    # list.index(wert) gibt an an welcher Indexposition der gesuchte wert steht
    print(listZwei.index(4))
    # Falls das Element nicht in der Liste enthalten ist wird ein ValueError geworfen
    # list.insert(index, wert)
    # Fügt den Wert am entsprechendne Index ein
    listZwei.insert(2, 9)
    print(listZwei)
    # Länge von einem list/dict/string usw.:
    print(len(listEins))
    # list.reverse() Dreht die Reihenfolge der Liste um
    listZwei.reverse()
    print(listZwei)
    # list.sort() Standardmäßig alphanumerisch aufsteigen
    listZwei.sort()
    print(listZwei)
    # list.extend(listZwei)
    listZwei.extend(listEins)
    print(listZwei)
    listZwei.sort()
    print(listZwei)
    # list.pop(index) Element an der Stelle wird gelöscht und zurückgegeben
    listZwei.pop(0)
    print(listZwei)
    # list.remove("wert") Entfernt den Wert am ersten Fundort
    listZwei.remove(1)
    print(listZwei)
    # list.clear() Löscht die gesamte Liste
    listZwei.clear()
    print(listZwei)

    # Tuple
    # Sind der Liste sehr ähnlich
    # Sind nicht veränderbar
    # Können verschiedene Datentypen enthalten
    tupleEins = (2, 4, 4)
    # tuple.count(wert) Zählt wie oft das gesuchte Element im Tupel enthalten ist
    print(tupleEins.count(4))
    # tuple.index(wert) gibt den Index des Elementes zurück
    print(tupleEins.index(4))
    # tupleEins[1] = 5
    tempList = list(tupleEins) # Konvertiert unser Tuple zu einer Liste
    tempList[1] = 5
    tupleEins = tuple(tempList)
    print(tupleEins)
    # Range
    # nichtveränderbare Sequenz von Integern
    rangeEins = range(101) # Generiert eine range beginnend bei 0 und endend bei 100
    print(rangeEins)
    rangeEins = list(rangeEins)
    print(rangeEins)
    # range(ende) Nicht inklusiv
    # range(start, ende)
    # range(start, ende, schrittgröße)
    rangeZwei = list(range(0,51, 5))
    print(rangeZwei)
    rangeDrei = list(range(500, 249, -10))
    print(rangeDrei)
    # Wird meistens beim iterieren benutzt
    # Set
    # kein Index
    # DUplikate sind zwar prinzipiell erlaubt, aber werden nicht aufgelistet
    # Neue Elemente können angefügt werden, aber nicht bestehende verändern
    setEins = {"Test", "Eins", "Test", "Zwei"}
    print(setEins)
    # .clear() Leert das Set
    # .copy() Kopiert das Set und gibt ein neues Zurück
    # .remove(Wert) Entfernt das Element falls vorhanden, ansonsten Fehler
    # .pop() Entfernt ein zufälliges Element aus dem Set und gibt es zurück
    print(setEins.pop())
    setZwei = {"Test", "drei", "vier"}
    # set.add("wert") Fügt ein neues Element ans Set an
    setZwei.add("sechs")
    # set.intersection(set2) Gibt ein neues Set züruck, das nur aus den Überschneidungen von set und set2
    # besteht
    setDrei = setEins.intersection(setZwei)
    print(setDrei)
    # set.intersection_update(set2) Entfernt alle Element, die nicht in beiden Sets enthalten sind
    setEins.intersection_update(setZwei)
    print(setEins)
    # set.difference(set2) gibt ein Set zurück, das nur aus den Elementen besteht die nicht in beiden
    # sets vorkommen
    setVier = setEins.difference(setZwei) 
    print(setVier)
    setZwei.difference_update(setEins) # Entfernt elemente aus dem Set, die auch im  anderen enthalten sind
    print(setZwei)
    setFünf = setEins.union(setZwei) # kombiniert die Sets zu einem neuen
    print(setZwei.issubset(setEins))
    # set.issubset(set2) Prüft ob set komplett in set2 enthalten ist, True falls ja
    # set.issuperset(set2) Prüft ob set2 komplett in set enthalten ist, True falls ja
    # set.isdisjoint(set2) Prüft ob keins der Elemente von set in set2 enthalten ist, True falls ja
    

if __name__ == "__main__":
    main()
