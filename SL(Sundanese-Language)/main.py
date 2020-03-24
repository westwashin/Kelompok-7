
import sls_interpreter

from sys import *

#untuk menggunakan lexer dan parser
lexer = sls_lexer.BasicLexer()
parser = sls_parser.BasicParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    sls_interpreter.BasicExecute(tree, env)