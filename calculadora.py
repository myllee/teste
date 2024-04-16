import unittest


class Calculadora:
    def __init__(self):
        pass

    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y
    
    def multiplicacao(self, x, y):
        return x * y

    def divisao(self, x, y):
        if y == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return x / y
    
class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Calculadora()
    
    def teste_soma(self):
        self.assertEqual(self.calc.soma(12,13), 25)
        self.assertEqual(self.calc.soma(100,400), 500)

    def teste_subtracao(self):
        self.assertEqual(self.calc.subtracao(10,5), 5)
        self.assertEqual(self.calc.subtracao(20,10), 10)

    def teste_multiplicacao(self):
        self.assertEqual(self.calc.multiplicacao(10,5), 50)
        self.assertEqual(self.calc.multiplicacao(5,5), 25)

    def teste_divisao(self):
        self.assertEqual(self.calc.divisao(10,2), 5)
        self.assertEqual(self.calc.divisao(20,5), 4)

    
        
    
   
if __name__ == '__main__':
    unittest.main()

    