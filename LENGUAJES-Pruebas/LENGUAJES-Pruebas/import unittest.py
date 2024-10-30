import unittest
from Parcial import lexer

# test_Parcial.py


class TestLexer(unittest.TestCase):

    def test_reserved_words(self):
        code = "def if else return"
        expected_tokens = [
            '<def,1,1>', '<if,1,5>', '<else,1,8>', '<return,1,13>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_operators(self):
        code = "== != <= >= -> + - * / % = < > : ( ) [ ] { } , . ; __ @"
        expected_tokens = [
            '<tk_igual,1,1>', '<tk_distinto,1,4>', '<tk_menor_igual,1,7>', '<tk_mayor_igual,1,10>',
            '<tk_ejecuta,1,13>', '<tk_suma,1,16>', '<tk_resta,1,18>', '<tk_mult,1,20>', '<tk_div,1,22>',
            '<tk_modulo,1,24>', '<tk_asig,1,26>', '<tk_menor,1,28>', '<tk_mayor,1,30>', '<tk_dos_puntos,1,32>',
            '<tk_par_izq,1,34>', '<tk_par_der,1,36>', '<tk_corchete_izq,1,38>', '<tk_corchete_der,1,40>',
            '<tk_llave_izq,1,42>', '<tk_llave_der,1,44>', '<tk_coma,1,46>', '<tk_punto,1,48>', '<tk_punto_y_coma,1,50>',
            '<tk_doble_raya,1,53>', '<tk_overide,1,56>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_identifiers(self):
        code = "variable1 _variable2 var_3"
        expected_tokens = [
            '<id,variable1,1,1>', '<id,_variable2,1,11>', '<id,var_3,1,22>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_numbers(self):
        code = "123 456.789"
        expected_tokens = [
            '<tk_entero,123,1,1>', '<tk_flotante,456.789,1,5>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_strings(self):
        code = '"hello" \'world\''
        expected_tokens = [
            '<tk_cadena,"hello",1,1>', '<tk_cadena,\'world\',1,8>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_comments(self):
        code = "123 # this is a comment\n456"
        expected_tokens = [
            '<tk_entero,123,1,1>', '<tk_entero,456,2,1>'
        ]
        self.assertEqual(lexer(code), expected_tokens)

    def test_errors(self):
        code = "123.456.789"
        expected_tokens = [
            '<tk_flotante,123.456,1,1>', '>>> Error lexico(linea:1,posicion:8)'
        ]
        self.assertEqual(lexer(code), expected_tokens)

if __name__ == '__main__':
    unittest.main()