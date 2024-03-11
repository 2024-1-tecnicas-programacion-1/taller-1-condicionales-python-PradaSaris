import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.edad import evaluar

class TestEdad(unittest.TestCase):
    def test2000Enero1(self):
        valor_esperado = "Usted tiene 24 años"
        valor_actual = evaluar(1, 1, 2000)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
    
    def test2005Abril21(self):
        valor_esperado = "Usted tiene 18 años"
        valor_actual = evaluar(21, 4, 2005)
        self.assertEqual(valor_esperado, valor_actual)

    def test1950Noviembre31(self):
        valor_esperado = "Usted tiene 73 años"
        valor_actual = evaluar(29, 11, 1950)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2019Junio20(self):
        valor_esperado = "Usted tiene 4 años"
        valor_actual = evaluar(20, 6, 2019)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test2026Mayo12(self):
        valor_esperado = "Fecha de nacimiento inválida"
        valor_actual = evaluar(12, 5, 2026)
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
