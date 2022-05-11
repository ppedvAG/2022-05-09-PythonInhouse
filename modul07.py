# Lambdas in Python
from functools import reduce
from pyclbr import Function
import re


lambdaTest = lambda x, y : f"{x} * {y} = {x*y}"

result = lambdaTest(5,2)
print(result)
(lambda x,y : print(x*y))(2,4) # Immediatly invoked function

# Lambda als Parameter:

numberList = list(range(251))
print(numberList)

multiplesOf15 = list(filter(lambda x: x % 15 == 0, numberList))
print(multiplesOf15)
multiplesOf15 = list(map(lambda x: x*5, multiplesOf15))
print(multiplesOf15)

# Lambda als Ausdruck

def multiplier(number):
    return lambda numTwo: numTwo * number

doubler = multiplier(2)
x = doubler(5)
print(x)
trippler = multiplier(3)
print(trippler(x))

multi = multiplier

quadruple = multi(4)
print(quadruple(x))

# Lambdas werden haupstächlich als Parameter höherer Funktionen benutzt
# https://docs.python.org/3/library/functools.html
sumOfNums = reduce(lambda x,y : x+y, numberList)
print(sumOfNums)


# Übung zu filter und lambda
# Erstelle eine Liste von 1 bis 100(inklusive)
# filter die Liste so, dass nur noch gerade Zahlen enthalten sind
# Anschließend die Liste in der  Konsole ausgeben lassen

listTwo = list(range(1,101))
filteredList = list(filter(lambda x: x % 2 == 0, listTwo))
print(filteredList)

def isEven(number):
    return number % 2 == 0

filteredList = list(filter(isEven, listTwo))
print(filteredList)

# Funktionen sind First Class Objekte, also können sie zurückgegeben werden oder als Parameter benutzt werden

def greetPerson(name):
    return f"Hallo {name}"

greeting = greetPerson("Max")


def greet_world(greeter: Function):
    return greeter("Welt")

print(greeting)
greeting = greet_world(greetPerson)
print(greeting)

def outerFunction(number):
    def innerFunction1():
        return "Innere Funtktion 1"
    def innerFunction2():
        return "Innere Funktion 2"
    
    if number == 1:
        return innerFunction1() # Führt die Funktion aus und gibt die Rückgabe zurück
    elif number == 2:
        return innerFunction2 # Gibt nur eine Referenz auf die Funktion zurück und erlaubt späteres ausführen
    else:
        return "Not Found"
    

test1 = outerFunction(1)
print(test1) # String aus Zeile 77
test2 = outerFunction(2) # ist die Funktion innerFunction2, muss aber erst noch ausgeführt werden
print(test2())

def simpleDecorator(func):
    def wrapper():
        print("Ich werde vor der Funktion ausgeführt")
        func()
        print("Ich werde nach der Funktion ausgeführt")
    return wrapper
# Beim return nur die Referenz zurückgeben ohne die ()

def doTwice(func, **kwargs):
    def wrapper():
        func()
        print(kwargs)
        func()
    return wrapper

# Das @decoratorName übernimmt für mich Zeile 108
# Es übergibt also die unten erstellte Funktion als Referenz an meinen Decorator
@doTwice
@simpleDecorator
def say_hello():
    print("Hello!")

# Ältere Methode decorater zu benutzen
# say_hello = simpleDecorator(say_hello)
# say_hello = doTwice(simpleDecorator(say_hello))
# say_hello()
# Decorators wurden in version 2.2 eingeführt

say_hello()
# say_hello()