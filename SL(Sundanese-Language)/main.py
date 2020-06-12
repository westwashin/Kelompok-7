import sunda_lexer
import sunda_parser
import sunda_interpreter

from sys import *

#MASUKAN LANGSUNG
if __name__ == '__main__':
    lexer = sunda_lexer.BasicLexer()
    parser = sunda_parser.BasicParser()
    env = {}
    while True:
        try:
            text = input('RHS > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            sunda_interpreter.BasicExecute(tree, env)
