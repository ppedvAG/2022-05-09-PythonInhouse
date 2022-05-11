from . import greeters
# Falss man relative Pfade beim importieren benutzt, muss das Modul wissen was sein parent Package ist
# => python -m {parentName}.{moduleName} behebt das Problem

def add_numbers(*number):
    sum = 0
    for i in number:
        sum += i
    return sum

def power(numOne, numTwo):
    return numOne**numTwo

def divide(numOne, numTwo):
    return numOne / numTwo

greeters.greet_world()