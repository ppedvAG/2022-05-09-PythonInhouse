# Kontrollstrukturen
# If Bedingungen
import modul01


def main():
    zahlEins = 4
    zahlZwei = 40
    if zahlEins < zahlZwei:
        print(f"{zahlEins} ist kleiner als zahlZwei")
        # formatted String
        # f vor Anführungszeichen
    elif zahlEins == zahlZwei:
        print("Die Zahlen sind gleich groß")
    else:
        print(f"{zahlEins} ist größer als zahlZwei")

    if zahlEins % 2 == 0:
        print(f"{zahlEins} ist gerade")

    # Falls man if und else auf eine Zeile schreiben will:
    print(f"{zahlEins} ist gerade") if zahlEins % 2 == 0 else print(
        f"{zahlEins} ist ungerade")

    # Ternary:
    print(f"{zahlEins} ist kleiner als zahlZwei") if zahlEins < zahlZwei else print(
        f"{zahlEins} ist größer als zahlZwei") if zahlEins > zahlZwei else print("Die beiden Zahlen sind gleich groß")
    # Fall warh if bedingung else (falls ja if bedingung) else fall nein
    # if ... elif... else

    # Match-case

    testVariable = -150

    match testVariable:
        case 50:
            print("Jup ist 50")
        case 100 | 150:  # Erlaubt meherere cases in einer Zeile
            print("test ist 100")
        case _ if testVariable < 0:
            print("Zahl ist kleiner null")
        case _:
            print("Kein Fall eingetreten")

    # Schleifen in Python
    # Haben prinzipiell nur Kopfgesteuerte schleifen in Python

    # While-Syntax:
    # while Bedingung:
    #   CodeBlock
    counter = 0
    while counter < 50:
        if counter == 40:
            print("Wird abgebrochen weil 40 erreicht wurde")
            break  # beendet die aktuelle Schleife
        elif counter % 10 == 0:
            print("Ist durch 10 teilbar")
            counter += 1
            continue  # Überspringt die derzeitige Iteration
        print(counter)
        counter += 1

    counter = 0

    while True:
        print(counter)
        counter += 1
        if counter > 50:
            break
        # Nachgebaute Fußgesteuerte Schleife
        # Endlosschleife im While und Abbruchbedingung im Block

    #for-Schleife:
    # Syntax:
    # for Bedingung

    myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    firstName = "Max"
    for number in myList:
        print(number)

    for char in firstName:
        print(char)

    myDict = {"key1": "Test", "key2": "Test2", "key3": "Test3"}

    for (key, value) in myDict.items():
        print(f"Key: {key} | Value: {value}")

    for i in range(0, len(myList), 3):
        print(myList[i])
    # for (int i = 0; i < myList.length; i++)
    mySecondList = [[1, 2, 3], [4, 5, 6]]
    for listX in mySecondList:
        print(listX)
        for value in listX:
            print(value)
            
    for i in range(250, 149, -30):
        print(i)


if __name__ == "__main__":
    main()
