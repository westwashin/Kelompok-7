from sly import Lexer
#dyrect lyblery dari laxer  
class Dasar(Lexer):
    tokens = { NAME, NUMBER, STRING, IF, PRINT, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '
    #menentukan token yang akan di ganti
    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    # Define tokens
    IF = r'UPAMI'
    PRINT = r'NYITAK'
    THEN = r'SATULUYNA'
    ELSE = r'NUSANES'
    FOR = r'PIKEUN'
    FUN = r'FUN'
    TO = r'KA'
    ARROW = r'JAMPARING'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value) #untuk memanggil hasil t.value
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = Dasar()
    env = {}
    while True:
        try:
            text = input('slg > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)

#akuaku