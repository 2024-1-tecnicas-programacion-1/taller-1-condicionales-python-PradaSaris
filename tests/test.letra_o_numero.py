import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.letra_o_numero import evaluar

class TestLetraONumero(unittest.TestCase):
    def test_es_numero(self):
        valor_esperado = "Es número"
        valor_actual = evaluar('5')
        self.assertEqual(valor_esperado, valor_actual)

    def test_es_letra_minuscula(self):
        valor_esperado = "Es letra minúscula"
        valor_actual = evaluar('f')
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_es_letra_mayuscula(self):
        valor_esperado = "Es letra mayúscula"
        valor_actual = evaluar('H')
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_no_es_letra_ni_numero(self):
        valor_esperado = "No es letra ni número"
        valor_actual = evaluar('+')
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    

if __name__ == '__main__':
    unittest.main()
