import sys
from pathlib import Path
import unittest

# Se adiciona el path del directorio padre,
# para que podamos ejecutar los tests sin inconveniente
root_path = Path(__file__).resolve().parent.parent
print('root_path:')
print(root_path)
sys.path.append(str(root_path))

from src.set_de_tenis import evaluar

class TestSetDeTenis(unittest.TestCase):
    def test_aun_no_termina(self):
        valor_esperado = "Aún no termina"
        valor_actual = evaluar(4, 5)
        self.assertEqual(valor_esperado, valor_actual)
    
    # TODO: Agrega tus otros casos de prueba aquí
        
    def test_gano_a(self):
        valor_esperado = "Ganó A"
        valor_actual = evaluar(6, 4)
        self.assertEqual(valor_esperado, valor_actual)
    
    def test_gano_b(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(5, 7)
        self.assertEqual(valor_esperado, valor_actual)

    def test_invalido(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(1, 7)
        self.assertEqual(valor_esperado, valor_actual)
    def test_ultimo_juego(self):
        valor_esperado = "Ganó B"
        valor_actual = evaluar(6, 7)
        self.assertEqual(valor_esperado, valor_actual)
    def test_prueba_borde(self):
        valor_esperado = "Inválido"
        valor_actual = evaluar(999999, 999997)
        self.assertEqual(valor_esperado, valor_actual)
if __name__ == '__main__':
    unittest.main()
