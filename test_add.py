# Damit der testrunner die Datei entdecken kann muss sie mit test beginnen
# Wir benutzen das unittest modul
import unittest
from helpers.mathstuff import add_numbers

# Eine Klasse muss erstellt werden, die für den Test zuständig ist

# So muss jede Testklasse aussehen
class TestAdd_Numbers(unittest.TestCase):
    
    def test_add(self):
        test_result = add_numbers(1, 2, 3)
        expected_result = 6
        self.assertEqual(test_result, expected_result, "Sollte 6 sein")
    
    def test_add_tuple(self):
        test_result = add_numbers(*(1, 2, 3, 4))
        expected_result = 10
        self.assertEqual(test_result, expected_result, "Sollte 10 sein")

if __name__ == "__main__":
    unittest.main()