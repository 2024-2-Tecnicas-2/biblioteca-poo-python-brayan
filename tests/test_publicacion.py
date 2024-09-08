import sys
import os
import unittest


# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from publicacion import Publicacion

class TestPublicacion(unittest.TestCase):
   
    def test_set_titulo(self):
        publicacion = Publicacion()
        publicacion.set_titulo("Brayan")
        self.assertEqual("Brayan", publicacion.get_titulo())

    def test_set_ano_publicacion(self):
        publicacion = Publicacion()
        publicacion.set_ano_publicacion(1999)
        self.assertEqual(1999, publicacion.get_ano_publicacion())

if __name__ == '__main__':
    unittest.main()
