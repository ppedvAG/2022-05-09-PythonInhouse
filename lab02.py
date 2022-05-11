# Übung 1:
# Wir wollen mittels Kontrollstrukturen das kleine 1x1 nachbauen
# Es soll von jeder Zahl von 1 bis 10 das ganze 10er einmal eins gerechnet werden
# Die Ausgabe von jedem Schritt soll in der Konsole erfolgen
# "1 x 1 = 1"
#.. "10 x 10 = 100"

# Übung 2:
# FizzBuzz
# Von 1 bis 100 gezählt
# Jede Zahl wird auf ihre Teilbarkeit durch 3 und 5 geprüft
# Falls die Zahl NUR durch 3 teilbar ist soll die Konsole "Fizz" ausgeben
# Falls die Zahl NUR durch 5 teilbar ist soll die Konsole "Buzz" ausgeben
# Falls die Zahl  durch 3 und durch 5 teilbar ist soll die Konsole "FizzBuzz" ausgeben
# Falls die Zahl weder durch 3 noch durch 5 teilbar ist soll die Zahl selbst in der Konsole ausgegeben werden



for i in range(1,11):
    print(f"{i}'er Einmaleins:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print("-------------------")
    

for i in range(1, 101):
    answer = ""
    if i % 3 == 0:
        answer += "Fizz"
    if i % 5 == 0:
        answer += "Buzz"
    if answer == "":
        print(i)
    else:
        print(answer)