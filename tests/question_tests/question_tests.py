#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_b.question_b import get_fahrenheit
from src.question_a.question_a import get_assessment_value, get_tax_assessed, test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())


    def test_get_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))

    def test_get_tax_assessed(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))

    def test_get_fahrenheit(self):
        self.assertEqual(32, get_fahrenheit(0))
        self.assertEqual(41, get_fahrenheit(5))
        self.assertEqual(50, get_fahrenheit(10))