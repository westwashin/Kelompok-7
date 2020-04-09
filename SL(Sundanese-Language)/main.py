
import sls_interpreter

from sys import *

#untuk menggunakan lexer dan parser
lexer = sls_lexer.BasicLexer()
parser = sls_parser.BasicParser()
env = {}