import sys
import os
import unittest



# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from revista import Revista

class TestRevista(unittest.TestCase):
   

    def test_revista(self):
        # Crear una revista con valores específicos
        revista = Revista(163, "Estefi", "errote", 2026)

        # Comprobar que los métodos get devuelven los valores correctos
        self.assertEqual("errote", revista.get_titulo())  # Usar el getter heredado
        self.assertEqual(2026, revista.get_ano_publicacion())  # Usar el getter heredado
        self.assertEqual(163, revista.get_numero_revistas())
        self.assertEqual("Estefi", revista.get_nombre_revista())

        # Comprobar el método __str__()
        expected = "Revista{Titulo=errote, anoPublicacion=2026, NumeroRevistas=163, NombreRevista=Estefi}"
        self.assertEqual(expected, str(revista))

    def test_invalido(self):
        # Probar con valores inválidos, como un año de publicación futuro
        revista_futura = Revista(5, "NombreRevista", "cy", 2015)
        self.assertEqual(5, revista_futura.get_numero_revistas())
        self.assertEqual(2015, revista_futura.get_ano_publicacion(), "El año de publicación debe ser 2015")

if __name__ == '__main__':
    unittest.main()