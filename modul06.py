# from helpers import mathstuff
# from helpers.greeters import greet_world
# Wie oben funktioniert es immer
from helpers import *
from helpers import mathstuff
from helpers.foo import bar
# Mit stern können wir nur importieren, falls wir __all__ in der __init__.py befüllt haben

x = mathstuff.power(2,4)
print(x)

greeters.greet_world()
bar.sayHello()