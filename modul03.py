# Funktionen
# Scope
# Globaler Scope
# Ist im gesamten Skript ansprechbar



import re


firstName = "Marius"

# Lokaler Scope
# Ist nur innerhalb des BLockes ansprechbar
def greeter():
    greeting = "Hello world"
    firstName = "Max"
    print(greeting)
    if greeting:
        test = "Bye world"
        print(test)
        print(greeting)
    print(test)
    print(firstName)

greeter()
print(firstName)
# Python ablauf Namenssuche:
# Schaut immer als erstes im lokalen Scope nach der Variable#
# Falls im lokalen Scope nichts gefunden wird, wird der globale Scope durchsucht
# Falls im Globalen Scope nichts gefunden wird, schaut er im Namespace von Python und den importierten Modulen nach

# Definition von Funktionen:

def nameDerFunktion():
    print("Ich bin eine Funktion")

# Aufrufen von Funtkionen:
nameDerFunktion()

# Rückgabe erhalten:

def add(numOne: int, numTwo: int) -> int:
    return numOne + numTwo

sumOne = add(12, 55)
print(sumOne)
sumTwo = add("test", "Test")
print(sumTwo)
sumThree = add([1,2,3], [4,5,6])
print(sumThree)

# Können Vorschläge angeben, welcher Typ übergeben werden soll

def addInts(numOne: int, numTwo: int) -> int:
    numOne += 5
    if type(numOne) is int and type(numTwo) is int:
        return numOne + numTwo
    else:
        print("Wrong types")

print(addInts(55, 66))
sumFour = addInts(numTwo=100, numOne=23)
x = 10
addInts(x, 5) # Werte werden übergeben, also ändert sich x nicht nach dem Aufruf
def addNumbers(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(addNumbers(1,2,3,4,5,6,76,1231,41242543,6))
print(addNumbers(1,5))
print(addNumbers(1))

def arbitraryKwargs(**words):
    for key, value in words.items():
        print(f"Key: {key}: {value}")

arbitraryKwargs(test="Test1", test2=56, cool=True)
person = {"firstName": "Max", "LastName": "Mustermann", "Age": 54}
arbitraryKwargs(**person)
numberList = list(range(1, 500))
result = addNumbers(*numberList)
print(result)

# Unpacking Operator:
# Bei List: *listName
# Bei Dictionary: **dictName

# Default-Parameter
# = nach Parametername
def divide(numOne = 1, numTwo = 1):
    return numOne / numTwo

result = divide(50, 2)
print(result)
result = divide(12)
print(result)
print(divide())

def factorial(number):
    if number < 1:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(101))
test = factorial
test(997)
