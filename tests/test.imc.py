import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.imc import evaluar

class TestIMC(unittest.TestCase):
    def testBajo(self):
        valor_esperado = "bajo"
        valor_actual = evaluar(50, 1.8,   20)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
        
    def testAlto(self):
        valor_esperado = "alto"
        valor_actual = evaluar(90, 1.72,   50)
        self.assertEqual(valor_esperado, valor_actual)
    
    def testmedio(self):
        valor_esperado = "medio"
        valor_actual = evaluar(70, 1.27,   25)
        self.assertEqual(valor_esperado, valor_actual)
        

if __name__ == '__main__':
    unittest.main()
