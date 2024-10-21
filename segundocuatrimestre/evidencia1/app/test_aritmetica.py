#PRUEBA DE test_aritmetica.py

#Cada operacion del Test, tiene 2 componentes a operar (ambos entre paréntesis), y un resultado por fuera de este. 

#El test, reliza un análisis de las operaciones según la función elegida del módulo aritmética. Si alteramos algunos de los resultados fuera de los paréntesis, el Error se muestra en la terminal didicada, y muestra cual es el resultado correcto. Al igual que si se altera, cualquiera de los componentes de la fórmula.  

import unittest

from aritmetica import sumar, restar, multiplicar, dividir

class TestAritmetica(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(1, 2), 3)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)

    def test_restar(self):
        self.assertEqual(restar(10, 5), 5)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)

    def test_multiplicar(self):
        self.assertEqual(multiplicar(3, 7), 21)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)

    def test_dividir(self):
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(-10, -2), 5)
        with self.assertRaises(ValueError):
            dividir(10, 0)

#En al caso del Test de division, si se intenta dividir por 0 (cero), el test lanza dicho error. "EL DIVISOR NO PUEDE SER IGUAL A CERO"

if __name__ == '__main__':
    unittest.main()