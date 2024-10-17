#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.a_functions import test_config, reverse_string
from src.question_b.b_functions import get_bonus_pay_amount
from src.question_c.c_functions import get_person_category
from src.question_d.d_functions import get_assessment_value, get_tax_assessed

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_reverse_string(self):
        self.assertEqual('dlrow olleh', reverse_string('hello world'))

    def test_bonus_pay(self):
        self.assertEqual("Invalid", get_bonus_pay_amount(-1))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        self.assertEqual("Invalid", get_bonus_pay_amount(2000))

    def test_person_category(self):
        self.assertEqual("Infant", get_person_category(1))
        self.assertEqual("Child", get_person_category(2))
        self.assertEqual("Teenager", get_person_category(14))
        self.assertEqual("Adult", get_person_category(20))

    def test_assessment_value(self):
        self.assertEqual(6000, get_assessment_value(10000))
        self.assertEqual(12000, get_assessment_value(20000))
    
    def test_tax_assessment(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
        self.assertEqual(72, get_tax_assessed(10000))