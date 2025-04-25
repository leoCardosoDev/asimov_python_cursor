import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Classe de testes para a calculadora.
    Implementa testes para todas as operações matemáticas básicas.
    """
    def setUp(self):
        """Configuração inicial para cada teste"""
        self.calc = Calculator()

    def test_add(self):
        """Testa a operação de soma"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Testa a operação de subtração"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """Testa a operação de multiplicação"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        """Testa a operação de divisão"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        
    def test_divide_by_zero(self):
        """Testa o tratamento de divisão por zero"""
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Testa a operação de potência"""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(2, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)

    def test_square_root(self):
        """Testa a operação de raiz quadrada"""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(0), 0)
        with self.assertRaises(ValueError):
            self.calc.square_root(-1)

if __name__ == '__main__':
    unittest.main() 