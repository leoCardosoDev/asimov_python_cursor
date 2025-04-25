# Calculadora em Python

Este projeto implementa uma calculadora simples em Python com operações matemáticas básicas.

## Funcionalidades

A calculadora oferece as seguintes operações:

- **Soma**: Adiciona dois números
- **Subtração**: Subtrai dois números
- **Multiplicação**: Multiplica dois números
- **Divisão**: Divide dois números (com tratamento para divisão por zero)
- **Potência**: Calcula a potência de um número
- **Raiz Quadrada**: Calcula a raiz quadrada de um número (com tratamento para números negativos)

## Estrutura do Projeto

O projeto é composto por dois arquivos principais:

- `calculator.py`: Contém a implementação da classe `Calculator` com todos os métodos matemáticos
- `test_calculator.py`: Contém os testes unitários para garantir o funcionamento correto da calculadora

## Como Usar

Para utilizar a calculadora, basta instanciar a classe `Calculator` e chamar os métodos desejados:

```python
from calculator import Calculator

calc = Calculator()

# Exemplos de uso
resultado_soma = calc.add(2, 3)        # Retorna 5
resultado_subtracao = calc.subtract(5, 3)  # Retorna 2
resultado_multiplicacao = calc.multiply(2, 3)  # Retorna 6
resultado_divisao = calc.divide(6, 2)  # Retorna 3
resultado_potencia = calc.power(2, 3)   # Retorna 8
resultado_raiz = calc.square_root(4)    # Retorna 2
```

## Testes

O projeto inclui testes unitários abrangentes para todas as operações. Para executar os testes, use o comando:

```bash
python -m unittest test_calculator.py
```

Os testes verificam:
- Operações básicas com números positivos
- Operações com números negativos
- Casos especiais (como divisão por zero)
- Operações com zero
- Tratamento de erros

## Tratamento de Erros

A calculadora inclui tratamento de erros para casos especiais:
- Divisão por zero
- Raiz quadrada de números negativos

## Requisitos

- Python 3.x
- Módulo `math` (incluído na biblioteca padrão do Python)

## Contribuição

Sinta-se à vontade para contribuir com o projeto através de pull requests ou reportando issues. 