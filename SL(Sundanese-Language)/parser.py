from sly import Parser

import rhs_lexer

class BasicParser(Parser):
    tokens = rhs_lexer.BasicLexer.tokens

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/'),
        ('right', 'UMINUS'),
        )