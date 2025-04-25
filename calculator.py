import math

class Calculator:
    """
    Classe que implementa uma calculadora simples com operações básicas.
    """
    def add(self, x, y):
        """
        Realiza a soma de dois números.
        
        Args:
            x (float): Primeiro número
            y (float): Segundo número
            
        Returns:
            float: Resultado da soma
        """
        return x + y

    def subtract(self, x, y):
        """
        Realiza a subtração de dois números.
        
        Args:
            x (float): Primeiro número
            y (float): Segundo número
            
        Returns:
            float: Resultado da subtração
        """
        return x - y

    def multiply(self, x, y):
        """
        Realiza a multiplicação de dois números.
        
        Args:
            x (float): Primeiro número
            y (float): Segundo número
            
        Returns:
            float: Resultado da multiplicação
        """
        return x * y

    def divide(self, x, y):
        """
        Realiza a divisão de dois números.
        
        Args:
            x (float): Primeiro número
            y (float): Segundo número
            
        Returns:
            float: Resultado da divisão
            
        Raises:
            ValueError: Se o divisor for zero
        """
        if y == 0:
            raise ValueError("Não é possível dividir por zero")
        return x / y

    def power(self, x, y):
        """
        Calcula a potência de um número.
        
        Args:
            x (float): Base
            y (float): Expoente
            
        Returns:
            float: Resultado da potência
        """
        return x ** y

    def square_root(self, x):
        """
        Calcula a raiz quadrada de um número.
        
        Args:
            x (float): Número para calcular a raiz quadrada
            
        Returns:
            float: Resultado da raiz quadrada
            
        Raises:
            ValueError: Se o número for negativo
        """
        if x < 0:
            raise ValueError("Não é possível calcular a raiz quadrada de um número negativo")
        return math.sqrt(x)
    
if __name__ == "__main__":
    # Exemplo de uso da calculadora
    calc = Calculator()
    print("Soma: 2 + 3 =", calc.add(2, 3))
    print("Subtração: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplicação: 2 * 3 =", calc.multiply(2, 3))
    print("Divisão: 6 / 2 =", calc.divide(6, 2))
    print("Potência: 2³ =", calc.power(2, 3))
    print("Raiz quadrada de 4 =", calc.square_root(4))
    