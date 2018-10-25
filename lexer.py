import ply.lex as lex

tokens = [
    'NUM',
    'WORD'
]

t_WORD = r'[a-zA-Z]+'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Ignore spaces and words
t_ignore = ' \t'

# Build the lexer
lexer = lex.lex()

def fetchNum(inputStream):
    lex.input(inputStream)
    for tok in lexer:
        if(tok.type == 'NUM'):
            return tok.value

def fetchWord(inputStream, keyword):
    lex.input(inputStream)
    for tok in lexer:
        if(tok.type == 'WORD' and tok.value.lower() in keyword):
            return True
