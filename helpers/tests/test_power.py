# Damit der testrunner die Datei entdecken kann muss sie mit test beginnen
# Wir benutzen das unittest modul
import unittest
from ..mathstuff import power

# Eine Klasse muss erstellt werden, die für den Test zuständig ist

# So muss jede Testklasse aussehen
class TestPower(unittest.TestCase):
    
    # def add_test(self): So wird der Test nicht ausgeführt
    def test_add(self):
        test_result = power(2, 2)
        expected_result = 4
        self.assertEqual(test_result, expected_result, "Sollte 4 sein")
    
    def test_add_tuple(self):
        test_result = power(5,2)
        expected_result = 25
        self.assertEqual(test_result, expected_result, "Sollte 10 sein")

if __name__ == "__main__":
    unittest.main() # Führt die Tests in der Datei aus
    
# Konsolenbefehl zum ausführen von allen Tests:
#  py -m unittest discover (-v verbos) (-s sourceDirectory) (-t)