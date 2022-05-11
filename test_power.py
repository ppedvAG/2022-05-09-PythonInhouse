# Damit der testrunner die Datei entdecken kann muss sie mit test beginnen
# Wir benutzen das unittest modul
import unittest
from helpers.mathstuff import power

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

# assertEqual(a,b) assertNotEqual(a,b) prüft ob die Werte übereinstimmen
# assertAlmostEqual(a,b, genauigkeit) 
# assertTrue(a) | assertFalse(a) püft ob a truthy oder falsey ist
# assertIs(a, b) | assertIsNot(a,b) prüft ob a die selbe id wie b hat
# assertIsNone(a) Pürft ob a None ist
# assertIsInstance(a, b) | assertIsNotInstance(a, b) püft ob a eine Instanz von b ist
# assertIn(a, b) | assertNotIn(a, b) prüft ob a in b enthalten ist
# https://docs.nose2.io/en/latest/