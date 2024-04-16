import unittest
from calculadora import Calculadora

class Test_calculadora(unittest.TesteCase):
   def setUp(self)->None:
      self.calc = Calculadora()

def teste_soma(self):
      self.assertEqual(self.calc.soma(10,10), 20)
      













if __name__ == '__main__':
    unittest.main()
