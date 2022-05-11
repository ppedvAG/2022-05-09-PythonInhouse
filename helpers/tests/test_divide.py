# Damit der testrunner die Datei entdecken kann muss sie mit test beginnen
# Wir benutzen das unittest modul
import unittest
from ..mathstuff import divide

# Eine Klasse muss erstellt werden, die für den Test zuständig ist

# So muss jede Testklasse aussehen
class TestDivide(unittest.TestCase):
    
    def test_divide(self):
        test_result = divide(12, 5)
        expected_result = 2.4
        self.assertEqual(test_result, expected_result, "Sollte 2.4 sein")
        # Bei floats eignet sich almostEqual oft besser, da die Zahlen minimalste unterschiede haben können
        
if __name__ == "__main__":
    unittest.main()
    
# Im Tab Testing beim test explorer auf die drei Punkte oben rechts => enable autorun
# Tests laufen immer durch, wenn wir was an der zu testenden Funktion ändern