import sys
import os
import unittest



# Add the 'src' directory to the Python path so 'calculadora' can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from libro import Libro

class TestLibro(unittest.TestCase):
 
    def test_set_titulo(self):
        libro = Libro("marcelo", 200, "si", 2004)
        self.assertEqual("marcelo", libro.get_autor())
        self.assertEqual(2004, libro.get_ano_publicacion())
        self.assertEqual(200, libro.get_numero_paginas())

    '''def test_to_string(self):
        libro = Libro("Harry Potter", 500, "J.K. Rowling", 2024)
        expected = "Libro{Titulo='Harry Potter', Numero_de_paginas=500, Autor='J.K. Rowling', Ano_publicacion=2024}"
        self.assertEqual(expected, str(libro))'''

    def test_getters(self):
        libro = Libro("volar alto", 888, "Márquez", 2000)
        self.assertEqual("Márquez", libro.get_titulo())
        self.assertEqual(888, libro.get_numero_paginas())
        self.assertEqual("volar alto", libro.get_autor())
        self.assertEqual(2000, libro.get_ano_publicacion())


if __name__ == '__main__':
    unittest.main()
